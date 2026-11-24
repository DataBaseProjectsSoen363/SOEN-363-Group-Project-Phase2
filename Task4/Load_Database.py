import pandas as pd
import os
from sqlalchemy import create_engine, text

print("--- Starting Task 4: Load into PostgreSQL (Clean SQLAlchemy Version) ---")

# 1. Database Connection Setup
DB_USER = "postgres"
DB_PASSWORD = "admin"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "hospital_db"

# Create the engine using a dictionary 
engine = create_engine(
    "postgresql+psycopg://", 
    connect_args={
        "user": DB_USER,
        "password": DB_PASSWORD,
        "host": DB_HOST,
        "port": DB_PORT,
        "dbname": DB_NAME
    }
)

# 2. Clean the Database 
print("Dropping old tables to prevent duplication...")

# We use a single transaction to drop all tables safely in reverse order
with engine.begin() as conn:
    tables = [
        "Map_Surgical_Procedures", "Unified_Surgical_Procedures",
        "Map_Discharge_Records", "Unified_Discharge_Records",
        "Map_Diagnostic_Orders", "Unified_Diagnostic_Orders",
        "Map_Clinical_Notes", "Unified_Clinical_Notes",
        "Map_ICU_Stays", "Unified_ICU_Stays",
        "Map_Diagnoses", "Unified_Diagnoses",
        "Map_Triage", "Unified_Triage",
        "Map_Admissions", "Unified_Admissions",
        "Map_Patients", "Unified_Patients"
    ]
    for table in tables:
        conn.execute(text(f"DROP TABLE IF EXISTS {table} CASCADE;"))


# 3. Load Data (Parents First)

print("\nLoading data (Parents first, then children)...")

# This dictionary maintains the load order so Foreign Keys don't break
load_order = {
    # 1. PARENTS
    "Unified_Patients": "Unified_Patients.csv",
    "Map_Patients": "Map_Patients.csv",
    
    # 2. CHILDREN
    "Unified_Admissions": "Unified_Admissions.csv",
    "Map_Admissions": "Map_Admissions.csv",
    
    # 3. GRANDCHILDREN & THEIR MAPS
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
    "Unified_Discharge_Records": "Unified_Discharge_Records.csv",
    "Map_Discharge_Records": "Map_Discharge_Records.csv",
    "Unified_Surgical_Procedures": "Unified_Surgical_Procedures.csv",
    "Map_Surgical_Procedures": "Map_Surgical_Procedures.csv"
}

for table_name, csv_file in load_order.items():
    filepath = f"../Integrated_Data/{csv_file}"
    
    if os.path.exists(filepath):
        df = pd.read_csv(filepath, low_memory=False)
        
        # creates the table schema and inserts the data
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        print(f" -> Loaded {len(df)} rows into {table_name}")
    else:
        print(f" -> WARNING: {csv_file} not found. Skipping.")



print("\n=== TASK 4 COMPLETE ===")