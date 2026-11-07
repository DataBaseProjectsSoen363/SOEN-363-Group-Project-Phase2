"""
ETL Load Script for Source A
"""
import pandas as pd
from profile import profile_dataframe

SourceA_Files = [
    "patients",
    "admissions",
    "clinical_notes",
    "diagnoses",
    "diagnostic_orders",
    "discharge_records",
    "icd9_dict",
    "icu_stays",
    "professionals",
    "radiology_examinations",
    "radiology_reports",
    "surgical_procedures",
    "triage_assessments"
]

for file_name in SourceA_Files:
    try:
      
        path = f"../Data_Sources/SourceA/SourceA_{file_name}.txt"
        df = pd.read_csv(path, sep="|", skiprows=1)
        
    except Exception as e:
        with open("malformed_records_log.txt", "a") as f:
            f.write(f"Failed to load Source A ({file_name}): {e}\n")
            
    else:
        profile_dataframe(df, f"Profiles/SourceA_{file_name}_profile.md")
        print(f"Successfully loaded and profiled Source A: {file_name}")








