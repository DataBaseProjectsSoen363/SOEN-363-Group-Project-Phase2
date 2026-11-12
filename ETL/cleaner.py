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
    
    # RULE 6: Clinical categories (Map EMER -> Emergency)
    df['ward_code'] = df['ward_code'].str.strip().str.upper()
    mapping = {"EMER": "Emergency", "SURG": "Surgery", "MED": "Medical", "PEDS": "Pediatrics", "OBS": "Observation"}
    df['ward_code'] = df['ward_code'].replace(mapping)
    
    # RULE 3: Text standardizing
    df['reason_text'] = df['reason_text'].str.strip().str.title()
    
    df.to_csv("../Cleaned_Data/SourceB_admissions_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean Source B admissions. Quarantined {len(bad_chrono)} bad dates.")


def clean_SourceB_triage(df):
    print("Cleaning Source B Triage...")
    
    # RULE 5: Numeric / Out of bounds vitals
    # Source B uses Fahrenheit (normal body temp is ~98.6F)
    bad_vitals = df[(df['hr_bpm'] < 0) | (df['temp_fahrenheit'] > 110) | (df['o2_sat'] < 50)].copy()
    bad_vitals['rejection_reason'] = "Out of bounds vitals"
    bad_vitals.to_csv("../Quarantine/SourceB_bad_vitals.csv", index=False)
    
    df = df[(df['hr_bpm'] >= 0) & (df['temp_fahrenheit'] <= 110) & (df['o2_sat'] >= 50)]
    
    # RULE 1 & 6: Missing / Categorical standardizing (ESI-1 to ESI-5)
    df['esi_priority'] = df['esi_priority'].str.strip().str.upper()
    df['allergy_note'] = df['allergy_note'].replace("UNK", "Unknown")
    
    df.to_csv("../Cleaned_Data/SourceB_triage_clean.csv", index=False)
    print(f" -> Saved {len(df)} clean Source B triage. Quarantined {len(bad_vitals)} bad vitals.")