"""
Clean Source B
"""
import pandas as pd
from cleaner import (
    clean_SourceB_patients, clean_SourceB_admissions, clean_SourceB_triage,
    clean_SourceB_clinical_notes, clean_SourceB_diagnoses, clean_SourceB_diagnostic_orders,
    clean_SourceB_discharge_records, clean_SourceB_icu_stays, clean_SourceB_radiology,
    clean_SourceB_surgical_procedures
)

# The Master Dictionary
# Keys must exactly match the filename stems (SourceB_<Key>.csv)

SourceB_Config = {
    "patient":            clean_SourceB_patients,
    "admission":          clean_SourceB_admissions,
    "triage_assessment":  clean_SourceB_triage,
    "clinical_note":      clean_SourceB_clinical_notes,
    "diagnosis":          clean_SourceB_diagnoses,
    "diagnostic_order":   clean_SourceB_diagnostic_orders,
    "discharge_record":   clean_SourceB_discharge_records,
    "icu_stay":           clean_SourceB_icu_stays,
    "radiology":          clean_SourceB_radiology,
    "surgical_procedure": clean_SourceB_surgical_procedures,
}

print("--- Starting Task 2 (Clean) for Source B ---")

for file_name, cleaner_function in SourceB_Config.items():
    path = f"../Data_Sources/SourceB/SourceB_{file_name}.csv"
    
    if cleaner_function is not None:
        try:
            df = pd.read_csv(path, sep=",")
            cleaner_function(df)
            print(f"[Task 2] Successfully cleaned: {file_name}")
        except Exception as e:
            with open("malformed_records_log.txt", "a") as f:
                f.write(f"Failed to clean Source B ({file_name}): {e}\n")
            print(f"[Task 2] FAILED to clean: {file_name} -> {e}\n")
    else:
        print(f"[Task 2] Skipped cleaning: {file_name} (No cleaner defined)\n")

print("All Source B files cleaned.")