import pandas as pd
from profile import profile_dataframe


# The XPath queries
SourceC_Tags = {
    "Patient":   ".//Patient",
    "Admission": ".//Admission",
    "Triage":    ".//Triage",
    "Diagnosis": ".//Diagnosis",
}

print("--- Starting Task 1 (Profile) for Source C ---\n")

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
        continue  # Skip to the next file if it fails to load

print("All Source C files profiled.")