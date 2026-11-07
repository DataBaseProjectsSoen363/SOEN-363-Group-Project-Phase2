"""
ETL Load Script for Source A (North America) using Pandas.
Follows SOEN 363 Lecture 14 concepts: read_csv, dropna, fillna, 
replace, drop_duplicates, and pd.merge.
"""
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from datetime import datetime

# ---- DATABASE CONFIG ----
DB_USER = "postgres"
DB_PASS = "your_password_here" # UPDATE THIS
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "hospital_db"

# Create SQLAlchemy engine for Pandas to_sql
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

def clean_basic_text(df, columns):
    """Lecture concept: Standardize text, remove extra whitespace, fix capitalization."""
    for col in columns:
        if col in df.columns:
            # Remove extra whitespace
            df[col] = df[col].astype(str).str.strip()
            # Fix inconsistent capitalization for categories
            if col in ['gender', 'life_status', 'admission_type', 'current_condition']:
                df[col] = df[col].str.title()
    return df

def main():
    print("🚀 Starting Pandas ETL Pipeline for Source A...")

    # =========================================================
    # 1. ICD9_DICT (Reference Table)
    # =========================================================
    # Use read_csv with sep='|' and skiprows to skip the '--- [ICD9_DICT] ---' header
    icd9_df = pd.read_csv("SourceA_icd9_dict.txt", sep="|", skiprows=1)
    icd9_df.to_sql('icd9_dict', engine, if_exists='append', index=False)
    print(f"✅ Loaded {len(icd9_df)} ICD-9 codes.")

    # =========================================================
    # 2. PROFESSIONALS -> Split into physician and nurse
    # =========================================================
    prof_df = pd.read_csv("SourceA_professionals.txt", sep="|", skiprows=1)
    # Lecture concept: replace specific values (normalizing role)
    prof_df['role'] = prof_df['role'].str.strip().str.lower()
    
    # Split using Pandas boolean filtering
    physician_df = prof_df[prof_df['role'] == 'physician'].copy()
    physician_df = physician_df.rename(columns={'professional_id': 'physician_id', 'full_name': 'name'})
    physician_df = physician_df[['physician_id', 'name', 'specialty']]
    
    nurse_df = prof_df[prof_df['role'] == 'nurse'].copy()
    nurse_df = nurse_df.rename(columns={'professional_id': 'nurse_id', 'full_name': 'name'})
    nurse_df = nurse_df[['nurse_id', 'name']]
    
    # Clean text
    physician_df = clean_basic_text(physician_df, ['name'])
    nurse_df = clean_basic_text(nurse_df, ['name'])

    physician_df.to_sql('physician', engine, if_exists='append', index=False)
    nurse_df.to_sql('nurse', engine, if_exists='append', index=False)
    print(f"✅ Loaded {len(physician_df)} physicians and {len(nurse_df)} nurses.")

    # =========================================================
    # 3. PATIENT
    # =========================================================
    patient_df = pd.read_csv("SourceA_patients.txt", sep="|", skiprows=1)
    
    # Lecture concept: fillna (Impute with default value)
    # If phone_number is empty (NaN from read_csv), replace with 'Unknown'
    patient_df['phone_number'] = patient_df['phone_number'].fillna('Unknown')
    
    # Lecture concept: replace specific values
    patient_df['gender'] = patient_df['gender'].replace({'M': 'Male', 'F': 'Female'})
    patient_df['gender'] = patient_df['gender'].fillna('Unknown')
    
    patient_df = clean_basic_text(patient_df, ['name', 'address', 'gender', 'life_status'])
    
    patient_df.to_sql('patient', engine, if_exists='append', index=False)
    print(f"✅ Loaded {len(patient_df)} patients.")

    # =========================================================
    # 4. ADMISSION
    # =========================================================
    adm_df = pd.read_csv("SourceA_admissions.txt", sep="|", skiprows=1)
    
    # Lecture concept: Correct data types
    adm_df['admission_date_time'] = pd.to_datetime(adm_df['admission_date_time'], errors='coerce')
    adm_df['discharge_date_time'] = pd.to_datetime(adm_df['discharge_date_time'], errors='coerce')
    
    # Lecture concept: dropna (Remove rows with missing values on critical fields)
    adm_df = adm_df.dropna(subset=['patient_id', 'admitting_professional_id'])
    
    # Lecture concept: Merge / Join (Reject broken FKs by only keeping valid IDs)
    # Inner join with patient ensures we drop broken patient_ids
    adm_df = pd.merge(adm_df, patient_df[['patient_id']], on='patient_id', how='inner')
    # Inner join with physician ensures we drop broken doctor IDs
    adm_df = pd.merge(adm_df, physician_df[['physician_id']], left_on='admitting_professional_id', right_on='physician_id', how='inner')
    adm_df = adm_df.drop(columns=['physician_id'])
    
    # Fix chronological errors: if discharge < admission, set to NaT (NULL)
    adm_df.loc[adm_df['discharge_date_time'] < adm_df['admission_date_time'], 'discharge_date_time'] = pd.NaT
    
    adm_df = clean_basic_text(adm_df, ['admission_type', 'reason_admission', 'current_condition'])
    
    adm_df.to_sql('admission', engine, if_exists='append', index=False)
    print(f"✅ Loaded {len(adm_df)} clean admissions.")

    # We will use this clean adm_df to validate all downstream tables
    valid_admissions = adm_df[['admission_id', 'patient_id']]

    # =========================================================
    # 5. TRIAGE_ASSESSMENT
    # =========================================================
    triage_df = pd.read_csv("SourceA_triage_assessments.txt", sep="|", skiprows=1)
    
    # Lecture concept: replace specific values (fix "5/10" anomaly)
    triage_df['pain_level'] = triage_df['pain_level'].astype(str).str.replace('/10', '', regex=False)
    triage_df['pain_level'] = pd.to_numeric(triage_df['pain_level'], errors='coerce')
    
    # Handle missing nurse
    triage_df['nurse_id'] = triage_df['nurse_id'].fillna(0).astype(int)
    triage_df.loc[triage_df['nurse_id'] == 0, 'nurse_id'] = None # Convert back to NaN for SQL NULL
    
    # Join to ensure valid FKs
    triage_df = pd.merge(triage_df, valid_admissions[['admission_id']], on='admission_id', how='inner')
    triage_df = pd.merge(triage_df, nurse_df[['nurse_id']], on='nurse_id', how='inner')
    
    # Handle outliers using Pandas boolean filtering (Lecture Slide 16)
    triage_df = triage_df[(triage_df['heart_rate'] > 0) & (triage_df['body_temperature'] < 45)]
    
    triage_df = clean_basic_text(triage_df, ['triage_priority_level'])
    
    triage_df.to_sql('triage_assessment', engine, if_exists='append', index=False)
    print(f"✅ Loaded {len(triage_df)} clean triage assessments.")

    # =========================================================
    # 6. DIAGNOSIS
    # =========================================================
    diag_df = pd.read_csv("SourceA_diagnoses.txt", sep="|", skiprows=1)
    
    # Lecture concept: drop_duplicates
    diag_df = diag_df.drop_duplicates(subset=['admission_id', 'icd9_code'])
    
    # Enforce strict consistency using pd.merge
    # We merge the diagnosis with the admission to see if the patient_ids match
    diag_df = pd.merge(diag_df, valid_admissions, on='admission_id', suffixes=('', '_adm'))
    
    # Fix wrong patient: if diag patient doesn't match admission patient, force it to match
    diag_df.loc[diag_df['patient_id'] != diag_df['patient_id_adm'], 'patient_id'] = diag_df['patient_id_adm']
    
    diag_df = diag_df[['diagnosis_id', 'patient_id', 'admission_id', 'icd9_code', 'diagnosis_date_time', 'primary_diagnosis', 'secondary_diagnosis', 'diagnosing_physician_id']]
    diag_df = pd.merge(diag_df, physician_df[['physician_id']], left_on='diagnosing_physician_id', right_on='physician_id', how='inner').drop(columns=['physician_id'])
    
    diag_df.to_sql('diagnosis', engine, if_exists='append', index=False)
    print(f"✅ Loaded {len(diag_df)} clean diagnoses.")

    # =========================================================
    # 7. ICU_STAY
    # =========================================================
    icu_df = pd.read_csv("SourceA_icu_stays.txt", sep="|", skiprows=1)
    
    # Correct data types
    icu_df['entry_date_time'] = pd.to_datetime(icu_df['entry_date_time'], errors='coerce')
    icu_df['exit_date_time'] = pd.to_datetime(icu_df['exit_date_time'], errors='coerce')
    
    # Fix chronological errors
    icu_df.loc[icu_df['exit_date_time'] < icu_df['entry_date_time'], 'exit_date_time'] = pd.NaT
    
    # Filter valid FKs
    icu_df = pd.merge(icu_df, valid_admissions[['admission_id']], on='admission_id', how='inner')
    icu_df = pd.merge(icu_df, physician_df[['physician_id']], left_on='responsible_physician_id', right_on='physician_id', how='inner').drop(columns=['physician_id'])
    
    icu_df.to_sql('icu_stay', engine, if_exists='append', index=False)
    print(f"✅ Loaded {len(icu_df)} clean ICU stays.")

    # =========================================================
    # 8. SURGICAL_PROCEDURE
    # =========================================================
    surg_df = pd.read_csv("SourceA_surgical_procedures.txt", sep="|", skiprows=1)
    surg_df['procedure_date_time'] = pd.to_datetime(surg_df['procedure_date_time'], errors='coerce')
    
    # Drop duplicates
    surg_df = surg_df.drop_duplicates(subset=['admission_id', 'procedure_name'])
    
    # Filter valid FKs
    surg_df = pd.merge(surg_df, valid_admissions, on='admission_id', suffixes=('', '_adm'))
    surg_df.loc[surg_df['patient_id'] != surg_df['patient_id_adm'], 'patient_id'] = surg_df['patient_id_adm']
    
    surg_df.to_sql('surgical_procedure', engine, if_exists='append', index=False)
    print(f"✅ Loaded {len(surg_df)} clean surgical procedures.")

    # =========================================================
    # 9. CLINICAL_NOTE
    # =========================================================
    notes_df = pd.read_csv("SourceA_clinical_notes.txt", sep="|", skiprows=1)
    
    # Replace garbage text with NaN
    notes_df['patient_symptoms'] = notes_df['patient_symptoms'].replace('ERROR - STRING TRUNCATED', pd.NA)
    
    # Drop duplicates (copy-paste errors)
    notes_df = notes_df.drop_duplicates(subset=['admission_id', 'patient_symptoms'])
    
    # Fill missing text
    notes_df['initial_clinical_findings'] = notes_df['initial_clinical_findings'].fillna("Not documented.")
    
    # Filter valid FKs
    notes_df = pd.merge(notes_df, valid_admissions[['admission_id']], on='admission_id', how='inner')
    notes_df = pd.merge(notes_df, physician_df[['physician_id']], on='physician_id', how='inner')
    
    notes_df.to_sql('clinical_note', engine, if_exists='append', index=False)
    print(f"✅ Loaded {len(notes_df)} clean clinical notes.")

    # =========================================================
    # 10. DIAGNOSTIC_ORDER
    # =========================================================
    orders_df = pd.read_csv("SourceA_diagnostic_orders.txt", sep="|", skiprows=1)
    orders_df['order_status'] = orders_df['order_status'].fillna("Pending")
    
    # Filter valid FKs
    orders_df = pd.merge(orders_df, valid_admissions, on='admission_id', suffixes=('', '_adm'))
    orders_df = pd.merge(orders_df, physician_df[['physician_id']], left_on='requesting_physician_id', right_on='physician_id', how='inner').drop(columns=['physician_id'])
    
    orders_df.to_sql('diagnostic_order', engine, if_exists='append', index=False)
    print(f"✅ Loaded {len(orders_df)} clean diagnostic orders.")

    # =========================================================
    # 11. RADIOLOGY_EXAMINATION & REPORT
    # =========================================================
    exams_df = pd.read_csv("SourceA_radiology_examinations.txt", sep="|", skiprows=1)
    
    exams_df['body_area_examined'] = exams_df['body_area_examined'].fillna("Unspecified")
    exams_df['medical_images'] = exams_df['medical_images'].fillna("No image available")
    
    # Filter valid FKs
    exams_df = pd.merge(exams_df, orders_df[['order_id']], on='order_id', how='inner')
    exams_df = pd.merge(exams_df, physician_df[['physician_id']], left_on='referring_physician_id', right_on='physician_id', how='inner').drop(columns=['physician_id'])
    
    exams_df.to_sql('radiology_examination', engine, if_exists='append', index=False)
    print(f"✅ Loaded {len(exams_df)} clean radiology exams.")

    reports_df = pd.read_csv("SourceA_radiology_reports.txt", sep="|", skiprows=1)
    reports_df['interpretation'] = reports_df['interpretation'].fillna("Pending interpretation.")
    
    # Filter valid FKs
    reports_df = pd.merge(reports_df, exams_df[['examination_id']], left_on='radiology_report_id', right_on='examination_id', how='inner').drop(columns=['examination_id'])
    
    reports_df.to_sql('radiology_report', engine, if_exists='append', index=False)
    print(f"✅ Loaded {len(reports_df)} clean radiology reports.")

    # =========================================================
    # 12. DISCHARGE_RECORD
    # =========================================================
    disc_df = pd.read_csv("SourceA_discharge_records.txt", sep="|", skiprows=1)
    disc_df['discharge_date_time'] = pd.to_datetime(disc_df['discharge_date_time'], errors='coerce')
    
    # Fix logical contradiction
    disc_df.loc[disc_df['discharge_status'] == 'Deceased', 'condition_at_discharge'] = 'Deceased'
    
    # Filter valid FKs
    disc_df = pd.merge(disc_df, valid_admissions[['admission_id']], on='admission_id', how='inner')
    
    disc_df.to_sql('discharge_record', engine, if_exists='append', index=False)
    print(f"✅ Loaded {len(disc_df)} clean discharge records.")

    print("\n🎉 Source A Pandas ETL Pipeline Completed Successfully!")

if __name__ == "__main__":
    main()