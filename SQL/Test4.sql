-- Test 4: Where both patient and admission identifiers are stored, they identify the same patient.

SELECT * FROM "Unified_Admissions" a
JOIN "Map_Admissions" m ON a.global_admission_id = m.global_admission_id
JOIN "Unified_Patients" p ON a.global_patient_id = p.global_patient_id
WHERE a.global_patient_id IS NULL;