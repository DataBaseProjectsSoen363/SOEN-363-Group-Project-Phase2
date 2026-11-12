import pandas as pd
from profile import profile_dataframe
from cleaner import clean_SourceB_patients, clean_SourceB_admissions, clean_SourceB_triage

SourceB_Files = [
    "Admission", "Clinical_Note", "Diagnosis", "Diagnostic_Order", 
    "Discharge_Record", "ICU_Stay", "Patient", "Radiology", 
    "Surgical_Procedure", "Triage"
]

# TASK 1. PROFILE THE DATA SOURCE B

for file_name in SourceB_Files:
    try:
        path = f"../Data_Sources/SourceB/SourceB_{file_name}.csv"
        df = pd.read_csv(path, sep=",") 
        
    except Exception as e:
        with open("malformed_records_log.txt", "a") as f:
            f.write(f"Failed to load Source B ({file_name}): {e}\n")
            
    else:
        profile_dataframe(df, f"Profiles/SourceB_{file_name}_profile.md")
        print(f"Successfully loaded and profiled Source B: {file_name}")

# TASK 2: CLEAN SOURCE B
print("\n--- Starting Task 2 Cleaning for Source B ---")

# 1. Clean Source B Patients
df_patients = pd.read_csv("../Data_Sources/SourceB/SourceB_Patient.csv", sep=",")
clean_SourceB_patients(df_patients)

# 2. Clean Source B Admissions
df_admissions = pd.read_csv("../Data_Sources/SourceB/SourceB_Admission.csv", sep=",")
clean_SourceB_admissions(df_admissions)

# 3. Clean Source B Triage
df_triage = pd.read_csv("../Data_Sources/SourceB/SourceB_Triage.csv", sep=",")
clean_SourceB_triage(df_triage)