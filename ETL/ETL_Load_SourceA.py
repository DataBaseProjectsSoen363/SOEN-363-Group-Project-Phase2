"""
ETL Load Script for Source A
"""
import pandas as pd
from profile import profile_dataframe
from cleaner import clean_SourceA_patients, clean_SourceA_admissions, clean_SourceA_triage

SourceA_Files = [
    "patients", "admissions", "clinical_notes", "diagnoses", 
    "diagnostic_orders", "discharge_records", "icd9_dict", 
    "icu_stays", "professionals", "radiology_examinations", 
    "radiology_reports", "surgical_procedures", "triage_assessments"
]

# TASK 1. PROFILE THE DATA SOURCE A
for file_name in SourceA_Files:
    try:
        path = f"../Data_Sources/SourceA/SourceA_{file_name}.txt"
        df = pd.read_csv(path, sep="|", skiprows=1)
    except Exception as e:
        with open("malformed_records_log.txt", "a") as f:
            f.write(f"Failed to load Source A ({file_name}): {e}\n")
    else:
        profile_dataframe(df, f"Profiles/SourceA_{file_name}_profile.md")
        print(f"Successfully loaded and profiled Source A: {file_name}")


# TASK 2. CLEAN THE DATA SOURCE A
print("\n--- Starting Task 2 Cleaning for Source A ---")

df_patients = pd.read_csv("../Data_Sources/SourceA/SourceA_patients.txt", sep="|", skiprows=1)
clean_SourceA_patients(df_patients) 

df_admissions = pd.read_csv("../Data_Sources/SourceA/SourceA_admissions.txt", sep="|", skiprows=1)
clean_SourceA_admissions(df_admissions) 

df_triage = pd.read_csv("../Data_Sources/SourceA/SourceA_triage_assessments.txt", sep="|", skiprows=1)
clean_SourceA_triage(df_triage) 








