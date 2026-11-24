"""
Clean Source D
"""
import pandas as pd
from cleaner import (
    clean_SourceD_patients,
    clean_SourceD_admissions,   
    clean_SourceD_triage,
    clean_SourceD_icu,
    clean_SourceD_surgery,
    clean_SourceD_notes,
    clean_SourceD_orders,
    clean_SourceD_discharge,
)

print("\n--- Starting Task 2 Cleaning for Source D ---")

# Map the REAL filenames to the cleaning functions
cleaners = {
    "patients":              clean_SourceD_patients,
    "admissions":            clean_SourceD_admissions,  
    "triage":                clean_SourceD_triage,
    "icu_stays":             clean_SourceD_icu,
    "surgical_procedures":   clean_SourceD_surgery,
    "clinical_notes":        clean_SourceD_notes,
    "diagnostic_orders":     clean_SourceD_orders,
    "discharge_records":     clean_SourceD_discharge,
}

for name, functions in cleaners.items():
    try:
        path = f"../Data_Sources/SourceD/SourceD_{name}.json"
        df = pd.read_json(path)
    except Exception as e:
        with open("malformed_records_log.txt", "a") as f:
            f.write(f"Failed to load Source D for cleaning ({name}): {e}\n")
        print(f"FAILED to load Source D: {name} -> {e}")
    else:
        functions(df)
        print(f"Successfully cleaned Source D: {name}")

print("All Source D files  cleaned.")