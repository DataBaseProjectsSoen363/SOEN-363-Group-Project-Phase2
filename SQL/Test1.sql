-- Test 1: Every admission belongs to an existing patient.

SELECT * FROM "Unified_Admissions" a
LEFT JOIN "Unified_Patients" p ON a.global_patient_id = p.global_patient_id
WHERE p.global_patient_id IS NULL;