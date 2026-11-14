import pandas as pd
from profile import profile_dataframe
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

print("--- Starting Task 1 (Profile) & Task 2 (Clean) for Source C ---\n")

path = "../Data_Sources/SourceC/SourceC_Hospital.xml"

for name, xpath_query in SourceC_Tags.items():
    try:
        # --- TASK 1: LOAD & PROFILE ---
        # Read specific XML tags into a DataFrame
        df = pd.read_xml(path, xpath=xpath_query)
        
        profile_dataframe(df, f"Profiles/SourceC_{name}_profile.md")
        print(f"[Task 1] Successfully loaded and profiled: {name}")
        
    except Exception as e:
        with open("malformed_records_log.txt", "a") as f:
            f.write(f"Failed to load Source C ({name}): {e}\n")
        print(f"[Task 1] FAILED to load: {name} -> {e}\n")
        continue # Skip to the next file if it fails to load
        
    # --- TASK 2: CLEAN ---
    cleaner_function = SourceC_Config.get(name)
    if cleaner_function is not None:
        try:
            cleaner_function(df)
            print(f"[Task 2] Successfully cleaned: {name}\n")
        except Exception as e:
            with open("malformed_records_log.txt", "a") as f:
                f.write(f"Failed to clean Source C ({name}): {e}\n")
            print(f"[Task 2] FAILED to clean: {name} -> {e}\n")
    else:
        print(f"[Task 2] Skipped cleaning: {name} (No cleaner defined)\n")

print("All Source C files profiled and cleaned.")