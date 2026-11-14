import pandas as pd
from profile import profile_dataframe
from cleaner import (
    clean_SourceB_patients, clean_SourceB_admissions, clean_SourceB_triage,
    clean_SourceB_clinical_notes, clean_SourceB_diagnoses, clean_SourceB_diagnostic_orders,
    clean_SourceB_discharge_records, clean_SourceB_icu_stays, clean_SourceB_radiology,
    clean_SourceB_surgical_procedures
)

# The Master Dictionary
# Keys must exactly match the filename stems (SourceB_<Key>.csv)

SourceB_Config = {
    "Patient":            clean_SourceB_patients,
    "Admission":          clean_SourceB_admissions,
    "Triage":             clean_SourceB_triage,
    "Clinical_Note":      clean_SourceB_clinical_notes,
    "Diagnosis":          clean_SourceB_diagnoses,
    "Diagnostic_Order":   clean_SourceB_diagnostic_orders,
    "Discharge_Record":   clean_SourceB_discharge_records,
    "ICU_Stay":           clean_SourceB_icu_stays,
    "Radiology":          clean_SourceB_radiology,
    "Surgical_Procedure": clean_SourceB_surgical_procedures,
}

print("--- Starting Task 1 (Profile) & Task 2 (Clean) for Source B ---\n")

for file_name, cleaner_function in SourceB_Config.items():
    path = f"../Data_Sources/SourceB/SourceB_{file_name}.csv"
    
    # --- TASK 1: LOAD & PROFILE ---
    try:
        df = pd.read_csv(path, sep=",")
    except Exception as e:
        with open("malformed_records_log.txt", "a") as f:
            f.write(f"Failed to load Source B ({file_name}): {e}\n")
        # If we can't even load it, skip to the next file entirely
        continue 
    
    # Profile the raw data
    profile_dataframe(df, f"Profiles/SourceB_{file_name}_profile.md")
    print(f"[Task 1] Successfully loaded and profiled: {file_name}")
    
    # --- TASK 2: CLEAN ---
    if cleaner_function is not None:
        try:
            cleaner_function(df)
            print(f"[Task 2] Successfully cleaned: {file_name}\n")
        except Exception as e:
            with open("malformed_records_log.txt", "a") as f:
                f.write(f"Failed to clean Source B ({file_name}): {e}\n")
            print(f"[Task 2] FAILED to clean: {file_name} -> {e}\n")
    else:
        print(f"[Task 2] Skipped cleaning: {file_name} (No cleaner defined)\n")

print("All Source B files profiled and cleaned.")