import pandas as pd
import os

os.makedirs("../Integrated_Data", exist_ok=True)

print("--- Starting Task 3: Data Integration ---")

# STEP 1: Loading Patient Tables
print("\n--- STEP 1: Patients ---")

# 1 Load all 4 cleaned patient files
df_a = pd.read_csv("../Cleaned_Data/SourceA_patients_clean.csv")
df_b = pd.read_csv("../Cleaned_Data/SourceB_patients_clean.csv")
df_c = pd.read_csv("../Cleaned_Data/SourceC_patients_clean.csv")
df_d = pd.read_csv("../Cleaned_Data/SourceD_patients_clean.csv")

# 2 Source Tracaebility(rubric 6.2) by adding a source label
df_a['source_system'] = 'Source_A'
print("Type of df_a",type(df_a))
print(df_a)
df_b['source_system'] = 'Source_B'
df_c['source_system'] = 'Source_C'
df_d['source_system'] = 'Source_D'

# 3 Rename Columns to match
df_a = df_a.rename(columns={'patient_id': 'source_id', 'name': 'full_name', 'date_birth': 'dob'})
print("Type of df_a",type(df_a))
print(df_a)
df_b = df_b.rename(columns={'patient_mrn': 'source_id', 'full_name': 'full_name', 'dob': 'dob'})
df_c = df_c.rename(columns={'patient_id': 'source_id', 'first_name': 'first_name', 'last_name': 'last_name', 'date_birth': 'dob'})
df_d = df_d.rename(columns={'patientId': 'source_id', 'first_name': 'first_name', 'last_name': 'last_name', 'dobTimestamp': 'dob'})

# 4 Create Global Surrogate keys(rubric 6.1)
unified_patients = pd.concat([df_a, df_b, df_c, df_d], ignore_index=True) # combine all patients in one list
unified_patients['global_patient_id'] = unified_patients.index + 1        # create global surrogate key ID(1,2,......up to 3000)

# 5 ID mapping table(Example: ID 1 from source A is Global ID 1)
patient_mapping = unified_patients[['global_patient_id', 'source_system', 'source_id']]
patient_mapping.to_csv("../Integrated_Data/Map_Patients.csv", index=False)

# 6 cleaning up the columns by droping the old IDs
final_patients = unified_patients.drop(columns=['source_id', 'source_system'])

# 7 Create an unified patients.csv across all continents in a final table
final_patients.to_csv("../Integrated_Data/Unified_Patients.csv", index=False)

print("Saved Patients.")

# STEP 2: Loading Admission Tables
print("\n--- STEP 2: Admissions ---")

# 1 Load all 4 cleaned patient files
df_a_adm = pd.read_csv("../Cleaned_Data/SourceA_admissions_clean.csv")
df_b_adm = pd.read_csv("../Cleaned_Data/SourceB_admissions_clean.csv")
df_c_adm = pd.read_csv("../Cleaned_Data/SourceC_admissions_clean.csv")
df_d_adm = pd.read_csv("../Cleaned_Data/SourceD_admissions_clean.csv")

# 2 ource Tracaebility(rubric 6.2)
df_a_adm['source_system'] = 'Source_A'
df_b_adm['source_system'] = 'Source_B'
df_c_adm['source_system'] = 'Source_C'
df_d_adm['source_system'] = 'Source_D'

# 3 Rename Columns to match
df_a_adm = df_a_adm.rename(columns={'admission_id': 'source_admission_id', 'patient_id': 'source_patient_id'})
df_b_adm = df_b_adm.rename(columns={'admission_id': 'source_admission_id', 'patient_mrn': 'source_patient_id'})
df_c_adm = df_c_adm.rename(columns={'admission_id': 'source_admission_id', 'patient_id': 'source_patient_id'})
df_d_adm = df_d_adm.rename(columns={'admission_id': 'source_admission_id', 'patient_id': 'source_patient_id'})

# 4 Create Global Surrogate keys(rubric 6.1)
unified_adm = pd.concat([df_a_adm, df_b_adm, df_c_adm, df_d_adm], ignore_index=True) # combine all admissions in one list
unified_adm['global_admission_id'] = unified_adm.index + 1     # create global surrogate key ID(1,2,......up to 3000)               

# 5 Map he local patient IDs to the global surrogate key
merged_adm = pd.merge(
    unified_adm, 
    patient_mapping, 
    left_on=['source_system', 'source_patient_id'], 
    right_on=['source_system', 'source_id'], 
    how='left'
)

# 6 cleaning up the columns by droping the old IDs
final_adm = merged_adm.drop(columns=['source_patient_id', 'source_id'])

# 7 Create the admission mapping table
final_adm.to_csv("../Integrated_Data/Unified_Admissions.csv", index=False)
adm_mapping = final_adm[['global_admission_id', 'source_system', 'source_admission_id']].copy()
adm_mapping['source_admission_id'] = adm_mapping['source_admission_id'].astype(str).str.replace(r'\.0$', '', regex=True)

# 8 Save  unified Admission table
adm_mapping.to_csv("../Integrated_Data/Map_Admissions.csv", index=False)
print("Saved Admissions.")

# STEP 3: Loading Triage Tables
print("\n--- STEP 3: Triage ---")

# 1. Load the 4 cleaned triage files
df_a_tri = pd.read_csv("../Cleaned_Data/SourceA_triage_clean.csv")
df_b_tri = pd.read_csv("../Cleaned_Data/SourceB_triage_clean.csv")
df_c_tri = pd.read_csv("../Cleaned_Data/SourceC_triage_clean.csv")
df_d_tri = pd.read_csv("../Cleaned_Data/SourceD_triage_clean.csv")

# 2. Source Traceability
df_a_tri['source_system'] = 'Source_A'
df_b_tri['source_system'] = 'Source_B'
df_c_tri['source_system'] = 'Source_C'
df_d_tri['source_system'] = 'Source_D'

# 3. Rename Columns to match
df_a_tri = df_a_tri.rename(columns={'triage_id': 'source_triage_id', 'admission_id': 'source_admission_id'})
df_b_tri = df_b_tri.rename(columns={'triage_id': 'source_triage_id', 'admission_id': 'source_admission_id'})
df_c_tri = df_c_tri.rename(columns={'id': 'source_triage_id', 'admission_ref': 'source_admission_id'})
df_d_tri = df_d_tri.rename(columns={'triageId': 'source_triage_id', 'visitId': 'source_admission_id'})

# 4 Create Global Surrogate keys(rubric 6.1)
unified_tri = pd.concat([df_a_tri, df_b_tri, df_c_tri, df_d_tri], ignore_index=True)
unified_tri['global_triage_id'] = unified_tri.index + 1 #  Create Global Surrogate key

# 5. Map the local Admission IDs to the Global Admission IDs
# convert the ID to a string to avoid float mismatches
unified_tri['source_admission_id'] = unified_tri['source_admission_id'].astype(str).str.replace(r'\.0$', '', regex=True)

merged_tri = pd.merge(
    unified_tri, 
    adm_mapping, 
    left_on=['source_system', 'source_admission_id'], 
    right_on=['source_system', 'source_admission_id'], 
    how='left'
)

# 7. Cleaning up the columns by dropping the old IDs
final_tri = merged_tri.drop(columns=['source_admission_id'])

# 8. Create the unified Triage table
final_tri.to_csv("../Integrated_Data/Unified_Triage.csv", index=False)
print("Saved Triage.")

# ==========================================
# STEP 4: Loading Diagnoses Tables
# ==========================================
print("\n--- STEP 4: Diagnoses ---")

# 1. Load the 4 cleaned diagnoses files
df_a_diag = pd.read_csv("../Cleaned_Data/SourceA_diagnoses_clean.csv")
df_b_diag = pd.read_csv("../Cleaned_Data/SourceB_diagnoses_clean.csv")
df_c_diag = pd.read_csv("../Cleaned_Data/SourceC_diagnoses_clean.csv")


# 2. Source Traceability
df_a_diag['source_system'] = 'Source_A'
df_b_diag['source_system'] = 'Source_B'
df_c_diag['source_system'] = 'Source_C'


# 3. Rename Columns to match
# Source C's diagnosis_id might just be 'id' due to the XML parsing
df_a_diag = df_a_diag.rename(columns={'diagnosis_id': 'source_diagnosis_id', 'admission_id': 'source_admission_id'})
df_b_diag = df_b_diag.rename(columns={'diagnosis_id': 'source_diagnosis_id', 'admission_id': 'source_admission_id'})
df_c_diag = df_c_diag.rename(columns={'id': 'source_diagnosis_id', 'admission_ref': 'source_admission_id'}) 


# 4. Stack them all together
print("Stacking all diagnoses into one unified table...")
unified_diag = pd.concat([df_a_diag, df_b_diag, df_c_diag], ignore_index=True)

# 5. Create Global Surrogate key
unified_diag['global_diagnosis_id'] = unified_diag.index + 1

# 6. Map the local Admission IDs to the Global Admission IDs
# Convert to string first to ensure the merge doesn't break on float vs int
unified_diag['source_admission_id'] = unified_diag['source_admission_id'].astype(str).str.replace(r'\.0$', '', regex=True)

merged_diag = pd.merge(
    unified_diag, 
    adm_mapping, 
    left_on=['source_system', 'source_admission_id'], 
    right_on=['source_system', 'source_admission_id'], 
    how='left'
)

# 7. Cleaning up the columns
final_diag = merged_diag.drop(columns=['source_admission_id'])

# 8. Create the unified Diagnoses table
final_diag.to_csv("../Integrated_Data/Unified_Diagnoses.csv", index=False)
print("Saved Diagnoses.")


# STEP 5: Loading ICU Stays Tables
print("\n--- STEP 5: ICU Stays ---")

# 1. Load the cleaned ICU files (Source C doesn't have one)
df_a_icu = pd.read_csv("../Cleaned_Data/SourceA_icu_stays_clean.csv")
df_b_icu = pd.read_csv("../Cleaned_Data/SourceB_icu_stays_clean.csv")
df_d_icu = pd.read_csv("../Cleaned_Data/SourceD_icu_clean.csv")

# 2. Source Traceability
df_a_icu['source_system'] = 'Source_A'
df_b_icu['source_system'] = 'Source_B'
df_d_icu['source_system'] = 'Source_D'

# 3. Rename Columns to match
# Note: Source D JSON calls it 'stayId' and 'visitId'
df_a_icu = df_a_icu.rename(columns={'unit_stay_id': 'source_icu_id', 'admission_id': 'source_admission_id'})
df_b_icu = df_b_icu.rename(columns={'unit_stay_id': 'source_icu_id', 'admission_id': 'source_admission_id'})
df_d_icu = df_d_icu.rename(columns={'stayId': 'source_icu_id', 'visitId': 'source_admission_id'})

# 4. Stack them all together
print("Stacking all ICU stays into one unified table...")
unified_icu = pd.concat([df_a_icu, df_b_icu, df_d_icu], ignore_index=True)

# 5. Create Global Surrogate key
unified_icu['global_icu_id'] = unified_icu.index + 1

# 6. Map the local Admission IDs to the Global Admission IDs
unified_icu['source_admission_id'] = unified_icu['source_admission_id'].astype(str).str.replace(r'\.0$', '', regex=True)

merged_icu = pd.merge(
    unified_icu, 
    adm_mapping, 
    left_on=['source_system', 'source_admission_id'], 
    right_on=['source_system', 'source_admission_id'], 
    how='left'
)

# 7. Cleaning up the columns
final_icu = merged_icu.drop(columns=['source_admission_id'])

# 8. Create the unified ICU table
final_icu.to_csv("../Integrated_Data/Unified_ICU_Stays.csv", index=False)
print("Saved ICU Stays.")


# STEP 6: Loading Clinical Notes Tables
print("\n--- STEP 6: Clinical Notes ---")

# 1. Load the cleaned Clinical Notes files
df_a_note = pd.read_csv("../Cleaned_Data/SourceA_clinical_notes_clean.csv")
df_b_note = pd.read_csv("../Cleaned_Data/SourceB_clinical_notes_clean.csv")
df_d_note = pd.read_csv("../Cleaned_Data/SourceD_notes_clean.csv")

# 2. Source Traceability
df_a_note['source_system'] = 'Source_A'
df_b_note['source_system'] = 'Source_B'
df_d_note['source_system'] = 'Source_D'

# 3. Rename Columns to match
df_a_note = df_a_note.rename(columns={'note_id': 'source_note_id', 'admission_id': 'source_admission_id'})
df_b_note = df_b_note.rename(columns={'note_id': 'source_note_id', 'admission_id': 'source_admission_id'})
# Source D JSON uses noteId and visitId
df_d_note = df_d_note.rename(columns={'noteId': 'source_note_id', 'visitId': 'source_admission_id'})

# 4. Stack them all together
print("Stacking all clinical notes into one unified table...")
unified_note = pd.concat([df_a_note, df_b_note, df_d_note], ignore_index=True)

# 5. Create Global Surrogate key
unified_note['global_note_id'] = unified_note.index + 1

# 6. Map the local Admission IDs to the Global Admission IDs
unified_note['source_admission_id'] = unified_note['source_admission_id'].astype(str).str.replace(r'\.0$', '', regex=True)

merged_note = pd.merge(
    unified_note, 
    adm_mapping, 
    left_on=['source_system', 'source_admission_id'], 
    right_on=['source_system', 'source_admission_id'], 
    how='left'
)

# 7. Cleaning up the columns
final_note = merged_note.drop(columns=['source_admission_id'])

# 8. Create the unified Clinical Notes table
final_note.to_csv("../Integrated_Data/Unified_Clinical_Notes.csv", index=False)
print("Saved Clinical Notes.")


# STEP 7: Loading Diagnostic Orders Tables
print("\n--- STEP 7: Diagnostic Orders ---")

# 1. Load the cleaned Diagnostic Orders files
df_a_order = pd.read_csv("../Cleaned_Data/SourceA_diagnostic_orders_clean.csv")
df_b_order = pd.read_csv("../Cleaned_Data/SourceB_diagnostic_orders_clean.csv")
df_d_order = pd.read_csv("../Cleaned_Data/SourceD_orders_clean.csv")

# 2. Source Traceability
df_a_order['source_system'] = 'Source_A'
df_b_order['source_system'] = 'Source_B'
df_d_order['source_system'] = 'Source_D'

# 3. Rename Columns to match
df_a_order = df_a_order.rename(columns={'order_id': 'source_order_id', 'admission_id': 'source_admission_id'})
df_b_order = df_b_order.rename(columns={'order_id': 'source_order_id', 'admission_id': 'source_admission_id'})
# Source D JSON uses orderId and visitId
df_d_order = df_d_order.rename(columns={'orderId': 'source_order_id', 'visitId': 'source_admission_id'})

# 4. Stack them all together
print("Stacking all diagnostic orders into one unified table...")
unified_order = pd.concat([df_a_order, df_b_order, df_d_order], ignore_index=True)

# 5. Create Global Surrogate key
unified_order['global_order_id'] = unified_order.index + 1

# 6. Map the local Admission IDs to the Global Admission IDs
unified_order['source_admission_id'] = unified_order['source_admission_id'].astype(str).str.replace(r'\.0$', '', regex=True)

merged_order = pd.merge(
    unified_order, 
    adm_mapping, 
    left_on=['source_system', 'source_admission_id'], 
    right_on=['source_system', 'source_admission_id'], 
    how='left'
)

# 7. Cleaning up the columns
final_order = merged_order.drop(columns=['source_admission_id'])

# 8. Create the unified Diagnostic Orders table
final_order.to_csv("../Integrated_Data/Unified_Diagnostic_Orders.csv", index=False)
print("Saved Diagnostic Orders.")


# STEP 8: Loading Discharge Records Tables
print("\n--- STEP 8: Discharge Records ---")

# 1. Load the cleaned Discharge Records files
df_a_dis = pd.read_csv("../Cleaned_Data/SourceA_discharge_records_clean.csv")
df_b_dis = pd.read_csv("../Cleaned_Data/SourceB_discharge_records_clean.csv")
df_d_dis = pd.read_csv("../Cleaned_Data/SourceD_discharge_clean.csv")

# 2. Source Traceability
df_a_dis['source_system'] = 'Source_A'
df_b_dis['source_system'] = 'Source_B'
df_d_dis['source_system'] = 'Source_D'

# 3. Rename Columns to match
df_a_dis = df_a_dis.rename(columns={'discharge_record_id': 'source_discharge_id', 'admission_id': 'source_admission_id'})
df_b_dis = df_b_dis.rename(columns={'discharge_record_id': 'source_discharge_id', 'admission_id': 'source_admission_id'})
# Source D JSON uses dischargeId and visitId
df_d_dis = df_d_dis.rename(columns={'dischargeId': 'source_discharge_id', 'visitId': 'source_admission_id'})

# 4. Stack them all together
print("Stacking all discharge records into one unified table...")
unified_dis = pd.concat([df_a_dis, df_b_dis, df_d_dis], ignore_index=True)

# 5. Create Global Surrogate key
unified_dis['global_discharge_id'] = unified_dis.index + 1

# 6. Map the local Admission IDs to the Global Admission IDs
unified_dis['source_admission_id'] = unified_dis['source_admission_id'].astype(str).str.replace(r'\.0$', '', regex=True)

merged_dis = pd.merge(
    unified_dis, 
    adm_mapping, 
    left_on=['source_system', 'source_admission_id'], 
    right_on=['source_system', 'source_admission_id'], 
    how='left'
)

# 7. Cleaning up the columns
final_dis = merged_dis.drop(columns=['source_admission_id'])

# 8. Create the unified Discharge Records table
final_dis.to_csv("../Integrated_Data/Unified_Discharge_Records.csv", index=False)
print("Saved Discharge Records.")


# STEP 9: Loading Surgical Procedures Tables
print("\n--- STEP 9: Surgical Procedures ---")

# 1. Load the cleaned Surgical Procedures files
df_a_surg = pd.read_csv("../Cleaned_Data/SourceA_surgical_procedures_clean.csv")
df_b_surg = pd.read_csv("../Cleaned_Data/SourceB_surgical_procedures_clean.csv")
df_d_surg = pd.read_csv("../Cleaned_Data/SourceD_surgery_clean.csv")

# 2. Source Traceability
df_a_surg['source_system'] = 'Source_A'
df_b_surg['source_system'] = 'Source_B'
df_d_surg['source_system'] = 'Source_D'

# 3. Rename Columns to match
df_a_surg = df_a_surg.rename(columns={'procedure_id': 'source_procedure_id', 'admission_id': 'source_admission_id'})
df_b_surg = df_b_surg.rename(columns={'procedure_id': 'source_procedure_id', 'admission_id': 'source_admission_id'})
# Source D JSON uses surgeryId and visitId
df_d_surg = df_d_surg.rename(columns={'surgeryId': 'source_procedure_id', 'visitId': 'source_admission_id'})

# 4. Stack them all together
print("Stacking all surgical procedures into one unified table...")
unified_surg = pd.concat([df_a_surg, df_b_surg, df_d_surg], ignore_index=True)

# 5. Create Global Surrogate key
unified_surg['global_procedure_id'] = unified_surg.index + 1

# 6. Map the local Admission IDs to the Global Admission IDs
unified_surg['source_admission_id'] = unified_surg['source_admission_id'].astype(str).str.replace(r'\.0$', '', regex=True)

merged_surg = pd.merge(
    unified_surg, 
    adm_mapping, 
    left_on=['source_system', 'source_admission_id'], 
    right_on=['source_system', 'source_admission_id'], 
    how='left'
)

# 7. Cleaning up the columns
final_surg = merged_surg.drop(columns=['source_admission_id'])

# 8. Create the unified Surgical Procedures table
final_surg.to_csv("../Integrated_Data/Unified_Surgical_Procedures.csv", index=False)
print("Saved Surgical Procedures.")

print("\n=== TASK 3 COMPLETE ===")





