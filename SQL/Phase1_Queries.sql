
-- Task 6: Writing the Queries

-- Instructions:
-- 1. Find the block assigned to your handle below.
-- 2. Run each query in pgAdmin to confirm it executes.
-- 3. Screenshot of the Data Output grid captured
-- 4. Screenshot pasted into the shared Word document
-- 5. Comment under the screenshot explaining what the query does
--    and what the result shows (2-4 sentences)
-- 6. Commit this file when done.

-- ---------------------------------------------------------------------
-- 1 - 4   |   @Zitkq
-- ---------------------------------------------------------------------
SELECT DISTINCT esi_priority FROM "Unified_Triage";
-- Q1: List the names and admission dates of all patients who were classified as high-priority
-- emergency patients during triage.
SELECT p.name, a.admission_date_time
FROM admission a
JOIN patient p ON a.patient_id = p.patient_id
JOIN triage_assessment t ON a.admission_id = t.admission_id
WHERE t.triage_priority_level = 'High-Priority Emergency';

-- New Query
SELECT 
    p.first_name || ' ' || p.last_name AS patient_name, 
    a.admission_date_time
FROM "Unified_Admissions" a
JOIN "Unified_Patients" p ON a.global_patient_id = p.global_patient_id
JOIN "Unified_Triage" t ON a.global_admission_id = t.global_admission_id
WHERE t.esi_priority = 'ESI-1';

-- Q2: Find all patients who had more than three hospital admissions. Display the
-- patient identifier, patient name, and total number of admissions.
SELECT p.patient_id, p.name, COUNT(a.admission_id) AS "Total_Admission"
FROM patient p
JOIN admission a ON a.patient_id = p.patient_id
GROUP BY p.patient_id, p.name
HAVING COUNT(a.admission_id) > 3;

-- New Query
SELECT 
    p.global_patient_id, 
    p.first_name || ' ' || p.last_name AS patient_name, 
    COUNT(a.global_admission_id) AS "Total_Admission"
FROM "Unified_Patients" p
JOIN "Unified_Admissions" a ON a.global_patient_id = p.global_patient_id
GROUP BY p.global_patient_id, p.first_name, p.last_name
HAVING COUNT(a.global_admission_id) > 3;


-- Q3: Retrieve the names, admission dates, and discharge dates of patients who were discharged
-- without undergoing any surgical procedure during the admission.
SELECT p.name, a.admission_date_time, d.discharge_date_time
FROM patient p
JOIN admission a ON p.patient_id = a.patient_id
JOIN discharge_record d ON a.admission_id = d.admission_id
WHERE NOT EXISTS(
	SELECT 1
	FROM surgical_procedure sp
	WHERE sp.admission_id = a.admission_id
)
ORDER BY p.name;

-- New Query
SELECT 
    p.first_name || ' ' || p.last_name AS patient_name, 
    a.admission_date_time, 
    d.discharge_date_time
FROM "Unified_Patients" p
JOIN "Unified_Admissions" a ON p.global_patient_id = a.global_patient_id
JOIN "Unified_Discharge_Records" d ON a.global_admission_id = d.global_admission_id
WHERE NOT EXISTS (
    SELECT 1 
    FROM "Unified_Surgical_Procedures" sp
    WHERE sp.global_admission_id = a.global_admission_id
)
ORDER BY patient_name;

-- Q4: List all patients who had both a radiology examination and a surgical procedure
-- during the same admission.
SELECT DISTINCT p.name
FROM patient p
JOIN admission a ON a.patient_id = p.patient_id
JOIN diagnostic_order d ON d.admission_id = a.admission_id
JOIN radiology_examination r ON r.order_id = d.order_id
JOIN surgical_procedure s ON s.admission_id = a.admission_id;

-- New Query
SELECT DISTINCT 
    p.first_name || ' ' || p.last_name AS patient_name
FROM "Unified_Patients" p
JOIN "Unified_Admissions" a ON p.global_patient_id = a.global_patient_id
JOIN "Unified_Diagnostic_Orders" d ON a.global_admission_id = d.global_admission_id
JOIN "Unified_Surgical_Procedures" s ON a.global_admission_id = s.global_admission_id;


-- ---------------------------------------------------------------------
-- 5 - 8   |   @JuanMa_487
-- ---------------------------------------------------------------------

-- Q5: Find all ICU or CCU unit stays that lasted more than seven days. Display the
-- patient name, unit type, unit entry time, unit exit time, and calculated length of stay.
SELECT
    p.name,
    i.unit_type,
    i.entry_date_time,
    i.exit_date_time,
    (i.exit_date_time - i.entry_date_time) AS length_of_stay
FROM icu_stay i
JOIN admission a ON i.admission_id = a.admission_id
JOIN patient p ON a.patient_id = p.patient_id
WHERE i.unit_type IN ('ICU', 'CCU')
  AND i.exit_date_time IS NOT NULL
  AND (i.exit_date_time - i.entry_date_time) > INTERVAL '7 days';

-- New Query
SELECT 
    p.first_name || ' ' || p.last_name AS patient_name,
    i.icu_unit,
    i.entry_date_time,
    i.exit_date_time,
    (i.exit_date_time::timestamp - i.entry_date_time::timestamp) AS length_of_stay
FROM "Unified_ICU_Stays" i
JOIN "Unified_Admissions" a ON i.global_admission_id = a.global_admission_id
JOIN "Unified_Patients" p ON a.global_patient_id = p.global_patient_id
WHERE i.icu_unit IN ('ICU', 'CCU')
  AND i.exit_date_time IS NOT NULL
  AND (i.exit_date_time::timestamp - i.entry_date_time::timestamp) > INTERVAL '7 days';

-- Q6: Count the total number of hospital admissions for each patient. Include patients
-- who have no recorded admissions.
SELECT
    p.patient_id,
    p.name,
    COUNT(a.admission_id) AS total_admissions
FROM patient p
LEFT JOIN admission a ON a.patient_id = p.patient_id
GROUP BY p.patient_id, p.name;

-- New Query
SELECT 
    p.global_patient_id AS patient_id,
    p.first_name || ' ' || p.last_name AS patient_name,
    COUNT(a.global_admission_id) AS total_admissions
FROM "Unified_Patients" p
LEFT JOIN "Unified_Admissions" a ON p.global_patient_id = a.global_patient_id
GROUP BY p.global_patient_id, p.first_name, p.last_name;

-- Q7: List all patients who entered the hospital through the Emergency Department and were
-- later transferred to an ICU or CCU during the same admission.
SELECT DISTINCT p.name
FROM patient p
JOIN admission a ON a.patient_id = p.patient_id
JOIN icu_stay i ON i.admission_id = a.admission_id
WHERE a.admission_source = 'Emergency Room'
  AND i.unit_type IN ('ICU', 'CCU')
  AND i.entry_date_time > a.admission_date_time;

-- New Query
SELECT DISTINCT admission_source FROM "Unified_Admissions";
SELECT DISTINCT icu_unit FROM "Unified_ICU_Stays";

SELECT DISTINCT 
    p.first_name || ' ' || p.last_name AS patient_name,
    a.admission_source,
    i.icu_unit
FROM "Unified_Patients" p
JOIN "Unified_Admissions" a ON p.global_patient_id = a.global_patient_id
JOIN "Unified_ICU_Stays" i ON a.global_admission_id = i.global_admission_id
WHERE a.admission_source = 'Emergency Room'
  AND (i.icu_unit LIKE '%ICU%' OR i.icu_unit LIKE '%CCU%');

-- Q8: Retrieve the most frequently assigned primary ICD-9 diagnosis among admissions
-- that included at least one ICU or CCU stay. Display the ICD-9 code, its official
-- description, and the number of times it was assigned.

-- New Query
SELECT 
    d.diagnosis_code AS icd9_code,
    COUNT(*) AS times_assigned
FROM "Unified_Diagnoses" d
JOIN "Unified_Admissions" a ON d.global_admission_id = a.global_admission_id
JOIN "Unified_ICU_Stays" i ON a.global_admission_id = i.global_admission_id
WHERE d.primary_diagnosis = TRUE 
  AND (i.icu_unit LIKE '%ICU%' OR i.icu_unit LIKE '%CCU%')
GROUP BY d.diagnosis_code
ORDER BY times_assigned DESC
LIMIT 10;


-- ---------------------------------------------------------------------
-- 9 - 12   |   @Mohammad
-- ---------------------------------------------------------------------

-- Q9: CCalculate the average length of stay for each critical care unit type, such as MICU,
-- SICU, ICU, and CCU. Display the unit type and its average length of stay.
SELECT
    unit_type,
    AVG(exit_date_time - entry_date_time) AS average_length_of_stay_days
FROM icu_stay
WHERE exit_date_time IS NOT NULL
GROUP BY unit_type
ORDER BY unit_type;

-- New Query
SELECT 
    icu_unit AS unit_type,
    ROUND(AVG(EXTRACT(EPOCH FROM (exit_date_time::timestamp - entry_date_time::timestamp)) / 86400), 2) AS average_length_of_stay_days
FROM "Unified_ICU_Stays"
WHERE exit_date_time IS NOT NULL AND exit_date_time != ''
GROUP BY icu_unit
ORDER BY icu_unit;


-- Q10: List patients who had a surgical procedure before entering
-- an ICU or CCU during the same admission.
SELECT
    p.name,
    sp.procedure_date_time,
    i.unit_type,
    i.entry_date_time
FROM patient p
JOIN admission a
    ON p.patient_id = a.patient_id
JOIN surgical_procedure sp
    ON a.admission_id = sp.admission_id
JOIN icu_stay i
    ON a.admission_id = i.admission_id
WHERE i.unit_type IN ('ICU', 'CCU')
  AND sp.procedure_date_time < i.entry_date_time
ORDER BY p.name;

-- New Query
SELECT 
    p.first_name || ' ' || p.last_name AS patient_name,
    sp.procedure_date_time,
    i.icu_unit AS unit_type,
    i.entry_date_time
FROM "Unified_Patients" p
JOIN "Unified_Admissions" a ON p.global_patient_id = a.global_patient_id
JOIN "Unified_Surgical_Procedures" sp ON a.global_admission_id = sp.global_admission_id
JOIN "Unified_ICU_Stays" i ON a.global_admission_id = i.global_admission_id
WHERE (i.icu_unit LIKE '%ICU%' OR i.icu_unit LIKE '%CCU%')
  AND sp.procedure_date_time::timestamp < i.entry_date_time::timestamp
ORDER BY patient_name;


-- Q11: Count the total number of radiology examinations for each patient,
-- including patients who have not received any examinations.
SELECT
    p.name,
    COUNT(re.examination_id) AS total_radiology_exams
FROM patient p
LEFT JOIN admission a
    ON p.patient_id = a.patient_id
LEFT JOIN diagnostic_order doo
    ON a.admission_id = doo.admission_id
LEFT JOIN radiology_examination re
    ON doo.order_id = re.order_id
GROUP BY p.patient_id, p.name
ORDER BY p.name;

-- New Query
SELECT DISTINCT note_format FROM "Unified_Clinical_Notes";

SELECT 
    p.first_name || ' ' || p.last_name AS patient_name,
    COUNT(d.global_order_id) AS total_radiology_exams
FROM "Unified_Patients" p
LEFT JOIN "Unified_Admissions" a 
    ON p.global_patient_id = a.global_patient_id
LEFT JOIN "Unified_Diagnostic_Orders" d 
    ON a.global_admission_id = d.global_admission_id
GROUP BY p.global_patient_id, p.first_name, p.last_name
ORDER BY patient_name;

-- Q12: Find patients whose discharge-summary clinical note
-- contains the keyword "recovery", case-insensitively.
SELECT DISTINCT
    p.name
FROM patient p
JOIN admission a
    ON p.patient_id = a.patient_id
JOIN clinical_note cn
    ON a.admission_id = cn.admission_id
WHERE cn.type = 'Discharge Summary'
  AND cn.contents ILIKE '%recovery%'
ORDER BY p.name;

-- New Query

SELECT 
    cn.note_format, 
    cn.note_text 
FROM "Unified_Clinical_Notes" cn
LIMIT 5;

SELECT DISTINCT
    p.first_name || ' ' || p.last_name AS patient_name
FROM "Unified_Patients" p
JOIN "Unified_Admissions" a 
    ON p.global_patient_id = a.global_patient_id
JOIN "Unified_Clinical_Notes" cn 
    ON a.global_admission_id = cn.global_admission_id
WHERE cn.note_format = 'Discharge Summary'
  AND cn.note_text ILIKE '%recovery%'
ORDER BY patient_name;

-- ---------------------------------------------------------------------
-- 13 - 16   |   @Laurent
-- ---------------------------------------------------------------------

-- Q13: List all admissions in which the patient had at least one radiology examination but
-- had no recorded ICU or CCU stay.
SELECT DISTINCT
  patient.name,
  admission.patient_id,
  admission.admission_id,
  radiology_examination.examination_id,
  icu_stay.unit_stay_id
FROM admission
-- LEFT JOINs to produce a table with all icu_stays + radiology_examinations according to admission
-- (Just JOIN would reject null columns but we want to keep to filter out later)
LEFT JOIN icu_stay ON admission.admission_id = icu_stay.admission_id
LEFT JOIN diagnostic_order ON admission.admission_id = diagnostic_order.admission_id
LEFT JOIN radiology_examination ON diagnostic_order.order_id = radiology_examination.order_id
LEFT JOIN patient ON admission.patient_id = patient.patient_id
-- Filter out admissions without radiology examinations and that has some icu_stay
WHERE icu_stay.admission_id IS NULL
  AND radiology_examination.examination_id IS NOT NULL
ORDER BY admission.patient_id;

-- New Query
SELECT DISTINCT
    p.first_name || ' ' || p.last_name AS patient_name,
    a.global_patient_id,
    a.global_admission_id,
    d.global_order_id AS radiology_exam_id,
    i.global_icu_id
FROM "Unified_Admissions" a
LEFT JOIN "Unified_ICU_Stays" i ON a.global_admission_id = i.global_admission_id
LEFT JOIN "Unified_Diagnostic_Orders" d ON a.global_admission_id = d.global_admission_id
LEFT JOIN "Unified_Patients" p ON a.global_patient_id = p.global_patient_id
WHERE i.global_admission_id IS NULL
  AND d.global_order_id IS NOT NULL
ORDER BY a.global_patient_id;

-- Q14: Retrieve the patient or patients with the longest completed hospital stay, calculated
-- from admission time to discharge time. If multiple patients have the same
-- maximum length of stay, display all of them.
SELECT
    patient.patient_id,
    patient.name,
    admission.admission_id,
    admission.admission_date_time,
    admission.discharge_date_time,
    (admission.discharge_date_time - admission.admission_date_time) AS length_of_stay
FROM admission
-- JOIN for admission + patient table
JOIN patient ON admission.patient_id = patient.patient_id
-- Filter for maximum length of stay
WHERE (admission.discharge_date_time - admission.admission_date_time) = (
    SELECT MAX(discharge_date_time - admission_date_time) FROM admission
);

-- New Query
SELECT
    p.global_patient_id,
    p.first_name || ' ' || p.last_name AS patient_name,
    a.global_admission_id,
    a.admission_date_time,
    a.discharge_date_time,
    (a.discharge_date_time::timestamp - a.admission_date_time::timestamp) AS length_of_stay
FROM "Unified_Admissions" a
JOIN "Unified_Patients" p ON a.global_patient_id = p.global_patient_id
WHERE (a.discharge_date_time::timestamp - a.admission_date_time::timestamp) = (
    SELECT MAX(discharge_date_time::timestamp - admission_date_time::timestamp) 
    FROM "Unified_Admissions"
    WHERE discharge_date_time IS NOT NULL AND discharge_date_time != ''
);

-- Q15: Count the total number of transfers between hospital units for each patient. The
-- patient’s first unit placement is not considered a transfer; each subsequent unit stay
-- within the same admission represents one transfer.
SELECT
  patient.name,
  admission.patient_id,
  icu_stay.admission_id,
  COUNT(*) - 1 AS total_transfers -- First transfer doesn't count
FROM icu_stay
-- JOIN for icu_stay + admission + patient table
JOIN admission ON icu_stay.admission_id = admission.admission_id
JOIN patient ON admission.patient_id = patient.patient_id
GROUP BY patient.name, admission.patient_id, icu_stay.admission_id;

-- New Query
SELECT
    p.first_name || ' ' || p.last_name AS patient_name,
    a.global_patient_id,
    a.global_admission_id,
    COUNT(*) - 1 AS total_transfers
FROM "Unified_ICU_Stays" i
JOIN "Unified_Admissions" a ON i.global_admission_id = a.global_admission_id
JOIN "Unified_Patients" p ON a.global_patient_id = p.global_patient_id
GROUP BY p.first_name, p.last_name, a.global_patient_id, a.global_admission_id
ORDER BY total_transfers DESC;


-- Q16: List all patients who stayed in more than one type of critical care unit during
-- the same admission. For example, a patient may have been transferred from an ICU
-- to a CCU.
SELECT
    patient.patient_id,
    patient.name,
    admission.admission_id,
    COUNT(DISTINCT icu_stay.unit_type) AS distinct_unit_types
FROM admission
-- JOIN of patient + admission + icu_stay to get a table
JOIN patient ON admission.patient_id = patient.patient_id
JOIN icu_stay ON admission.admission_id = icu_stay.admission_id
GROUP BY patient.patient_id, patient.name, admission.admission_id
-- Filter out with distinct unit types greater than 1
HAVING COUNT(DISTINCT icu_stay.unit_type) > 1;

-- New Query
SELECT
    p.global_patient_id,
    p.first_name || ' ' || p.last_name AS patient_name,
    a.global_admission_id,
    COUNT(DISTINCT i.icu_unit) AS distinct_unit_types
FROM "Unified_Admissions" a
JOIN "Unified_Patients" p ON a.global_patient_id = p.global_patient_id
JOIN "Unified_ICU_Stays" i ON a.global_admission_id = i.global_admission_id
GROUP BY p.global_patient_id, p.first_name, p.last_name, a.global_admission_id
HAVING COUNT(DISTINCT i.icu_unit) > 1
ORDER BY distinct_unit_types DESC;



-- ---------------------------------------------------------------------
-- 17 - 20   |   @fmvemba
-- ---------------------------------------------------------------------

-- Q17: Find all admissions during which the patient received more than one distinct ICD-
-- 9 diagnosis. Display the patient name, admission identifier, and number of distinct
-- ICD-9 codes.
SELECT p.name,
	   a.admission_id,
	   COUNT(DISTINCT d.icd9_code) AS num_distinct_diagnoses
FROM patient P
JOIN admission a ON p.patient_id = a.patient_id
JOIN diagnosis d ON a.admission_id = d.admission_id
GROUP BY p.name, a.admission_id
HAVING COUNT(DISTINCT d.icd9_code) > 1;

-- New Query
SELECT 
    p.first_name || ' ' || p.last_name AS patient_name,
    a.global_admission_id,
    COUNT(DISTINCT d.diagnosis_code) AS num_distinct_diagnoses
FROM "Unified_Patients" p
JOIN "Unified_Admissions" a ON p.global_patient_id = a.global_patient_id
JOIN "Unified_Diagnoses" d ON a.global_admission_id = d.global_admission_id
GROUP BY p.global_patient_id, p.first_name, p.last_name, a.global_admission_id
HAVING COUNT(DISTINCT d.diagnosis_code) > 1
ORDER BY num_distinct_diagnoses DESC;

	
-- Q18: Retrieve the latest clinical note for each patient.
SELECT DISTINCT ON (p.patient_id) 
       p.name, cn.contents, cn.creation_date, cn.patient_symptoms
FROM patient p
JOIN admission a ON a.patient_id = p.patient_id
JOIN clinical_note cn ON cn.admission_id = a.admission_id
ORDER BY p.patient_id, cn.creation_date DESC;

-- New Query
SELECT DISTINCT ON (p.global_patient_id)
    p.first_name || ' ' || p.last_name AS patient_name, 
    cn.note_text, 
    cn.creation_date
FROM "Unified_Patients" p
JOIN "Unified_Admissions" a ON a.global_patient_id = p.global_patient_id
JOIN "Unified_Clinical_Notes" cn ON cn.global_admission_id = a.global_admission_id
WHERE cn.creation_date IS NOT NULL AND cn.creation_date != ''
ORDER BY p.global_patient_id, cn.creation_date::timestamp DESC;

-- Q19: List all admissions where the patient’s discharge status or discharge condition indicates
-- that the patient died during the hospital stay. Display the patient name, admission
-- date, recorded date of death, and associated primary ICD-9 diagnosis.
SELECT
    p.name ,                                 
    a.admission_id,
    d.discharge_date_time,              
    dg.icd9_code                    
FROM admission a
JOIN patient           p  ON p.patient_id       = a.patient_id
JOIN discharge_record  d  ON d.admission_id     = a.admission_id
LEFT JOIN diagnosis    dg ON dg.admission_id    = a.admission_id
                          AND dg.primary_diagnosis = TRUE
WHERE d.condition_at_discharge = 'Deceased'
ORDER BY d.discharge_date_time;

-- New Query
SELECT
    p.first_name || ' ' || p.last_name AS patient_name,                                 
    a.global_admission_id,
    d.discharge_date_time,              
    dg.diagnosis_code                    
FROM "Unified_Admissions" a
JOIN "Unified_Patients" p ON p.global_patient_id = a.global_patient_id
JOIN "Unified_Discharge_Records" d ON d.global_admission_id = a.global_admission_id
LEFT JOIN "Unified_Diagnoses" dg ON dg.global_admission_id = a.global_admission_id
                          AND dg.primary_diagnosis = TRUE
WHERE d.condition_at_discharge = 'Deceased'
ORDER BY d.discharge_date_time;

-- Q20: Find all patients who underwent a surgical procedure and a radiology examination
-- on the same calendar day during the same admission. Display the patient
-- name, admission identifier, procedure type, radiology examination type, and the common
-- date.
SELECT
    p.name,
    a.admission_id,
    sp.procedure_id,
    re.examination_type,
    DATE(sp.procedure_date_time) AS common_date
FROM patient p
JOIN admission a ON a.patient_id = p.patient_id
JOIN surgical_procedure sp ON a.admission_id = sp.admission_id
JOIN diagnostic_order d ON d.admission_id = a.admission_id
JOIN radiology_examination re ON re.order_id = d.order_id
WHERE DATE(sp.procedure_date_time) = DATE(re.examination_date_time)
ORDER BY common_date, p.name;

-- New Query
SELECT
    p.first_name || ' ' || p.last_name AS patient_name,
    a.global_admission_id,
    sp.procedure_name AS procedure_type,
    d.exam_type AS radiology_examination_type,
    DATE(sp.procedure_date_time::timestamp) AS common_date
FROM "Unified_Patients" p
JOIN "Unified_Admissions" a ON a.global_patient_id = p.global_patient_id
JOIN "Unified_Surgical_Procedures" sp ON a.global_admission_id = sp.global_admission_id
JOIN "Unified_Diagnostic_Orders" d ON d.global_admission_id = a.global_admission_id
WHERE DATE(sp.procedure_date_time::timestamp) = DATE(d.exam_date_time::timestamp)
ORDER BY common_date, patient_name;










	



