-- Test 5: Examinations and procedures occur within the relevant admission period.

SELECT s.global_procedure_id, a.admission_date_time, s.procedure_date_time, a.discharge_date_time
FROM "Unified_Surgical_Procedures" s
JOIN "Unified_Admissions" a ON s.global_admission_id = a.global_admission_id
WHERE s.procedure_date_time::timestamp < a.admission_date_time::timestamp 
   OR (a.discharge_date_time IS NOT NULL AND s.procedure_date_time::timestamp > a.discharge_date_time::timestamp);