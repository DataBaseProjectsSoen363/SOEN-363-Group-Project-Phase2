import pandas as pd
from profile import profile_dataframe
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

SourceD_Files = [
    "patients",
    "admissions",
    "triage",
    "icu",
    "surgery",
    "notes",
    "orders",
    "discharge",
]

# TASK 1. PROFILE THE DATA SOURCE D
for file_name in SourceD_Files:
    try:
        path = f"../Data_Sources/SourceD/SourceD_{file_name}.json"
        df = pd.read_json(path)
    except Exception as e:
        with open("malformed_records_log.txt", "a") as f:
            f.write(f"Failed to load Source D ({file_name}): {e}\n")
    else:
        profile_dataframe(df, f"Profiles/SourceD_{file_name}_profile.md")
        print(f"Successfully loaded and profiled Source D: {file_name}")


# TASK 2. CLEAN THE DATA SOURCE D
print("\n--- Starting Task 2 Cleaning for Source D ---")

cleaners = {
    "patients":   clean_SourceD_patients,
    "admissions": clean_SourceD_admissions,  
    "triage":     clean_SourceD_triage,
    "icu":        clean_SourceD_icu,
    "surgery":    clean_SourceD_surgery,
    "notes":      clean_SourceD_notes,
    "orders":     clean_SourceD_orders,
    "discharge":  clean_SourceD_discharge,
}

for name, functions in cleaners.items():
    try:
        path = f"../Data_Sources/SourceD/SourceD_{name}.json"
        df = pd.read_json(path)
    except Exception as e:
        with open("malformed_records_log.txt", "a") as f:
            f.write(f"Failed to load Source D for cleaning ({name}): {e}\n")
    else:
        functions(df)
        print(f"Successfully cleaned Source D: {name}")