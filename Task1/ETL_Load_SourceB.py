import os
import pandas as pd
from profile import profile_dataframe

os.makedirs("Profiles", exist_ok=True)

# The Master List
# Names must exactly match the filename stems (SourceB_<name>.csv)

SourceB_Config = [
    "patient",
    "admission",
    "triage_assessment",
    "clinical_note",
    "diagnosis",
    "diagnostic_order",
    "discharge_record",
    "icu_stay",
    "radiology",
    "surgical_procedure",
]

print("--- Starting Task 1 (Profile)  ---")

for file_name in SourceB_Config:
    path = f"../Data_Sources/SourceB/SourceB_{file_name}.csv"

    # --- TASK 1: LOAD ---
    try:
        df = pd.read_csv(path, sep=",")
    except Exception as e:
        with open("malformed_records_log.txt", "a") as log:
            log.write(f"Failed to load Source B ({file_name}): {e}\n")
        print(f"[Task 1] FAILED to load: {file_name} -> {e}")
        continue

    # --- TASK 1: PROFILE ---
    try:
        profile_dataframe(df, f"Profiles/SourceB_{file_name}_profile.md")
        print(f"[Task 1] Profiled: {file_name}  (rows={len(df)}, cols={df.shape[1]})")
    except Exception as e:
        with open("malformed_records_log.txt", "a") as log:
            log.write(f"Failed to profile Source B ({file_name}): {e}\n")
        print(f"[Task 1] FAILED to profile: {file_name} -> {e}")
        continue

print("All Source B files profiled.")