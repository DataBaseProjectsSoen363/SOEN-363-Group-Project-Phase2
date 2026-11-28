
-- check validity of database

SELECT table_name
FROM information_schema.TABLES
WHERE table_schema = 'public';


SELECT ua.global_admission_id, up.full_name, ua.admission_type 
FROM "Unified_Admissions" ua
JOIN "Unified_Patients" up ON ua.global_patient_id = up.global_patient_id
LIMIT 5;