import pandas as pd
from profile import profile_dataframe

# Extract tags from  sml file
SourceC_Tags = {
    "Patient": ".//Patient",
    "Admission": ".//Admission",
    "Triage": ".//Triage",
    "Diagnosis": ".//Diagnosis"
}

for name, xpath_query in SourceC_Tags.items():
    try:
        # Read specific XML tags into a DataFrame
        path = "../Data_Sources/SourceC/SourceC_Hospital.xml"
        df = pd.read_xml(path, xpath=xpath_query)
        
    except Exception as e:
        with open("malformed_records_log.txt", "a") as f:
            f.write(f"Failed to load Source C ({name}): {e}\n")
            
    else:
        profile_dataframe(df, f"Profiles/SourceC_{name}_profile.md")
        print(f"Successfully loaded and profiled Source C: {name}")