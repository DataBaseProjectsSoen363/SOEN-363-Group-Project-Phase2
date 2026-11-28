import os
import pandas as pd
from sqlalchemy import create_engine, text

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

print("--- Starting Task 4: Load into PostgreSQL ---")

# 1. Database Connection Setup
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "hospital_db")

if not DB_PASSWORD:
    raise RuntimeError(
        "DB_PASSWORD is not set. Add it to your .env file or environment variables."
    )

engine = create_engine(
    "postgresql+psycopg://",
    connect_args={
        "user": DB_USER,
        "password": DB_PASSWORD,
        "host": DB_HOST,
        "port": DB_PORT,
        "dbname": DB_NAME,
    },
)


# 2. Clean & Rebuild Schema from SQL/SQL_Schema.sql
print("Dropping old tables and rebuilding schema from SQL/SQL_Schema.sql...")

tables_to_drop = [
    "Map_Surgical_Procedures",
    "Unified_Surgical_Procedures",
    "Map_Discharge_Records",
    "Unified_Discharge_Records",
    "Map_Radiology_Examinations",
    "Unified_Radiology_Examinations",
    "Map_Diagnostic_Orders",
    "Unified_Diagnostic_Orders",
    "Map_Clinical_Notes",
    "Unified_Clinical_Notes",
    "Map_ICU_Stays",
    "Unified_ICU_Stays",
    "Map_Diagnoses",
    "Unified_Diagnoses",
    "Map_Triage",
    "Unified_Triage",
    "Map_Admissions",
    "Unified_Admissions",
    "Map_Patients",
    "Unified_Patients",
    "Map_Nurses",
    "Unified_Nurses",
    "Map_Physicians",
    "Unified_Physicians",
    "Unified_ICD9_Dict",
    "Source_Systems",
]

with engine.begin() as conn:
    for table in tables_to_drop:
        conn.execute(text(f'DROP TABLE IF EXISTS "{table}" CASCADE;'))

    with open("./SQL/SQL_Schema.sql", "r", encoding="utf-8") as schema_file:
        conn.execute(text(schema_file.read()))

# 3. Load Data (Parents First, Then Children)
print("\nLoading data into constrained tables...")

load_order = {
    # 1. REFERENCE & LOOKUP PARENTS
    "Source_Systems": "Source_Systems.csv",
    "Unified_ICD9_Dict": "Unified_ICD9_Dict.csv",
    "Unified_Physicians": "Unified_Physicians.csv",
    "Map_Physicians": "Map_Physicians.csv",
    "Unified_Nurses": "Unified_Nurses.csv",
    "Map_Nurses": "Map_Nurses.csv",
    # 2. CORE PARENTS
    "Unified_Patients": "Unified_Patients.csv",
    "Map_Patients": "Map_Patients.csv",
    # 3. CHILDREN
    "Unified_Admissions": "Unified_Admissions.csv",
    "Map_Admissions": "Map_Admissions.csv",
    # 4. GRANDCHILDREN & THEIR MAPS
    "Unified_Triage": "Unified_Triage.csv",
    "Map_Triage": "Map_Triage.csv",
    "Unified_Diagnoses": "Unified_Diagnoses.csv",
    "Map_Diagnoses": "Map_Diagnoses.csv",
    "Unified_ICU_Stays": "Unified_ICU_Stays.csv",
    "Map_ICU_Stays": "Map_ICU_Stays.csv",
    "Unified_Clinical_Notes": "Unified_Clinical_Notes.csv",
    "Map_Clinical_Notes": "Map_Clinical_Notes.csv",
    "Unified_Diagnostic_Orders": "Unified_Diagnostic_Orders.csv",
    "Map_Diagnostic_Orders": "Map_Diagnostic_Orders.csv",
    # 5. GREAT-GRANDCHILDREN (Child of Diagnostic Orders)
    "Unified_Radiology_Examinations": "Unified_Radiology_Examinations.csv",
    "Map_Radiology_Examinations": "Map_Radiology_Examinations.csv",
    # 6. REMAINING ADMISSION CHILDREN
    "Unified_Discharge_Records": "Unified_Discharge_Records.csv",
    "Map_Discharge_Records": "Map_Discharge_Records.csv",
    "Unified_Surgical_Procedures": "Unified_Surgical_Procedures.csv",
    "Map_Surgical_Procedures": "Map_Surgical_Procedures.csv",
}

with engine.begin() as conn:
    for table_name, csv_file in load_order.items():
        filepath = f"./Integrated_Data/{csv_file}"
        if os.path.exists(filepath):
            df = pd.read_csv(
                filepath,
                dtype=str,
                keep_default_na=False,
            )
            df = df.replace("", pd.NA)

            for col in df.columns:
                if col.startswith("global_") or col in {"heart_rate", "oxygen_saturation"}:
                    df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")
                elif col in {
                    "respiratory_rate",
                    "body_temperature",
                    "temp_fahrenheit",
                    "bp_systolic",
                    "bp_diastolic",
                    "pain_level",
                }:
                    df[col] = pd.to_numeric(df[col], errors="coerce")
                elif col in {
                    "primary_diagnosis",
                    "secondary_diagnosis",
                    "ventilator_used",
                    "contrast_used",
                }:
                    df[col] = df[col].map({
                        "True": True,
                        "False": False,
                        "TRUE": True,
                        "FALSE": False,
                    })
                elif col in {"dob", "followup_appointments"}:
                    df[col] = pd.to_datetime(
                        df[col], format="mixed", errors="coerce"
                    ).dt.date
                elif col in {
                    "admission_date_time",
                    "discharge_date_time",
                    "diagnosis_date_time",
                    "entry_date_time",
                    "exit_date_time",
                    "creation_date",
                    "request_date_time",
                    "examination_date_time",
                    "procedure_date_time",
                }:
                    df[col] = pd.to_datetime(
                        df[col], format="mixed", errors="coerce", utc=True
                    )

            df.to_sql(table_name, conn, if_exists="append", index=False)
            print(f" -> Loaded {len(df)} rows into {table_name}")
        else:
            print(f" -> WARNING: {csv_file} not found. Skipping.")

print("\n=== TASK 4 COMPLETE ===")
