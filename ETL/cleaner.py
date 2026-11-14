import pandas as pd
import os

# SOURCE A CLEANING FUNCTIONS

def clean_SourceA_patients(df):
    print("Cleaning Source A Patients...")
    os.makedirs("../Cleaned_Data", exist_ok=True)
    os.makedirs("../Quarantine", exist_ok=True)

    # RULE 3 & 5: Text standardizing
    df['name'] = df['name'].str.strip().str.title()
    df['address'] = df['address'].str.strip()
    df['gender'] = df['gender'].str.strip().str.title()
    df['gender'] = df['gender'].replace({'M': 'Male', 'F': 'Female'})
    
    # RULE 1: Missing values
    df['phone_number'] = df['phone_number'].fillna('Unknown')
    
    # RULE 4: Dates
    df['date_birth'] = pd.to_datetime(df['date_birth'], errors='coerce')
    
    # RULE 8: Chronology (Impossible Future Birthdates)
    future_dates = df[df['date_birth'] > pd.Timestamp.now()].copy()
    future_dates['rejection_reason'] = "Birthdate in the future"
    future_dates.to_csv("../Quarantine/SourceA_future_birthdates.csv", index=False)
    
    # Drop the future dates from the main dataframe
    df = df[df['date_birth'] <= pd.Timestamp.now()]
    
    df.to_csv("../Cleaned_Data/SourceA_patients_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean patients. Quarantined {len(future_dates)} future dates.")

def clean_SourceA_admissions(df_admission):
    print("Cleaning Source A Admissions...")
    
    # RULE 4: Dates
    df_admission['admission_date_time'] = pd.to_datetime(df_admission['admission_date_time'], errors='coerce')
    df_admission['discharge_date_time'] = pd.to_datetime(df_admission['discharge_date_time'], errors='coerce')

    # RULE 7: Quarantine broken patient foreign keys
    bad_fks = df_admission[df_admission['patient_id'] > 800].copy()
    bad_fks['rejection_reason'] = "Broken patient Foreign Key"
    bad_fks.to_csv("../Quarantine/SourceA_bad_fks.csv", index=False)
    df_admission = df_admission[df_admission['patient_id'] <= 800]
    
    # RULE 8: Chronology (Discharge before Admission)
    bad_chrono = df_admission[df_admission['discharge_date_time'] < df_admission['admission_date_time']].copy()
    bad_chrono['rejection_reason'] = "Discharge date before admission date"
    bad_chrono.to_csv("../Quarantine/SourceA_bad_chronology.csv", index=False)
    
    # Keep only good rows
    df_admission = df_admission[~(df_admission['discharge_date_time'] < df_admission['admission_date_time'])]
    
    # RULE 3: Text standardizing
    df_admission['admission_type'] = df_admission['admission_type'].str.strip().str.title()
    df_admission['reason_admission'] = df_admission['reason_admission'].str.strip()
    
    df_admission.to_csv("../Cleaned_Data/SourceA_admissions_clean.csv", index=False)
    print(f" -> Saved {len(df_admission)} clean admissions. Quarantined {len(bad_chrono)} bad dates.")

def clean_SourceA_triage(df_triage):
    print("Cleaning Source A Triage...")
    
    # RULE 5: Numeric / Out of bounds vitals
    bad_vitals = df_triage[(df_triage['heart_rate'] < 0) | (df_triage['body_temperature'] > 45) | (df_triage['oxygen_saturation'] < 50)].copy()
    bad_vitals['rejection_reason'] = "Out of bounds vitals"
    bad_vitals.to_csv("../Quarantine/SourceA_bad_vitals.csv", index=False)
    
    df_triage = df_triage[(df_triage['heart_rate'] >= 0) & (df_triage['body_temperature'] <= 45) & (df_triage['oxygen_saturation'] >= 50)]
    
    # RULE 5: Fix "5/10" data type anomaly
    df_triage['pain_level'] = df_triage['pain_level'].astype(str).str.split('/').str[0]
    df_triage['pain_level'] = pd.to_numeric(df_triage['pain_level'], errors='coerce')
    
    df_triage.to_csv("../Cleaned_Data/SourceA_triage_clean.csv", index=False)
    print(f" -> Saved {len(df_triage)} clean triage records. Quarantined {len(bad_vitals)} bad vitals.")


def clean_SourceA_clinical_notes(df):
    print("Cleaning Source A Clinical Notes...")
    
    # RULE 4: Dates
    df['creation_date'] = pd.to_datetime(df['creation_date'], errors='coerce')
    
    # RULE 1: Missing text -> Quarantine
    bad_notes = df[df['patient_symptoms'].astype(str).str.contains("ERROR - STRING TRUNCATED", na=False)].copy()
    bad_notes['rejection_reason'] = "Truncated note text"
    bad_notes.to_csv("../Quarantine/SourceA_bad_notes.csv", index=False)
    df = df[~df['patient_symptoms'].astype(str).str.contains("ERROR - STRING TRUNCATED", na=False)]
    
    # RULE 3: Text Standardization
    df['type'] = df['type'].str.strip().str.title()
    
    # RULE 2: Duplicates
    df = df.drop_duplicates(subset=['note_id'])
    
    df.to_csv("../Cleaned_Data/SourceA_clinical_notes_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean clinical notes. Quarantined {len(bad_notes)} truncated notes.")

def clean_SourceA_diagnoses(df):
    print("Cleaning Source A Diagnoses...")
    
    # RULE 4: Dates
    df['diagnosis_date_time'] = pd.to_datetime(df['diagnosis_date_time'], errors='coerce')
    
    # RULE 6: Standardize booleans (TRUE, true, True -> True; FALSE, false -> False)
    df['primary_diagnosis'] = df['primary_diagnosis'].astype(str).str.strip().str.lower().map({'true': True, 'false': False})
    df['secondary_diagnosis'] = df['secondary_diagnosis'].astype(str).str.strip().str.lower().map({'true': True, 'false': False})
    
    # RULE 2: Duplicates
    df = df.drop_duplicates(subset=['diagnosis_id'])
    
    df.to_csv("../Cleaned_Data/SourceA_diagnoses_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean diagnoses.")

def clean_SourceA_diagnostic_orders(df):
    print("Cleaning Source A Diagnostic Orders...")
    
    # RULE 4: Dates
    df['request_date_time'] = pd.to_datetime(df['request_date_time'], errors='coerce')
    
    # RULE 3 & 6: Standardization
    df['priority'] = df['priority'].str.strip().str.title()
    df['order_status'] = df['order_status'].str.strip().str.title()
    df['order_status'] = df['order_status'].replace('', 'Unknown') # If empty string
    
    # RULE 2: Duplicates
    df = df.drop_duplicates(subset=['order_id'])
    
    df.to_csv("../Cleaned_Data/SourceA_diagnostic_orders_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean diagnostic orders.")

def clean_SourceA_discharge_records(df):
    print("Cleaning Source A Discharge Records...")
    
    # RULE 4: Dates
    df['discharge_date_time'] = pd.to_datetime(df['discharge_date_time'], errors='coerce')
    if 'followup_appointments' in df.columns:
        df['followup_appointments'] = pd.to_datetime(df['followup_appointments'], errors='coerce')
    
    # RULE 3: Text Standardization
    df['discharge_destination'] = df['discharge_destination'].str.strip().str.title()
    df['condition_at_discharge'] = df['condition_at_discharge'].str.strip().str.title()
    df['discharge_status'] = df['discharge_status'].str.strip().str.title()
    
    # RULE 2: Duplicates
    df = df.drop_duplicates(subset=['discharge_record_id'])
    
    df.to_csv("../Cleaned_Data/SourceA_discharge_records_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean discharge records.")

def clean_SourceA_icu_stays(df):
    print("Cleaning Source A ICU Stays...")
    
    # RULE 4: Dates
    df['entry_date_time'] = pd.to_datetime(df['entry_date_time'], errors='coerce')
    df['exit_date_time'] = pd.to_datetime(df['exit_date_time'], errors='coerce')
    
    # RULE 8: Chronology (Exit before Entry)
    bad_chrono = df[df['exit_date_time'] < df['entry_date_time']].copy()
    bad_chrono['rejection_reason'] = "Exit date before entry date"
    bad_chrono.to_csv("../Quarantine/SourceA_bad_icu_chrono.csv", index=False)
    df = df[~(df['exit_date_time'] < df['entry_date_time'])]
    
    # RULE 3: Text
    df['unit_type'] = df['unit_type'].str.strip().str.upper()
    df['reason_transfer'] = df['reason_transfer'].str.strip().str.title()
    
    # RULE 2: Duplicates
    df = df.drop_duplicates(subset=['unit_stay_id'])
    
    df.to_csv("../Cleaned_Data/SourceA_icu_stays_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean ICU stays. Quarantined {len(bad_chrono)} bad dates.")

def clean_SourceA_professionals(df):
    print("Cleaning Source A Professionals...")
    
    # RULE 3: Standardize text
    df['role'] = df['role'].str.strip().str.title()
    # Fix " Physician " -> "Physician"
    df['role'] = df['role'].replace({'Physician': 'Physician'}) 
    
    df['specialty'] = df['specialty'].str.strip().str.title()
    df['specialty'] = df['specialty'].fillna('General') # Missing specialty
    
    # RULE 2: Duplicates
    df = df.drop_duplicates(subset=['professional_id'])
    
    df.to_csv("../Cleaned_Data/SourceA_professionals_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean professionals.")

def clean_SourceA_radiology_examinations(df):
    print("Cleaning Source A Radiology Examinations...")
    
    # RULE 4: Dates
    df['examination_date_time'] = pd.to_datetime(df['examination_date_time'], errors='coerce')
    
    # RULE 3 & 6: Standardize
    df['examination_status'] = df['examination_status'].str.strip().str.title()
    df['body_area_examined'] = df['body_area_examined'].str.strip().str.title()
    
    # RULE 2: Duplicates
    df = df.drop_duplicates(subset=['examination_id'])
    
    df.to_csv("../Cleaned_Data/SourceA_radiology_examinations_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean radiology exams.")

def clean_SourceA_radiology_reports(df):
    print("Cleaning Source A Radiology Reports...")
    
    # RULE 3: Text Standardization
    df['radiologist_findings'] = df['radiologist_findings'].str.strip()
    df['interpretation'] = df['interpretation'].str.strip()
    df['clinical_conclusion'] = df['clinical_conclusion'].str.strip()
    
    # RULE 2: Duplicates
    df = df.drop_duplicates(subset=['radiology_report_id'])
    
    df.to_csv("../Cleaned_Data/SourceA_radiology_reports_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean radiology reports.")

def clean_SourceA_surgical_procedures(df):
    print("Cleaning Source A Surgical Procedures...")
    
    # RULE 4: Dates
    df['procedure_date_time'] = pd.to_datetime(df['procedure_date_time'], errors='coerce')
    
    # RULE 3: Text Standardization
    df['procedure_name'] = df['procedure_name'].str.strip().str.title()
    df['body_site'] = df['body_site'].str.strip().str.title()
    
    # RULE 2: Duplicates
    df = df.drop_duplicates(subset=['procedure_id'])
    
    df.to_csv("../Cleaned_Data/SourceA_surgical_procedures_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean surgical procedures.")



# SOURCE B CLEANING FUNCTIONS

def clean_SourceB_patients(df):
    print("Cleaning Source B Patients...")
    
    # RULE 1: Missing values (Replace 'N/A' string with actual NaN)
    df = df.replace("N/A", pd.NA)
    df['contact_phone'] = df['contact_phone'].fillna('Unknown')
    
    # RULE 3: Text Standardization
    df['full_name'] = df['full_name'].str.strip().str.title()
    df['home_address'] = df['home_address'].str.strip()
    
    # RULE 4: Dates (European format DD/MM/YYYY)
    df['dob'] = pd.to_datetime(df['dob'], format='%d/%m/%Y', errors='coerce')
    
    # RULE 6: Clinical Categories (Map M/F to Male/Female to match Phase 1)
    df['gender_cd'] = df['gender_cd'].replace({'M': 'Male', 'F': 'Female'})
    
    # Save to clean folder with a Source B specific name
    df.to_csv("../Cleaned_Data/SourceB_patients_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean Source B patients.")


def clean_SourceB_admissions(df):
    print("Cleaning Source B Admissions...")
    
    # RULE 4: Dates (European format)
    df['admit_date'] = pd.to_datetime(df['admit_date'], format='%d/%m/%Y %H:%M', errors='coerce')
    df['discharge_date'] = pd.to_datetime(df['discharge_date'], format='%d/%m/%Y %H:%M', errors='coerce')
    
    # RULE 8: Chronology (Quarantine Discharge before Admit)
    bad_chrono = df[df['discharge_date'] < df['admit_date']].copy()
    bad_chrono['rejection_reason'] = "Discharge date before admission date"
    bad_chrono.to_csv("../Quarantine/SourceB_bad_chronology.csv", index=False)
    
    df = df[~(df['discharge_date'] < df['admit_date'])]
    # Drop rows where the admit_date is NaT (e.g., impossible dates like 31/02)
    df = df.dropna(subset=['admit_date']) 

    # RULE 6: Clinical categories (Map EMER -> Emergency)
    df['ward_code'] = df['ward_code'].str.strip().str.upper()
    mapping = {"EMER": "Emergency", "SURG": "Surgery", "MED": "Medical", "PEDS": "Pediatrics", "OBS": "Observation"}
    df['ward_code'] = df['ward_code'].replace(mapping)
    
    # RULE 3: Text standardizing
    df['reason_text'] = df['reason_text'].str.strip().str.title()

    # RULE 7: Quarantine broken patient foreign keys (The fix from earlier)
    bad_fks = df[df['patient_mrn'] == 'MRN-99999'].copy()
    bad_fks['rejection_reason'] = "Broken patient Foreign Key"
    bad_fks.to_csv("../Quarantine/SourceB_bad_fks.csv", index=False)
    df = df[df['patient_mrn'] != 'MRN-99999']
    
    df.to_csv("../Cleaned_Data/SourceB_admissions_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean Source B admissions. Quarantined {len(bad_chrono)} bad dates.")


def clean_SourceB_triage(df):
    print("Cleaning Source B Triage...")
    
    # RULE 5: Numeric / Out of bounds vitals
    # Source B uses Fahrenheit (normal body temp is around 98.6F)
    bad_vitals = df[(df['hr_bpm'] < 0) | (df['temp_fahrenheit'] > 110) | (df['o2_sat'] < 50)].copy()
    bad_vitals['rejection_reason'] = "Out of bounds vitals"
    bad_vitals.to_csv("../Quarantine/SourceB_bad_vitals.csv", index=False)
    
    df = df[(df['hr_bpm'] >= 0) & (df['temp_fahrenheit'] <= 110) & (df['o2_sat'] >= 50)]
    
    # RULE 1 & 6: Missing / Categorical standardizing (ESI-1 to ESI-5)
    df['esi_priority'] = df['esi_priority'].str.strip().str.upper()
    df['allergy_note'] = df['allergy_note'].replace("UNK", "Unknown")
    
    df.to_csv("../Cleaned_Data/SourceB_triage_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean Source B triage. Quarantined {len(bad_vitals)} bad vitals.")

def clean_SourceB_clinical_notes(df):
    print("Cleaning Source B Clinical Notes...")
    
    # RULE 4: Dates (European format with time)
    df['created_datetime'] = pd.to_datetime(df['created_datetime'], format='%d/%m/%Y %H:%M', errors='coerce')
    
    # RULE 1: Missing values (Quarantine empty notes)
    bad_notes = df[df['note_text'].isna() | (df['note_text'].astype(str).str.strip() == '')].copy()
    bad_notes['rejection_reason'] = "Missing note text"
    bad_notes.to_csv("../Quarantine/SourceB_bad_notes.csv", index=False)
    df = df[~(df['note_text'].isna() | (df['note_text'].astype(str).str.strip() == ''))]
    
    # RULE 3: Text Standardization
    df['note_format'] = df['note_format'].str.strip().str.title()
    
    df.to_csv("../Cleaned_Data/SourceB_clinical_notes_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean clinical notes. Quarantined {len(bad_notes)} empty notes.")

def clean_SourceB_diagnoses(df):
    print("Cleaning Source B Diagnoses...")
    
    # RULE 4: Dates
    df['diag_datetime'] = pd.to_datetime(df['diag_datetime'], format='%d/%m/%Y %H:%M', errors='coerce')
    
    # RULE 6: Categorical Standardization (Yes, YES, yes -> True; No -> False)
    df['is_primary'] = df['is_primary'].str.strip().str.lower().map({'yes': True, 'no': False})
    
    df.to_csv("../Cleaned_Data/SourceB_diagnoses_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean diagnoses.")

def clean_SourceB_diagnostic_orders(df):
    print("Cleaning Source B Diagnostic Orders...")
    
    # RULE 4: Dates
    df['order_datetime'] = pd.to_datetime(df['order_datetime'], format='%d/%m/%Y %H:%M', errors='coerce')
    
    # RULE 3 & 6: Text Standardizing
    df['exam_type'] = df['exam_type'].str.strip().str.title()
    df['order_status'] = df['order_status'].str.strip().str.title()
    # Fix empty strings to 'Unknown'
    df['order_status'] = df['order_status'].replace('', 'Unknown')
    
    # RULE 2: Drop exact duplicate order_ids if any
    df = df.drop_duplicates(subset=['order_id'])
    
    df.to_csv("../Cleaned_Data/SourceB_diagnostic_orders_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean diagnostic orders.")

def clean_SourceB_discharge_records(df):
    print("Cleaning Source B Discharge Records...")
    
    # RULE 4: Dates
    df['discharge_datetime'] = pd.to_datetime(df['discharge_datetime'], format='%d/%m/%Y %H:%M', errors='coerce')
    if 'followup_date' in df.columns:
        df['followup_date'] = pd.to_datetime(df['followup_date'], format='%d/%m/%Y', errors='coerce')
    
    # RULE 6: Map disposition codes to full words
    # Assuming standard hospital codes: HOME, SNF (Skilled Nursing), REHAB, EXP (Expired)
    mapping = {"HOME": "Home", "SNF": "Skilled Nursing Facility", "REHAB": "Rehabilitation", "EXP": "Expired"}
    df['disposition_code'] = df['disposition_code'].str.strip().str.upper().replace(mapping)
    
    df.to_csv("../Cleaned_Data/SourceB_discharge_records_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean discharge records.")

def clean_SourceB_icu_stays(df):
    print("Cleaning Source B ICU Stays...")
    
    # 1. RULE 4: Dates (Using the ACTUAL generator column names)
    df['in_date'] = pd.to_datetime(df['in_date'], format='%d/%m/%Y %H:%M', errors='coerce')
    df['out_date'] = pd.to_datetime(df['out_date'], format='%d/%m/%Y %H:%M', errors='coerce')
    
    # 2. RULE 8: Chronology (Exit before Entry)
    # Note: We check 'out_date' < 'in_date'
    bad_chrono = df[df['out_date'] < df['in_date']].copy()
    bad_chrono['rejection_reason'] = "ICU discharge before ICU admit"
    bad_chrono.to_csv("../Quarantine/SourceB_bad_icu_chrono.csv", index=False)
    df = df[~(df['out_date'] < df['in_date'])]
    
    # 3. RULE 3: Text Standardizing (using 'ward_type')
    df['ward_type'] = df['ward_type'].str.strip().str.upper()
    
    # 4. HARMONIZATION: Rename to match Source A for the unified database
    df = df.rename(columns={
        'ward_type': 'icu_unit',
        'in_date': 'icu_admit_datetime',
        'out_date': 'icu_discharge_datetime'
    })
    
    df.to_csv("../Cleaned_Data/SourceB_icu_stays_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean ICU stays. Quarantined {len(bad_chrono)} bad dates.")

def clean_SourceB_radiology(df):
    print("Cleaning Source B Radiology...")
    
    # Read actual generator columns: 'scan_datetime'
    df['scan_datetime'] = pd.to_datetime(df['scan_datetime'], format='%d/%m/%Y %H:%M', errors='coerce')
    
    # Text standardizing
    df['technician_name'] = df['technician_name'].str.strip().str.title()
    
    # Harmonize names for Task 3 (Integration)
    df = df.rename(columns={
        'scan_datetime': 'exam_datetime',
        'radiologist_conclusion': 'conclusion'
    })
    
    df.to_csv("../Cleaned_Data/SourceB_radiology_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean radiology exams.")

def clean_SourceB_surgical_procedures(df):
    print("Cleaning Source B Surgical Procedures...")
    
    # Read actual generator columns: 'surgery_datetime'
    df['surgery_datetime'] = pd.to_datetime(df['surgery_datetime'], format='%d/%m/%Y %H:%M', errors='coerce')
    
    # Text standardizing (read 'proc_name')
    df['proc_name'] = df['proc_name'].str.strip().str.title()
    
    # Harmonize names for Task 3 (Integration)
    df = df.rename(columns={
        'proc_name': 'procedure_name',
        'proc_code': 'category'
    })
    
    df.to_csv("../Cleaned_Data/SourceB_surgical_procedures_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean surgical procedures.")

# SOURCE C CLEANING FUNCTIONS

def clean_SourceC_patients(df):
    print("Cleaning Source C Patients...")
    
    # 1. HARMONIZATION: Rename to match standard schema (From the profile!)
    df = df.rename(columns={
        'id': 'patient_id',
        'FirstName': 'first_name',
        'LastName': 'last_name',
        'Address': 'address',
        'DateOfBirth': 'date_birth',
        'Gender': 'gender',
        'Phone': 'phone_number'
    })
    
    # RULE 3: Text Standardizing
    df['first_name'] = df['first_name'].astype(str).str.strip().str.title()
    df['last_name'] = df['last_name'].astype(str).str.strip().str.title()
    
    # TRAP FIX: The profile shows Address is just "\n" (a newline character). 
    # We strip it, and if it becomes empty, we fill it.
    df['address'] = df['address'].astype(str).str.strip()
    df['address'] = df['address'].replace({'': 'Unknown', '\\n': 'Unknown'}).fillna('Unknown')
    
    # RULE 1: Missing Values
    df['phone_number'] = df['phone_number'].fillna('Unknown')
    
    # RULE 6: Categorical Standardizing
    df['gender'] = df['gender'].astype(str).str.strip().str.title()
    df['gender'] = df['gender'].replace({'M': 'Male', 'F': 'Female'})
    
    # RULE 4: Dates
    # Note: profile shows dates as "1995-04-08T13:22:27", to_datetime handles this anomaly
    df['date_birth'] = pd.to_datetime(df['date_birth'], errors='coerce')
    
    # RULE 2: Duplicates
    df = df.drop_duplicates(subset=['patient_id'])
    
    df.to_csv("../Cleaned_Data/SourceC_patients_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean Source C patients.")


def clean_SourceC_admissions(df):
    print("Cleaning Source C Admissions...")
    
    # 1. HARMONIZATION
    df = df.rename(columns={
        'id': 'admission_id',
        'patient_ref': 'patient_id',
        'AdmissionDate': 'admission_date_time',
        'DischargeDate': 'discharge_date_time',
        'AdmissionType': 'admission_type',
        'Reason': 'reason_admission',
        'DoctorId': 'admitting_professional_id'
    })
    
    # RULE 4: Dates
    df['admission_date_time'] = pd.to_datetime(df['admission_date_time'], errors='coerce')
    df['discharge_date_time'] = pd.to_datetime(df['discharge_date_time'], errors='coerce')
    
    # RULE 8: Chronology (Discharge before Admit)
    bad_chrono = df[df['discharge_date_time'] < df['admission_date_time']].copy()
    bad_chrono['rejection_reason'] = "Discharge before admission"
    bad_chrono.to_csv("../Quarantine/SourceC_bad_chronology.csv", index=False)
    df = df[~(df['discharge_date_time'] < df['admission_date_time'])]
    
    # RULE 3: Text Standardizing
    df['admission_type'] = df['admission_type'].astype(str).str.strip().str.title()
    df['reason_admission'] = df['reason_admission'].astype(str).str.strip().str.title()
    
    # RULE 2: Duplicates
    df = df.drop_duplicates(subset=['admission_id'])
    
    df.to_csv("../Cleaned_Data/SourceC_admissions_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean Source C admissions. Quarantined {len(bad_chrono)} bad dates.")


def clean_SourceC_triage(df):
    print("Cleaning Source C Triage...")
    
    # 1. HARMONIZATION
    df = df.rename(columns={
        'id': 'triage_id',
        'admission_ref': 'admission_id',
        'NurseId': 'professional_id',
        'HeartRate': 'heart_rate',
        'OxygenSaturation': 'oxygen_saturation',
        'Priority': 'esi_priority'
    })
    
    # RULE 5: Out of bounds vitals
    # The profile shows a min HeartRate of -99! This will catch it.
    bad_vitals = df[(df['heart_rate'] < 0) | (df['oxygen_saturation'] < 50)].copy()
    bad_vitals['rejection_reason'] = "Out of bounds vitals"
    bad_vitals.to_csv("../Quarantine/SourceC_bad_vitals.csv", index=False)
    
    df = df[(df['heart_rate'] >= 0) & (df['oxygen_saturation'] >= 50)]
    
    # RULE 6: Clinical Categories
    df['esi_priority'] = df['esi_priority'].astype(str).str.strip().str.upper()
        
    df.to_csv("../Cleaned_Data/SourceC_triage_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean Source C triage. Quarantined {len(bad_vitals)} bad vitals.")


def clean_SourceC_diagnoses(df):
    print("Cleaning Source C Diagnoses...")
    
    # 1. HARMONIZATION
    df = df.rename(columns={
        'ICD9Code': 'diagnosis_code',
        'Date': 'diagnosis_date_time',
        'IsPrimary': 'primary_diagnosis',
        'DoctorId': 'professional_id'
    })
    
    # RULE 4: Dates
    df['diagnosis_date_time'] = pd.to_datetime(df['diagnosis_date_time'], errors='coerce')
    
    # RULE 3 & 6: Text Standardizing
    # Profile shows ICD9Code is a float (e.g. 410.9). 
    df['diagnosis_code'] = df['diagnosis_code'].astype(str).str.strip()
    
    # RULE 2: Duplicates (Profile shows 11 duplicates!)
    df = df.drop_duplicates()
    
    df.to_csv("../Cleaned_Data/SourceC_diagnoses_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean Source C diagnoses.")

# SOURCE D CLEANING FUNCTIONS

def clean_SourceD_patients(df):
    print("Cleaning Source D Patients...")
    
    # The 'name' and 'contact' columns are dictionaries! 
    # We use .apply(pd.Series) to flatten them into separate columns.
    df = pd.concat([df.drop(['name', 'contact'], axis=1), df['name'].apply(pd.Series), df['contact'].apply(pd.Series)], axis=1)

    # HARMONIZATION
    df = df.rename(columns={
        'patientId': 'patient_id',
        'first': 'first_name',
        'last': 'last_name',
        'dobTimestamp': 'date_birth',
        'gender': 'gender',
        'phone': 'phone_number',
        'city': 'city'
    })
    
    # RULE 4: Dates (Convert UNIX timestamp to actual datetime)
    df['date_birth'] = pd.to_datetime(df['date_birth'], unit='s', errors='coerce')
    
    # The profile shows some dates are in the future (e.g., 2026). Quarantine them!
    future_dates = df[df['date_birth'] > pd.Timestamp.now()].copy()
    future_dates['rejection_reason'] = "Birthdate in the future"
    future_dates.to_csv("../Quarantine/SourceD_future_birthdates.csv", index=False)
    df = df[df['date_birth'] <= pd.Timestamp.now()]

    # RULE 3: Text Standardizing
    df['first_name'] = df['first_name'].astype(str).str.strip().str.title()
    df['last_name'] = df['last_name'].astype(str).str.strip().str.title()
    df['city'] = df['city'].astype(str).str.strip().str.title()
    df['phone_number'] = df['phone_number'].fillna('Unknown')
    
    # RULE 6: Categorical Standardizing
    df['gender'] = df['gender'].replace({'M': 'Male', 'F': 'Female'})
    
    # RULE 2: Duplicates
    df = df.drop_duplicates(subset=['patient_id'])
    
    df.to_csv("../Cleaned_Data/SourceD_patients_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean Source D patients. Quarantined {len(future_dates)} future dates.")


def clean_SourceD_admissions(df):
    print("Cleaning Source D Admissions...")
    
    df = df.rename(columns={
        'visitId': 'admission_id',
        'patientId': 'patient_id',
        'admitTimestamp': 'admission_date_time',
        'dischargeTimestamp': 'discharge_date_time',
        'admissionType': 'admission_type',
        'reason': 'reason_admission',
        'doctorId': 'admitting_professional_id',
        'primary_diagnosis': 'primary_diagnosis'
    })
    
    # RULE 4: Dates (Timestamp is in seconds)
    df['admission_date_time'] = pd.to_datetime(df['admission_date_time'], unit='s', errors='coerce')
    df['discharge_date_time'] = pd.to_datetime(df['discharge_date_time'], unit='s', errors='coerce')
    
    # RULE 8: Chronology
    bad_chrono = df[df['discharge_date_time'] < df['admission_date_time']].copy()
    bad_chrono['rejection_reason'] = "Discharge date before admission date"
    bad_chrono.to_csv("../Quarantine/SourceD_bad_chronology.csv", index=False)
    df = df[~(df['discharge_date_time'] < df['admission_date_time'])]
    
    # RULE 7: Broken FKs (Patient 9999 is the dummy ID)
    bad_fks = df[df['patient_id'] == 9999].copy()
    bad_fks['rejection_reason'] = "Broken patient Foreign Key"
    bad_fks.to_csv("../Quarantine/SourceD_bad_fks.csv", index=False)
    df = df[df['patient_id'] != 9999]
    
    # RULE 3: Text Standardizing
    df['admission_type'] = df['admission_type'].astype(str).str.strip().str.title()
    df['reason_admission'] = df['reason_admission'].astype(str).str.strip().str.title()
    
    # RULE 2: Duplicates
    df = df.drop_duplicates(subset=['admission_id'])
    
    df.to_csv("../Cleaned_Data/SourceD_admissions_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean Source D admissions. Quarantined {len(bad_chrono)} bad dates, {len(bad_fks)} bad FKs.")


def clean_SourceD_triage(df):
    print("Cleaning Source D Triage...")
    
    # FLATTEN the nested 'vitals' dictionary
    df = pd.concat([df.drop(['vitals'], axis=1), df['vitals'].apply(pd.Series)], axis=1)

    df = df.rename(columns={
        'triageId': 'triage_id',
        'visitId': 'admission_id',
        'nurseId': 'professional_id',
        'heartRate': 'heart_rate',
        'oxygenSaturation': 'oxygen_saturation',
        'bloodPressure': 'blood_pressure',
        'triagePriority': 'esi_priority'
    })
    
    # RULE 5: Out of bounds vitals (Profile shows -99 heart rate!)
    bad_vitals = df[(df['heart_rate'] < 0) | (df['oxygen_saturation'] < 50)].copy()
    bad_vitals['rejection_reason'] = "Out of bounds vitals"
    bad_vitals.to_csv("../Quarantine/SourceD_bad_vitals.csv", index=False)
    df = df[(df['heart_rate'] >= 0) & (df['oxygen_saturation'] >= 50)]
    
    # RULE 6: Standardize Categories
    df['esi_priority'] = df['esi_priority'].astype(str).str.strip().str.upper()
    
    # RULE 2: Duplicates
    df = df.drop_duplicates(subset=['triage_id'])
    
    df.to_csv("../Cleaned_Data/SourceD_triage_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean Source D triage. Quarantined {len(bad_vitals)} bad vitals.")


def clean_SourceD_icu(df):
    print("Cleaning Source D ICU Stays...")
    
    df = df.rename(columns={
        'stayId': 'unit_stay_id',
        'visitId': 'admission_id',
        'wardType': 'icu_unit',
        'doctorId': 'professional_id',
        'entryTimestamp': 'entry_date_time',
        'exitTimestamp': 'exit_date_time'
    })
    
    # RULE 4: Dates
    df['entry_date_time'] = pd.to_datetime(df['entry_date_time'], unit='s', errors='coerce')
    df['exit_date_time'] = pd.to_datetime(df['exit_date_time'], unit='s', errors='coerce')
    
    # RULE 8: Chronology
    bad_chrono = df[df['exit_date_time'] < df['entry_date_time']].copy()
    bad_chrono['rejection_reason'] = "Exit date before entry date"
    bad_chrono.to_csv("../Quarantine/SourceD_bad_icu_chrono.csv", index=False)
    df = df[~(df['exit_date_time'] < df['entry_date_time'])]
    
    # RULE 3: Text
    df['icu_unit'] = df['icu_unit'].astype(str).str.strip().str.upper()
    
    # RULE 2: Duplicates
    df = df.drop_duplicates(subset=['unit_stay_id'])
    
    df.to_csv("../Cleaned_Data/SourceD_icu_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean Source D ICU stays. Quarantined {len(bad_chrono)} bad dates.")


def clean_SourceD_notes(df):
    print("Cleaning Source D Clinical Notes...")
    
    df = df.rename(columns={
        'noteId': 'note_id',
        'visitId': 'admission_id',
        'authorId': 'professional_id',
        'noteTimestamp': 'creation_date',
        'noteText': 'note_text'
    })
    
    # RULE 4: Dates
    df['creation_date'] = pd.to_datetime(df['creation_date'], unit='s', errors='coerce')
    
    # RULE 1: Missing values -> Quarantine
    bad_notes = df[df['note_text'].isna() | (df['note_text'].astype(str).str.strip() == '')].copy()
    bad_notes['rejection_reason'] = "Missing note text"
    bad_notes.to_csv("../Quarantine/SourceD_bad_notes.csv", index=False)
    df = df[~(df['note_text'].isna() | (df['note_text'].astype(str).str.strip() == ''))]
    
    # RULE 3: Text Standardizing
    df['note_text'] = df['note_text'].astype(str).str.strip()
    
    # RULE 2: Duplicates
    df = df.drop_duplicates(subset=['note_id'])
    
    df.to_csv("../Cleaned_Data/SourceD_notes_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean Source D notes. Quarantined {len(bad_notes)} empty notes.")


def clean_SourceD_orders(df):
    print("Cleaning Source D Diagnostic Orders...")
    
    df = df.rename(columns={
        'orderId': 'order_id',
        'visitId': 'admission_id',
        'doctorId': 'professional_id',
        'examType': 'exam_type',
        'orderTimestamp': 'request_date_time',
        'examTimestamp': 'exam_date_time',
        'technician': 'technician_name',
        'report_findings': 'findings',
        'report_conclusion': 'conclusion'
    })
    
    # RULE 4: Dates
    df['request_date_time'] = pd.to_datetime(df['request_date_time'], unit='s', errors='coerce')
    df['exam_date_time'] = pd.to_datetime(df['exam_date_time'], unit='s', errors='coerce')
    
    # RULE 3: Text
    df['exam_type'] = df['exam_type'].astype(str).str.strip().str.title()
    df['technician_name'] = df['technician_name'].astype(str).str.strip().str.title()
    
    # RULE 2: Duplicates
    df = df.drop_duplicates(subset=['order_id'])
    
    df.to_csv("../Cleaned_Data/SourceD_orders_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean Source D diagnostic orders.")


def clean_SourceD_discharge(df):
    print("Cleaning Source D Discharge Records...")
    
    df = df.rename(columns={
        'dischargeId': 'discharge_record_id',
        'visitId': 'admission_id',
        'dischargeTimestamp': 'discharge_date_time',
        'destination': 'discharge_destination',
        'condition': 'condition_at_discharge'
    })
    
    # RULE 4: Dates
    df['discharge_date_time'] = pd.to_datetime(df['discharge_date_time'], unit='s', errors='coerce')
    
    # RULE 6: Categories
    mapping = {"HOME": "Home", "SNF": "Skilled Nursing Facility", "REHAB": "Rehabilitation"}
    df['discharge_destination'] = df['discharge_destination'].astype(str).str.strip().str.upper().replace(mapping)
    
    # RULE 3: Text
    df['condition_at_discharge'] = df['condition_at_discharge'].astype(str).str.strip().str.title()
    
    # RULE 2: Duplicates
    df = df.drop_duplicates(subset=['discharge_record_id'])
    
    df.to_csv("../Cleaned_Data/SourceD_discharge_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean Source D discharge records.")


def clean_SourceD_surgery(df):
    print("Cleaning Source D Surgical Procedures...")
    
    df = df.rename(columns={
        'surgeryId': 'procedure_id',
        'visitId': 'admission_id',
        'procedureCode': 'procedure_name',
        'surgeonId': 'professional_id',
        'surgeryTimestamp': 'procedure_date_time'
    })
    
    # RULE 4: Dates
    df['procedure_date_time'] = pd.to_datetime(df['procedure_date_time'], unit='s', errors='coerce')
    
    # RULE 3: Text
    df['procedure_name'] = df['procedure_name'].astype(str).str.strip().str.title()
    
    # RULE 2: Duplicates
    df = df.drop_duplicates(subset=['procedure_id'])
    
    df.to_csv("../Cleaned_Data/SourceD_surgery_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean Source D surgical procedures.")

