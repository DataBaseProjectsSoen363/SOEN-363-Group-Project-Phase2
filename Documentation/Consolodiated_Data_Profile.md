# Consolidated Data Profile — All Sources (A, B, C, D)

> Single-file reference combining every profile provided. Grouped by domain; each domain has a per-source table plus notes. A cross-source row-count matrix and a data-quality flag list appear at the end.

---

## 0. Source Inventory

| Source | Files profiled | Domains covered |
|---|---|---|
| A | admission, admissions, clinical_notes, diagnoses, diagnosis, diagnostic_orders, discharge_records, icd9_dict, icd9, icu_stays, patient, patients, professionals, radiology_examinations, radiology_reports, surgical_procedures, triage_assessments | All |
| B | Admission, Clinical_Note, Diagnosis, Diagnostic_Order, Discharge_Record, ICU_Stay, Patient, Radiology, Surgical_Procedure, Triage | All except professionals/dict |
| C | Admission, Diagnosis, Patient, Triage | Admissions, Diagnoses, Patients, Triage only |
| D | admissions, discharge, icu, notes, orders, patients, surgery, triage | All except professionals/dict |

---

## 1. PATIENTS

| Attribute | A (`SourceA_patient(s)_profile`) | B (`SourceB_Patient_profile`) | C (`SourceC_Patient_profile`) | D (`SourceD_patients_profile`) |
|---|---|---|---|---|
| Records | 800 | 800 | 800 | 800 |
| Shape | (800, 9) | (800, 7) | (800, 7) | (800, 5) |
| Fields | patient_id, name, health_insurance_number, life_status, address, date_birth, gender, emergency_contact_number, phone_number | mrn, full_name, insurance_id, dob, gender_cd, contact_phone, home_address | id, FirstName, LastName, Address, DateOfBirth, Gender, Phone | patientId, name, dobTimestamp, gender, contact |
| Missing | gender 1; emergency_contact_number 19; phone_number 19 | contact_phone 39 | Phone 47 | 0 |
| Hidden `N/A` | 0 (variant exists) | 0 | 0 | 0 |
| Duplicates | 0 | 0 | 0 | 0 |
| Notes | gender incl. Male/Female; address mixed case | mrn 795 unique / 800 rows (2 dupes) | Address = `"\n"` for all 800; names from 8 first/7 last; DOB has time | name/contact are dicts; dobTimestamp has negative (pre-1970) values; gender M/F |

---

## 2. ADMISSIONS

| Attribute | A (`SourceA_admission(s)_profile`) | B (`SourceB_Admission_profile`) | C (`SourceC_Admission_profile`) | D (`SourceD_admissions_profile`) |
|---|---|---|---|---|
| Records | 1200 | 1200 | 1200 | 1200 |
| Shape | (1200, 10) | (1200, 7) | (1200, 8) | (1200, 8) |
| Fields | admission_id, patient_id, admission_date_time, discharge_date_time, admission_type, admission_source, reason_admission, insurance_information, current_condition, admitting_professional_id | visit_id, patient_mrn, admitting_doctor, admit_date, discharge_date, ward_code, reason_text | id, patient_ref, AdmissionDate, DischargeDate, AdmissionType, Reason, DoctorId, Diagnoses | visitId, patientId, admitTimestamp, admissionType, reason, doctorId, dischargeTimestamp, diagnoses |
| Missing | discharge_date_time 24; insurance_information 303 | 0 | DischargeDate 26; Diagnoses 107 | dischargeTimestamp 44; diagnoses 138 |
| Hidden `N/A` | 0 (variant exists) | 0 | 0 | 0 |
| Duplicates | 0 | 0 | 0 | 0 |
| Notes | admission_id = row+1; patient_id max 844 | patient_mrn 617 unique; ward_code 5 vals; reason_text 8 vals (French, mixed case) | Diagnoses = `"\n"` (empty) for 1093 rows; DischargeDate has `2026-02-31`; patient_ref max 9999 | Timestamps are Unix ints; diagnoses is JSON array; patientId max 9999 |

---

## 3. TRIAGE

| Attribute | A (`SourceA_triage_assessments_profile`) | B (`SourceB_Triage_profile`) | C (`SourceC_Triage_profile`) | D (`SourceD_triage_profile`) |
|---|---|---|---|---|
| Records | 1200 | 1175 | 1200 | 1200 |
| Shape | (1200, 13) | (1175, 10) | (1200, 6) | (1200, 6) |
| Fields | triage_id, admission_id, nurse_id, blood_pressure, heart_rate, respiratory_rate, body_temperature, oxygen_saturation, pain_level, reported_symptoms, known_allergies, current_medications, triage_priority_level | triage_id, visit_id, nurse_mrn, bp_systolic, bp_diastolic, hr_bpm, temp_fahrenheit, o2_sat, esi_priority, allergy_note | id, admission_ref, NurseId, HeartRate, OxygenSaturation, Priority | triageId, visitId, nurseId, vitals, symptoms, triagePriority |
| Missing | nurse_id 28; known_allergies 240; current_medications 197 | allergy_note 211 | 0 | nurseId 24 |
| Hidden `N/A` | 0 (variant exists) | 0 | 0 | 0 |
| Duplicates | 0 | 0 | 0 | 0 |
| Notes | BP as string "121/82"; HR min −99; O2 min 0; temp max 45.2; 15 priority vals | temp °F (97–113); HR min −99; 5 ESI vals; allergy_note incl. "UNK" | O2 92–100; HR min −99; 5 ESI vals | vitals dict; symptoms list; nurseId 1176 unique |

---

## 4. CLINICAL NOTES

| Attribute | A (`SourceA_clinical_notes_profile`) | B (`SourceB_Clinical_Note_profile`) | C | D (`SourceD_notes_profile`) |
|---|---|---|---|---|
| Records | 1113 | 1053 | — | 1072 |
| Shape | (1113, 11) | (1053, 6) | — | (1072, 5) |
| Fields | note_id, admission_id, physician_id, type, creation_date, patient_symptoms, physical_examination, initial_clinical_findings, suspected_condition, planned_diagnostic_examinations, initial_treatment | note_id, visit_id, author_mrn, note_format, created_datetime, note_text | — | noteId, visitId, authorId, noteTimestamp, noteText |
| Missing | initial_clinical_findings 30; initial_treatment 34 | note_text 29 | — | noteText 27 |
| Hidden `N/A` | 0 | 0 | — | 0 |
| Duplicates | 0 | 0 | — | 0 |
| Notes | Structured SOAP fields; 12 note types; 4–5 vals each | note_text single template (1024 unique=1); 3 formats (SOAP/Narrative/…) | — | noteText single template; Unix timestamp; authorId 1–15 |

---

## 5. DIAGNOSES

| Attribute | A (`SourceA_diagnosis(es)_profile`) | B (`SourceB_Diagnosis_profile`) | C (`SourceC_Diagnosis_profile`) | D |
|---|---|---|---|---|
| Records | 2119 | 2133 | 2195 | — (embedded in admissions `diagnoses`) |
| Shape | (2119, 8) | (2133, 6) | (2195, 4) | — |
| Fields | diagnosis_id, patient_id, admission_id, icd9_code, diagnosis_date_time, primary_diagnosis, secondary_diagnosis, diagnosing_physician_id | diag_id, visit_id, icd9_code, diag_datetime, is_primary, attending_doctor | ICD9Code, Date, IsPrimary, DoctorId | — |
| Missing | 0 | 0 | Date 50 | — |
| Hidden `N/A` | 0 | 0 | 0 | — |
| Duplicates | 0 | 0 | **11** | — |
| Notes | admission_id max 9999; icd9 max 410.9; bool primary/secondary | is_primary "Yes"/"No" | bool IsPrimary; Date missing; 11 dup rows | JSON list inside admission row |

---

## 6. DIAGNOSTIC ORDERS / RADIOLOGY

| Attribute | A (orders + radiology_examinations + radiology_reports) | B (Diagnostic_Order + Radiology) | C | D (orders w/ embedded radiologyExam) |
|---|---|---|---|---|
| Orders records | 275 | 307 | — | 299 |
| Orders shape | (275, 9) | (307, 7) | — | (299, 6) |
| Radiology records | 275 exams; 260 reports | 301 exams | — | 299 embedded |
| Order fields | order_id, admission_id, patient_id, requesting_physician_id, requested_examination, request_date_time, clinical_reason_examination, priority, order_status | order_id, visit_id, doctor_mrn, exam_type, order_datetime, priority_level (int), order_status | — | orderId, visitId, doctorId, examType, orderTimestamp, radiologyExam |
| Order missing | order_status 4 | order_status 12 | — | 0 |
| Radiology missing | body_area 11; medical_images 9; interpretation 9 | findings_text 16; radiologist_conclusion 16 | — | — |
| Duplicates | 0 | 0 | — | 0 |
| Notes | 4 exam types; priority STAT/Urgent/Routine; status Completed/Pending | priority_level 1–4; status incl. Cancelled/COMPLETED/Completed | — | 3 exam types; radiologyExam JSON (findings/conclusion) |

---

## 7. DISCHARGE RECORDS

| Attribute | A (`SourceA_discharge_records_profile`) | B (`SourceB_Discharge_Record_profile`) | C | D (`SourceD_discharge_profile`) |
|---|---|---|---|---|
| Records | 1176 | 1148 | — | 1121 |
| Shape | (1176, 9) | (1148, 6) | — | (1121, 5) |
| Fields | discharge_record_id, admission_id, discharge_date_time, discharge_destination, condition_at_discharge, discharge_status, followup_instructions, followup_appointments, responsible_physician | discharge_id, visit_id, discharge_datetime, disposition_code, followup_date, discharging_doctor_mrn | — | dischargeId, visitId, dischargeTimestamp, destination, condition |
| Missing | followup_appointments 119 | followup_date 369 | — | 0 |
| Hidden `N/A` | 0 | 0 | — | 0 |
| Duplicates | 0 | 0 | — | 0 |
| Notes | 17 destination vals (mixed case e.g. "LONG-TERM CARE"); 2 status vals; followup_instructions single template | 4 disposition codes (HOME/SNF/REHAB/…); followup missing 1/3 | — | 3 destinations; 3 conditions; Unix timestamp |

---

## 8. ICU STAYS

| Attribute | A (`SourceA_icu_stays_profile`) | B (`SourceB_ICU_Stay_profile`) | C | D (`SourceD_icu_profile`) |
|---|---|---|---|---|
| Records | 355 | 360 | — | 351 |
| Shape | (355, 9) | (360, 8) | — | (351, 6) |
| Fields | unit_stay_id, admission_id, responsible_physician_id, unit_type, room_number, bed_number, entry_date_time, exit_date_time, reason_transfer | stay_id, visit_id, doctor_mrn, ward_type, ventilator_used, in_date, out_date, transfer_reason | — | stayId, visitId, wardType, doctorId, entryTimestamp, exitTimestamp |
| Missing | exit_date_time 11 | out_date 18 | — | exitTimestamp 17 |
| Hidden `N/A` | 0 | 0 | — | 0 |
| Duplicates | 0 | 0 | — | 0 |
| Notes | unit_type 11 vals (ICU/MICU/SICU/CCU…); room/bed strings | ward_type 3 vals; ventilator Y/N; transfer_reason 6 (French) | — | wardType 4 vals; Unix timestamps |

---

## 9. SURGICAL PROCEDURES

| Attribute | A (`SourceA_surgical_procedures_profile`) | B (`SourceB_Surgical_Procedure_profile`) | C | D (`SourceD_surgery_profile`) |
|---|---|---|---|---|
| Records | 247 | 237 | — | 251 |
| Shape | (247, 7) | (237, 6) | — | (251, 5) |
| Fields | procedure_id, admission_id, patient_id, procedure_name, body_site, procedure_date_time, surgeon_id | surgery_id, visit_id, surgeon_mrn, proc_code, proc_name, surgery_datetime | — | surgeryId, visitId, procedureCode, surgeonId, surgeryTimestamp |
| Missing | 0 | surgery_datetime 5 | — | 0 |
| Hidden `N/A` | 0 | 0 | — | 0 |
| Duplicates | 0 | 0 | — | 0 |
| Notes | procedure_name 14 vals (mixed case "knee replacement"/"Knee Replacement"); body_site 5 | proc_code 5; proc_name 5 | — | procedureCode 3 vals; Unix timestamp |

---

## 10. PROFESSIONALS / PROVIDERS

| Attribute | A (`SourceA_professionals_profile`) | B | C | D |
|---|---|---|---|---|
| Records | 25 | — (embedded as MRNs) | — | — (embedded as IDs) |
| Shape | (25, 5) | — | — | — |
| Fields | professional_id, full_name, role, specialty, license_number | — | — | — |
| Missing | specialty 13 | — | — | — |
| Hidden `N/A` | 0 | — | — | — |
| Duplicates | 0 rows (but 23 unique names / 25 → 2 dup names) | — | — | — |
| Notes | role 5 vals incl. "physician" vs "Physician"; specialty 5 vals | — | — | — |

---

## 11. ICD-9 DICTIONARY (Source A only)

| Attribute | A (`SourceA_icd9_dict_profile` / `SourceA_icd9_profile`) |
|---|---|
| Records | 20 |
| Shape | (20, 4) |
| Fields | icd9_code, official_diagnosis_title, description, disease_category |
| Missing | 0 |
| Duplicates | 0 |
| Notes | Two profile files, same shape, different samples; 8 disease categories; codes are strings here but floats in diagnosis tables |

---

## 12. CROSS-SOURCE ROW-COUNT MATRIX

| Domain | A | B | C | D |
|---|---|---|---|---|
| Patients | 800 | 800 | 800 | 800 |
| Admissions | 1200 | 1200 | 1200 | 1200 |
| Triage | 1200 | 1175 | 1200 | 1200 |
| Clinical Notes | 1113 | 1053 | — | 1072 |
| Diagnoses | 2119 | 2133 | 2195 | — (embedded) |
| Diagnostic Orders | 275 | 307 | — | 299 |
| Radiology Exams / Reports | 275 / 260 | 301 | — | 299 (embedded) |
| Discharge Records | 1176 | 1148 | — | 1121 |
| ICU Stays | 355 | 360 | — | 351 |
| Surgical Procedures | 247 | 237 | — | 251 |
| Professionals | 25 | — | — | — |
| ICD-9 Dict | 20 | — | — | — |

---

## 13. KEY DATA-QUALITY FLAGS ACROSS SOURCES

- **Impossible dates**: Source C DischargeDate has `2026-02-31`; all sources use 2026 dates.
- **Negative / implausible vitals**: HR min −99 (A, B, C); O2 min 0 (A); O2 92 (C); O2 95 (B).
- **Placeholder / empty strings**: C Address = `"\n"` for all 800; C Diagnoses = `"\n"` for 1093; B note_text single template (1024/1025 identical).
- **Hidden missing**: `N/A` strings appear only in Source A hidden-missing variants (0 counts reported, variants exist).
- **ID inconsistency**: A admissions patient_id max 844 vs 800 patients; admission_id/patient_id max 9999 in A, B, D.
- **Duplicates**: C Diagnosis 11 dup rows; A professionals 2 dup names; B patients 2 dup MRNs.
- **Mixed case / format**: French vs English reasons (B, D); destination casing (A); procedure_name casing (A); role "physician"/"Physician" (A).
- **Nested / JSON fields**: D uses dicts/lists (name, contact, vitals, symptoms, diagnoses, radiologyExam); A/B/C flat columns.

---

*End of consolidated profile. Total domains: 11. Total profiled tables: ~40 across 4 sources.*