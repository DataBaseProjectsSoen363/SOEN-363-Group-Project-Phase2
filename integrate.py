import os
import pandas as pd

CLEAN_DIR = "./Cleaned_Source"
OUT_DIR = "./Integrated_Data"
SOURCES = ["A", "B", "C", "D"]

# Adjust continent names 
CONTINENT_MAP = {
    "Source_A": "North America",
    "Source_B": "Europe",
    "Source_C": "Asia",
    "Source_D": "South America",
}

os.makedirs(OUT_DIR, exist_ok=True)

print("--- Starting Task 3: Data Integration ---")


def load_clean_table(source_letter, table_name):
    path = f"{CLEAN_DIR}/Source{source_letter}/{table_name}.csv"
    df = pd.read_csv(path, dtype=str, keep_default_na=False)
    meta_cols = [c for c in df.columns if c.startswith("_")]
    df = df.drop(columns=meta_cols, errors="ignore")
    df = df.replace("", pd.NA)
    df["source_system"] = f"Source_{source_letter}"
    return df


def concat_sources(table_name):
    frames = []
    for s in SOURCES:
        df = load_clean_table(s, table_name)
        if not df.empty:
            frames.append(df)
    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index=True)


def normalize_id_col(series):
    return series.astype(str).str.replace(r"\.0$", "", regex=True)


# STEP 0: Source Systems & Continent Traceability (Section 3.2)
print("\n--- STEP 0: Source Systems ---")
source_systems_df = pd.DataFrame([
    {"source_system": src, "continent": cont}
    for src, cont in CONTINENT_MAP.items()
])
source_systems_df.to_csv(f"{OUT_DIR}/Source_Systems.csv", index=False)
print(f"Saved Source Systems ({len(source_systems_df)} rows).")


# STEP 1: Reference & Staff Tables (ICD-9 Dictionary, Physicians, Nurses)
print("\n--- STEP 1: Reference & Staff Tables ---")
icd9_df = load_clean_table("A", "icd9_dict").drop(columns=["source_system"])
icd9_df.to_csv(f"{OUT_DIR}/Unified_ICD9_Dict.csv", index=False)
print(f"Saved ICD-9 Dictionary ({len(icd9_df)} rows).")

phys_df = load_clean_table("A", "physician")
phys_df = phys_df.rename(columns={"physician_id": "source_physician_id"})
phys_df["source_physician_id"] = normalize_id_col(
    phys_df["source_physician_id"]
)
phys_df["global_physician_id"] = phys_df.index + 1
phys_df[["global_physician_id", "source_system", "source_physician_id"]].to_csv(
    f"{OUT_DIR}/Map_Physicians.csv", index=False
)
phys_df.drop(columns=["source_physician_id", "source_system"]).to_csv(
    f"{OUT_DIR}/Unified_Physicians.csv", index=False
)
print(f"Saved Physicians ({len(phys_df)} rows).")

nurse_df = load_clean_table("A", "nurse")
nurse_df = nurse_df.rename(columns={"nurse_id": "source_nurse_id"})
nurse_df["source_nurse_id"] = normalize_id_col(nurse_df["source_nurse_id"])
nurse_df["global_nurse_id"] = nurse_df.index + 1
nurse_df[["global_nurse_id", "source_system", "source_nurse_id"]].to_csv(
    f"{OUT_DIR}/Map_Nurses.csv", index=False
)
nurse_df.drop(columns=["source_nurse_id", "source_system"]).to_csv(
    f"{OUT_DIR}/Unified_Nurses.csv", index=False
)
print(f"Saved Nurses ({len(nurse_df)} rows).")


# STEP 2: Patients
print("\n--- STEP 2: Patients ---")
unified_patients = concat_sources("patient")
unified_patients = unified_patients.rename(columns={
    "patient_id": "source_id",
    "name": "full_name",
    "date_birth": "dob",
})
unified_patients["source_id"] = normalize_id_col(unified_patients["source_id"])
unified_patients["global_patient_id"] = unified_patients.index + 1
unified_patients["continent"] = unified_patients["source_system"].map(
    CONTINENT_MAP
)

patient_mapping = unified_patients[
    ["global_patient_id", "source_system", "continent", "source_id"]
].copy()
patient_mapping.to_csv(f"{OUT_DIR}/Map_Patients.csv", index=False)

final_patients = unified_patients.drop(
    columns=["source_id", "source_system", "continent"]
)
final_patients.to_csv(f"{OUT_DIR}/Unified_Patients.csv", index=False)
print(f"Saved Patients ({len(final_patients)} rows).")


# STEP 3: Admissions
print("\n--- STEP 3: Admissions ---")
unified_adm = concat_sources("admission")
unified_adm = unified_adm.rename(columns={
    "admission_id": "source_admission_id",
    "patient_id": "source_patient_id",
})
unified_adm["source_admission_id"] = normalize_id_col(
    unified_adm["source_admission_id"]
)
unified_adm["source_patient_id"] = normalize_id_col(
    unified_adm["source_patient_id"]
)
unified_adm["global_admission_id"] = unified_adm.index + 1

merged_adm = pd.merge(
    unified_adm,
    patient_mapping[["global_patient_id", "source_system", "source_id"]],
    left_on=["source_system", "source_patient_id"],
    right_on=["source_system", "source_id"],
    how="left",
)

adm_mapping = (
    merged_adm[["global_admission_id", "source_system", "source_admission_id"]]
    .drop_duplicates(subset=["source_system", "source_admission_id"])
    .copy()
)
adm_mapping.to_csv(f"{OUT_DIR}/Map_Admissions.csv", index=False)

final_adm = merged_adm.drop(
    columns=["source_patient_id", "source_id", "source_admission_id"]
)
final_adm.to_csv(f"{OUT_DIR}/Unified_Admissions.csv", index=False)
print(f"Saved Admissions ({len(final_adm)} rows).")


# Helper for Admission Child Tables
def integrate_child_table(
    step_num,
    label,
    clean_table,
    source_pk_col,
    mapped_pk_col,
    global_pk_col,
    source_fk_col,
    mapped_fk_col,
    parent_map_df,
    map_filename,
    unified_filename,
):
    print(f"\n--- STEP {step_num}: {label} ---")
    unified_df = concat_sources(clean_table)
    if unified_df.empty:
        print(f"No rows found for {label}, skipping.")
        return pd.DataFrame()

    unified_df = unified_df.rename(columns={
        source_pk_col: mapped_pk_col,
        source_fk_col: mapped_fk_col,
    })
    unified_df[mapped_pk_col] = normalize_id_col(unified_df[mapped_pk_col])
    unified_df[mapped_fk_col] = normalize_id_col(unified_df[mapped_fk_col])
    unified_df[global_pk_col] = unified_df.index + 1

    merged_df = pd.merge(
        unified_df,
        parent_map_df,
        on=["source_system", mapped_fk_col],
        how="left",
    )

    mapping_df = merged_df[
        [global_pk_col, "source_system", mapped_pk_col]
    ].copy()
    mapping_df.to_csv(f"{OUT_DIR}/{map_filename}", index=False)

    final_df = merged_df.drop(columns=[mapped_fk_col, mapped_pk_col])
    final_df.to_csv(f"{OUT_DIR}/{unified_filename}", index=False)
    print(f"Saved {label} ({len(final_df)} rows).")
    return mapping_df


# STEP 4: Triage Assessments
integrate_child_table(
    4,
    "Triage",
    "triage_assessment",
    "triage_id",
    "source_triage_id",
    "global_triage_id",
    "admission_id",
    "source_admission_id",
    adm_mapping,
    "Map_Triage.csv",
    "Unified_Triage.csv",
)

# STEP 5: Diagnoses
integrate_child_table(
    5,
    "Diagnoses",
    "diagnosis",
    "diagnosis_id",
    "source_diagnosis_id",
    "global_diagnosis_id",
    "admission_id",
    "source_admission_id",
    adm_mapping,
    "Map_Diagnoses.csv",
    "Unified_Diagnoses.csv",
)

# STEP 6: ICU Stays
integrate_child_table(
    6,
    "ICU Stays",
    "icu_stay",
    "unit_stay_id",
    "source_icu_id",
    "global_icu_id",
    "admission_id",
    "source_admission_id",
    adm_mapping,
    "Map_ICU_Stays.csv",
    "Unified_ICU_Stays.csv",
)

# STEP 7: Clinical Notes
integrate_child_table(
    7,
    "Clinical Notes",
    "clinical_note",
    "note_id",
    "source_note_id",
    "global_note_id",
    "admission_id",
    "source_admission_id",
    adm_mapping,
    "Map_Clinical_Notes.csv",
    "Unified_Clinical_Notes.csv",
)

# STEP 8: Diagnostic Orders
order_mapping = integrate_child_table(
    8,
    "Diagnostic Orders",
    "diagnostic_order",
    "order_id",
    "source_order_id",
    "global_order_id",
    "admission_id",
    "source_admission_id",
    adm_mapping,
    "Map_Diagnostic_Orders.csv",
    "Unified_Diagnostic_Orders.csv",
)

# STEP 9: Radiology Examinations (Child of Diagnostic Orders)
integrate_child_table(
    9,
    "Radiology Examinations",
    "radiology_examination",
    "examination_id",
    "source_examination_id",
    "global_examination_id",
    "order_id",
    "source_order_id",
    order_mapping,
    "Map_Radiology_Examinations.csv",
    "Unified_Radiology_Examinations.csv",
)

# STEP 10: Discharge Records
integrate_child_table(
    10,
    "Discharge Records",
    "discharge_record",
    "discharge_record_id",
    "source_discharge_id",
    "global_discharge_id",
    "admission_id",
    "source_admission_id",
    adm_mapping,
    "Map_Discharge_Records.csv",
    "Unified_Discharge_Records.csv",
)

# STEP 11: Surgical Procedures
integrate_child_table(
    11,
    "Surgical Procedures",
    "surgical_procedure",
    "procedure_id",
    "source_procedure_id",
    "global_procedure_id",
    "admission_id",
    "source_admission_id",
    adm_mapping,
    "Map_Surgical_Procedures.csv",
    "Unified_Surgical_Procedures.csv",
)

print("\n=== TASK 3 COMPLETE ===")
