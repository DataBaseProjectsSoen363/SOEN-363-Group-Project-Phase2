import pandas as pd
from profile import profile_dataframe

SourceD_Files = [
    "patients",
    "admissions",
    "triage",
    "icu",
    "surgery",
    "notes",
    "orders",
    "discharge"
]

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