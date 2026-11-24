"""
Clean Source A 
"""
import pandas as pd
from cleaner import (
    clean_SourceA_patients, clean_SourceA_admissions, clean_SourceA_triage,
    clean_SourceA_clinical_notes, clean_SourceA_diagnoses, clean_SourceA_diagnostic_orders,
    clean_SourceA_discharge_records, clean_SourceA_icu_stays, clean_SourceA_professionals,
    clean_SourceA_radiology_examinations, clean_SourceA_radiology_reports, clean_SourceA_surgical_procedures
)

# The Master Dictionary
SourceA_Config = {
    "patient":           clean_SourceA_patients,
    "admission":         clean_SourceA_admissions,
    "triage_assessment": clean_SourceA_triage,
    "clinical_note":     clean_SourceA_clinical_notes,
    "diagnosis":          clean_SourceA_diagnoses,
    "diagnostic_order":  clean_SourceA_diagnostic_orders,
    "discharge_record":  clean_SourceA_discharge_records,
    "icu_stay":          clean_SourceA_icu_stays,
    "professional":      clean_SourceA_professionals,
    "radiology_examination": clean_SourceA_radiology_examinations,
    "radiology_report":  clean_SourceA_radiology_reports,
    "surgical_procedure": clean_SourceA_surgical_procedures,
    "icd9_dict":          None,  # No cleaner needed for the dictionary
}

print("--- Starting Task 2 (Clean) for Source A ---")

# We iterate over the unified dictionary
for file_name, cleaner_function in SourceA_Config.items():
    path = f"../Data_Sources/SourceA/SourceA_{file_name}.txt"
    
    if cleaner_function is not None:
        try:
            df = pd.read_csv(path, sep="|", skiprows=1)
            cleaner_function(df)
            print(f"[Task 2] Successfully cleaned: {file_name}")
        except Exception as e:
            with open("malformed_records_log.txt", "a") as f:
                f.write(f"Failed to clean Source A ({file_name}): {e}\n")
            print(f"[Task 2] FAILED to clean: {file_name} -> {e}\n")
    else:
        df.to_csv(f"../Cleaned_Data/SourceA_{file_name}_clean.csv", index=False)
        print(f"[Task 2] Skipped cleaning: {file_name} (No cleaner defined)")

print("All Source A files cleaned.")









