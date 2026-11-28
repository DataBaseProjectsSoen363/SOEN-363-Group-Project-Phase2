-- Test 2: Discharge times occur after admission times.
-- Because we loaded dates as strings, we have to cast them to timestamps in PostgreSQL to compare them).

SELECT * FROM "Unified_Admissions"
WHERE discharge_date_time IS NOT NULL 
AND discharge_date_time::timestamp < admission_date_time::timestamp;