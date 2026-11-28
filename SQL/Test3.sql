-- Test 3: Unit exit times occur after unit entry times.

SELECT * FROM "Unified_ICU_Stays"
WHERE exit_date_time IS NOT NULL 
AND exit_date_time::timestamp < entry_date_time::timestamp;