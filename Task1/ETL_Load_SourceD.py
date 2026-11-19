import pandas as pd
from profile import profile_dataframe


SourceD_Files = [
    "patients",
    "admissions",
    "triage",
    "icu_stays",
    "surgical_procedures",
    "clinical_notes",
    "diagnostic_orders",
    "discharge_records",
]

# TASK 1. PROFILE THE DATA SOURCE D
for file_name in SourceD_Files:
    path = f"../Data_Sources/SourceD/SourceD_{file_name}.json"

    # --- TASK 1: LOAD ---
    try:
        df = pd.read_json(path)
    except Exception as e:
        with open("malformed_records_log.txt", "a") as f:
            f.write(f"Failed to load Source D ({file_name}): {e}\n")
        print(f"[Task 1] FAILED to load: {file_name} -> {e}")
        continue

    # --- TASK 1: PROFILE ---
    try:
        profile_dataframe(df, f"Profiles/SourceD_{file_name}_profile.md")
        print(f"[Task 1] Successfully loaded and profiled: {file_name}")
    except Exception as e:
        with open("malformed_records_log.txt", "a") as f:
            f.write(f"Failed to profile Source D ({file_name}): {e}\n")
        print(f"[Task 1] FAILED to profile: {file_name} -> {e}")

