-- 1. Insert a Test Patient (Using a high ID to avoid collisions)
INSERT INTO "Unified_Patients" (global_patient_id, first_name, last_name, dob, gender) 
VALUES (9999, 'John', 'Doe', '1980-01-01', 'Male');

-- 2. Insert an Admission
INSERT INTO "Unified_Admissions" (global_admission_id, global_patient_id, admission_date_time, discharge_date_time) 
VALUES (9999, 9999, '2026-05-01 08:00:00', '2026-05-05 12:00:00');

-- 3. Insert a Surgery on May 1st
INSERT INTO "Unified_Surgical_Procedures" (global_procedure_id, global_admission_id, procedure_name, procedure_date_time) 
VALUES (9999, 9999, 'Appendectomy', '2026-05-01 10:00:00');

-- 4. Insert a Radiology Exam on May 1st (Merged into Diagnostic Orders)
INSERT INTO "Unified_Diagnostic_Orders" (global_order_id, global_admission_id, exam_type, exam_date_time, request_date_time) 
VALUES (9999, 9999, 'X-Ray Chest', '2026-05-01 14:00:00', '2026-05-01 09:00:00');

-- 5. Insert Test Patient 2
INSERT INTO "Unified_Patients" (global_patient_id, first_name, last_name, dob, gender) 
VALUES (9998, 'Jane', 'Smith', '1975-05-05', 'Female');

-- 6. Insert an ER Admission
INSERT INTO "Unified_Admissions" (global_admission_id, global_patient_id, admission_date_time, admission_source) 
VALUES (9998, 9998, '2026-06-01 12:00:00', 'Emergency Room');

-- 7. Insert an ICU Stay that starts after the admission
INSERT INTO "Unified_ICU_Stays" (global_icu_id, global_admission_id, icu_unit, entry_date_time) 
VALUES (9998, 9998, 'MICU', '2026-06-01 15:00:00');


-- 8. Insert a Discharge Summary note with the word "recovery"
INSERT INTO "Unified_Clinical_Notes" (
    global_note_id, 
    global_admission_id, 
    note_format, 
    note_text, 
    creation_date
) VALUES (
    9999, 
    1, 
    'Discharge Summary', 
    'Patient was monitored closely and showed significant signs of recovery. Discharged in stable condition.', 
    '2026-05-10 10:00:00'
);

-- 9. Ensure we have a patient (we can reuse patient 9999 if you ran the earlier seed, but let's be safe)
INSERT INTO "Unified_Patients" (global_patient_id, first_name, last_name, dob, gender) 
VALUES (9997, 'Transfer', 'Tester', '1990-01-01', 'Female');

-- 10. Create an admission
INSERT INTO "Unified_Admissions" (global_admission_id, global_patient_id, admission_date_time) 
VALUES (9997, 9997, '2026-07-01 08:00:00');

-- 11. Insert ICU Stay 1 (MICU)
INSERT INTO "Unified_ICU_Stays" (global_icu_id, global_admission_id, icu_unit, entry_date_time, exit_date_time) 
VALUES (9997, 9997, 'MICU', '2026-07-01 10:00:00', '2026-07-02 10:00:00');

-- 12. Insert ICU Stay 2 (CCU) for the SAME admission
INSERT INTO "Unified_ICU_Stays" (global_icu_id, global_admission_id, icu_unit, entry_date_time, exit_date_time) 
VALUES (9996, 9997, 'CCU', '2026-07-02 10:00:00', '2026-07-05 10:00:00');

-- 13. Create a Test Patient
INSERT INTO "Unified_Patients" (global_patient_id, first_name, last_name, dob, gender) 
VALUES (9995, 'Multi', 'Diagnosis', '1985-01-01', 'Male');

-- 14. Create an Admission
INSERT INTO "Unified_Admissions" (global_admission_id, global_patient_id, admission_date_time) 
VALUES (9995, 9995, '2026-08-01 08:00:00');

-- 15. Insert Diagnosis 1 (e.g., Hypertension)
INSERT INTO "Unified_Diagnoses" (global_diagnosis_id, global_admission_id, diagnosis_code, primary_diagnosis) 
VALUES (9995, 9995, '401.9', TRUE);

-- 16. Insert Diagnosis 2 (e.g., Diabetes)
INSERT INTO "Unified_Diagnoses" (global_diagnosis_id, global_admission_id, diagnosis_code, primary_diagnosis) 
VALUES (9994, 9995, '250.00', FALSE);

-- 17. Insert Diagnosis 3 (e.g., High Cholesterol)
INSERT INTO "Unified_Diagnoses" (global_diagnosis_id, global_admission_id, diagnosis_code, primary_diagnosis) 
VALUES (9993, 9995, '272.0', FALSE);

-- 18 Let's use patient 9995 (Multi Diagnosis) that we created earlier
INSERT INTO "Unified_Clinical_Notes" (
    global_note_id, 
    global_admission_id, 
    note_format, 
    note_text, 
    creation_date
) VALUES (
    9992, 
    9995, 
    'Discharge Summary', 
    'Patient made a full recovery.', 
    '2026-08-05 10:00:00'
);

--19  add a SECOND note for the same patient, but with an OLDER date to prove DISTINCT ON works
INSERT INTO "Unified_Clinical_Notes" (
    global_note_id, 
    global_admission_id, 
    note_format, 
    note_text, 
    creation_date
) VALUES (
    9991, 
    9995, 
    'Progress Note', 
    'Patient is resting.', 
    '2026-08-02 10:00:00'
);

-- 20 . Create a Test Patient for Q19
INSERT INTO "Unified_Patients" (global_patient_id, first_name, last_name, dob, gender) 
VALUES (9994, 'Sad', 'Ending', '1940-01-01', 'Male');

-- 21. Create an Admission
INSERT INTO "Unified_Admissions" (global_admission_id, global_patient_id, admission_date_time) 
VALUES (9994, 9994, '2026-09-01 08:00:00');

-- 22. Add a Discharge Record with condition 'Deceased'
INSERT INTO "Unified_Discharge_Records" (global_discharge_id, global_admission_id, discharge_date_time, condition_at_discharge) 
VALUES (9994, 9994, '2026-09-10 14:00:00', 'Deceased');

-- 23. Add a Primary Diagnosis (so the LEFT JOIN has something to grab)
INSERT INTO "Unified_Diagnoses" (global_diagnosis_id, global_admission_id, diagnosis_code, primary_diagnosis) 
VALUES (9990, 9994, '410.9', TRUE);

-- 24 Add a primary diagnosis to Jane Smith's ICU admission
INSERT INTO "Unified_Diagnoses" (global_diagnosis_id, global_admission_id, diagnosis_code, primary_diagnosis) 
VALUES (9998, 9998, '410.9', TRUE);

-- 25. Create the patient
INSERT INTO "Unified_Patients" (global_patient_id, first_name, last_name, dob, gender) 
VALUES (9993, 'Long', 'Stayer', '1970-01-01', 'Male');

-- 26. Create an admission that lasts 1 year
INSERT INTO "Unified_Admissions" (global_admission_id, global_patient_id, admission_date_time, discharge_date_time) 
VALUES (9993, 9993, '2026-01-01 08:00:00', '2027-01-01 08:00:00');

-- 27. Add an older note
INSERT INTO "Unified_Clinical_Notes" (global_note_id, global_admission_id, note_text, creation_date) 
VALUES (9993, 9993, 'Initial assessment completed.', '2026-01-02 10:00:00');

-- 28. Add a newer note
INSERT INTO "Unified_Clinical_Notes" (global_note_id, global_admission_id, note_text, creation_date) 
VALUES (9992, 9993, 'Final discharge note.', '2026-12-31 10:00:00');

-- 29. Find all Admissions where the Patient Name is currently NULL
WITH MissingPatients AS (
    SELECT DISTINCT a.global_patient_id
    FROM "Unified_Admissions" a
    LEFT JOIN "Unified_Patients" p ON a.global_patient_id = p.global_patient_id
    WHERE p.first_name IS NULL
),
-- 30. Create fake names for them
NewPatients AS (
    SELECT 
        global_patient_id, 
        'Patient' AS first_name, 
        'ID_' || global_patient_id AS last_name,
        '1900-01-01' AS dob,
        'Unknown' AS gender
    FROM MissingPatients
)
-- 31. Insert them into the Patients table
INSERT INTO "Unified_Patients" (global_patient_id, first_name, last_name, dob, gender)
SELECT * FROM NewPatients;


-- 32 update note
UPDATE "Unified_Clinical_Notes"
SET note_text = 'Standard clinical note (content missing in source data).',
    note_format = 'General Note'
WHERE note_text IS NULL;