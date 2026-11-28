"""
ETL Load Script for Source B
"""

import pandas as pd
from profile import profile_dataframe

SourceB_Files = [
    "admissions",
    "clinical_note",
    "diagnoses",
    "diagnostic_orders",
    "discharge_records",
    "icu_stay",
    "patients",
    "radiology",
    "surgical_procedures",
    "triage_assessments",
]


for file_name in SourceB_Files:
    try:
        path = f"./Data_Sources/SourceB/SourceB_{file_name}.csv"
        df = pd.read_csv(path, sep=",") 
        
    except Exception as e:
        with open("malformed_records_log.txt", "a") as f:
            f.write(f"Failed to load Source B ({file_name}): {e}\n")
            
    else:
        profile_dataframe(df, f"Profiles/SourceB_{file_name}_profile.md")
        print(f"Successfully loaded and profiled Source B: {file_name}")







