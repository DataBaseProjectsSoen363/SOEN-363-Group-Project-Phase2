"""
Clean Source C
"""
import pandas as pd
from cleaner import (
    clean_SourceC_patients, 
    clean_SourceC_admissions, 
    clean_SourceC_triage, 
    clean_SourceC_diagnoses
)

# 1. Map the XML tags to their specific cleaning functions
SourceC_Config = {
    "Patient":   clean_SourceC_patients,
    "Admission": clean_SourceC_admissions,
    "Triage":    clean_SourceC_triage,
    "Diagnosis": clean_SourceC_diagnoses,
}

# The XPath queries
SourceC_Tags = {
    "Patient": ".//Patient",
    "Admission": ".//Admission",
    "Triage": ".//Triage",
    "Diagnosis": ".//Diagnosis"
}

print("--- Starting Task 2 (Clean) for Source C ---")

path = "../Data_Sources/SourceC/SourceC_Hospital.xml"

for name, xpath_query in SourceC_Tags.items():
        
    cleaner_function = SourceC_Config.get(name)
    if cleaner_function is not None:
        try:
            # Read specific XML tags into a DataFrame
            df = pd.read_xml(path, xpath=xpath_query)
            cleaner_function(df)
            print(f"[Task 2] Successfully cleaned: {name}")
        except Exception as e:
            with open("malformed_records_log.txt", "a") as f:
                f.write(f"Failed to clean Source C ({name}): {e}\n")
            print(f"[Task 2] FAILED to clean: {name} -> {e}\n")
    else:
        print(f"[Task 2] Skipped cleaning: {name} (No cleaner defined)\n")

print("All Source C files  cleaned.")