"""
ETL Load Script for Source A (Unified Profile)
"""
import os
import pandas as pd
from profile import profile_dataframe

os.makedirs("Profiles", exist_ok=True)

# The Master List
SourceA_Config = [
    "patients", "admissions", "triage_assessments",
    "clinical_notes", "diagnoses", "diagnostic_orders",
    "discharge_records", "icu_stays", "professionals",
    "radiology_examinations", "radiology_reports",
    "surgical_procedures", "icd9_dict",
]

print("--- Starting Task 1 (Profile) ---\n")

for file_name in SourceA_Config:
    path = f"../Data_Sources/SourceA/SourceA_{file_name}.txt"

    # TASK 1: LOAD
    try:
        df = pd.read_csv(path, sep="|", skiprows=1)
    except Exception as e:
        with open("malformed_records_log.txt", "a") as log:
            log.write(f"Failed to load Source A ({file_name}): {e}\n")
        print(f"[Task 1] FAILED to load: {file_name} -> {e}")
        continue

    # TASK 1: PROFILE 
    try:
        profile_dataframe(df, f"Profiles/SourceA_{file_name}_profile.md")
        print(f"[Task 1] Profiled: {file_name}  (rows={len(df)}, cols={df.shape[1]})")
    except Exception as e:
        with open("malformed_records_log.txt", "a") as log:
            log.write(f"Failed to profile Source A ({file_name}): {e}\n")
        print(f"[Task 1] FAILED to profile: {file_name} -> {e}")
        continue

print("All Source A files profiled.")










