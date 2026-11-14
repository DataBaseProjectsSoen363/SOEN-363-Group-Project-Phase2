"""
ETL Load Script for Source A (Unified Profile & Clean)
"""
import pandas as pd
from profile import profile_dataframe
from cleaner import (
    clean_SourceA_patients, clean_SourceA_admissions, clean_SourceA_triage,
    clean_SourceA_clinical_notes, clean_SourceA_diagnoses, clean_SourceA_diagnostic_orders,
    clean_SourceA_discharge_records, clean_SourceA_icu_stays, clean_SourceA_professionals,
    clean_SourceA_radiology_examinations, clean_SourceA_radiology_reports, clean_SourceA_surgical_procedures
)

# The Master Dictionary
SourceA_Config = {
    "patients":           clean_SourceA_patients,
    "admissions":         clean_SourceA_admissions,
    "triage_assessments": clean_SourceA_triage,
    "clinical_notes":     clean_SourceA_clinical_notes,
    "diagnoses":          clean_SourceA_diagnoses,
    "diagnostic_orders":  clean_SourceA_diagnostic_orders,
    "discharge_records":  clean_SourceA_discharge_records,
    "icu_stays":          clean_SourceA_icu_stays,
    "professionals":      clean_SourceA_professionals,
    "radiology_examinations": clean_SourceA_radiology_examinations,
    "radiology_reports":  clean_SourceA_radiology_reports,
    "surgical_procedures": clean_SourceA_surgical_procedures,
    "icd9_dict":          None,  # No cleaner needed for the dictionary
}

print("--- Starting Task 1 (Profile) & Task 2 (Clean) for Source A ---\n")

# We iterate over the unified dictionary
for file_name, cleaner_function in SourceA_Config.items():
    path = f"../Data_Sources/SourceA/SourceA_{file_name}.txt"
    
    # --- TASK 1: LOAD & PROFILE ---
    try:
        df = pd.read_csv(path, sep="|", skiprows=1)
    except Exception as e:
        with open("malformed_records_log.txt", "a") as f:
            f.write(f"Failed to load Source A ({file_name}): {e}\n")
        continue 
    
    # Profile the raw data
    profile_dataframe(df, f"Profiles/SourceA_{file_name}_profile.md")
    print(f"[Task 1] Successfully loaded and profiled: {file_name}")
    
    # --- TASK 2: CLEAN ---
    if cleaner_function is not None:
        try:
            cleaner_function(df)
            print(f"[Task 2] Successfully cleaned: {file_name}\n")
        except Exception as e:
            with open("malformed_records_log.txt", "a") as f:
                f.write(f"Failed to clean Source A ({file_name}): {e}\n")
            print(f"[Task 2] FAILED to clean: {file_name} -> {e}\n")
    else:
        df.to_csv(f"../Cleaned_Data/SourceA_{file_name}_clean.csv", index=False)
        print(f"[Task 2] Skipped cleaning: {file_name} (No cleaner defined)\n")

print("All Source A files profiled and cleaned.")











