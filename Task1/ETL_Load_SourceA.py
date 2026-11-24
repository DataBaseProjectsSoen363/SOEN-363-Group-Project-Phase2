"""
ETL Load Script for Source A (Unified Profile)
"""
import os
import pandas as pd
from profile import profile_dataframe

os.makedirs("Profiles", exist_ok=True)

# The Master List
SourceA_Config = [
    "patient", "admission", "triage_assessment",
    "clinical_note", "diagnosis", "diagnostic_order",
    "discharge_record", "icu_stay", "professional",
    "radiology_examination", "radiology_report",
    "surgical_procedure", "icd9_dict",
]

print("--- Starting Task 1 (Profile) ---")

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










