-- 1 Integrated patient and admission counts by source and continent.

SELECT 
    m.source_system AS source_and_continent,
    COUNT(DISTINCT p.global_patient_id) AS distinct_patients,
    COUNT(DISTINCT a.global_admission_id) AS distinct_admissions
FROM "Unified_Patients" p
JOIN "Map_Patients" m ON p.global_patient_id = m.global_patient_id
LEFT JOIN "Unified_Admissions" a ON p.global_patient_id = a.global_patient_id
GROUP BY m.source_system
ORDER BY m.source_system;

-- 2. Admission counts by standardized admission type across continents.

SELECT 
    m.source_system AS continent,
    a.admission_type,
    COUNT(*) AS admission_count
FROM "Unified_Admissions" a
JOIN "Map_Admissions" m ON a.global_admission_id = m.global_admission_id
GROUP BY m.source_system, a.admission_type
ORDER BY m.source_system, admission_count DESC;

-- 3. The most frequently assigned primary ICD-9 diagnoses by continent.

SELECT 
    m.source_system AS continent,
    d.diagnosis_code AS icd9_code,
    COUNT(*) AS diagnosis_frequency
FROM "Unified_Diagnoses" d
JOIN "Unified_Admissions" a ON d.global_admission_id = a.global_admission_id
JOIN "Map_Admissions" m ON a.global_admission_id = m.global_admission_id
WHERE d.primary_diagnosis = TRUE
GROUP BY m.source_system, d.diagnosis_code
ORDER BY diagnosis_frequency DESC
LIMIT 10;

-- 4. Average completed admission duration by continent.

SELECT 
    m.source_system AS continent,
    ROUND(AVG(EXTRACT(EPOCH FROM (a.discharge_date_time::timestamp - a.admission_date_time::timestamp)) / 86400), 2) AS avg_days_stayed
FROM "Unified_Admissions" a
JOIN "Map_Admissions" m ON a.global_admission_id = m.global_admission_id
WHERE a.discharge_date_time IS NOT NULL 
  AND a.discharge_date_time != ''
GROUP BY m.source_system;

-- 5. Evidence that duplicate source identifiers have been resolved correctly.

SELECT 
    source_system, 
    source_admission_id, 
    global_admission_id
FROM "Map_Admissions"
WHERE source_admission_id IN ('1', '2', '3') -- Looking for duplicates
ORDER BY source_admission_id, source_system;

-- 6. Integrity checks for orphaned records and invalid chronology.
-- Orphaned Admissions (Should be 0 rows):

SELECT a.global_admission_id 
FROM "Unified_Admissions" a
LEFT JOIN "Unified_Patients" p ON a.global_patient_id = p.global_patient_id
WHERE p.global_patient_id IS NULL;

-- 7. Invalid Chronology (Should be 0 rows):

SELECT global_admission_id 
FROM "Unified_Admissions"
WHERE discharge_date_time::timestamp < admission_date_time::timestamp;