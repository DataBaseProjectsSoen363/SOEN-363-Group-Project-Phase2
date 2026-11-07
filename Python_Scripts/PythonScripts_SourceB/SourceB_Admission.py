"""
Generate the ADMISSION table for Source B (Continent B / CSV format).
Output: SourceB_Admission.csv

Reads SourceB_Patient.csv to ensure valid MRNs.
Introduces new anomalies:
  - Impossible dates (e.g., 31/02/2026)
  - Text strings in date fields (e.g., "Unknown")
  - Chronological errors (discharge before admission)
"""
import csv
import random
from datetime import datetime, timedelta

PATIENTS_FILE = "SourceB_Patient.csv"
OUTPUT_FILE = "SourceB_Admission.csv"
SEED = 202
NUM_ADMISSIONS = 1200

# We will use the first 15 MRNs as "doctors" just to have valid IDs for now
# In the real ETL, we'll map these to the physician table.
DOCTOR_MRNS = [f"MRN-{10000 + i}" for i in range(1, 16)]
WARD_CODES = ["EMER", "SURG", "MED", "PEDS", "OBS"]
REASONS = ["Douleur thoracique", "Essoufflement", "Fièvre", "Traumatisme"]

def load_patient_mrns(path=PATIENTS_FILE):
    """Reads the CSV to get valid MRNs for our foreign keys."""
    mrns = []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            mrns.append(row["mrn"])
    return mrns

def generate_admissions():
    random.seed(SEED)
    valid_mrns = load_patient_mrns()

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        
        # Custom headers for Source B
        writer.writerow(["visit_id", "patient_mrn", "admitting_doctor", "admit_date", "discharge_date", "ward_code", "reason_text"])
        
        for a_id in range(1, NUM_ADMISSIONS + 1):
            # --- ANOMALY: Broken FK (~2%) ---
            if random.random() < 0.02:
                patient_mrn = "MRN-99999" # Does not exist
            else:
                patient_mrn = random.choice(valid_mrns)
                
            doctor_mrn = random.choice(DOCTOR_MRNS)
            
            # Dates: DD/MM/YYYY HH:MM
            admit_dt = datetime(2026, 1, 1) + timedelta(days=random.randint(0, 250), hours=random.randint(0, 23))
            discharge_dt = admit_dt + timedelta(days=random.randint(1, 10))
            
            admit_str = admit_dt.strftime("%d/%m/%Y %H:%M")
            discharge_str = discharge_dt.strftime("%d/%m/%Y %H:%M")
            
            # --- ANOMALY: Chronological error (~2%) ---
            if random.random() < 0.02:
                discharge_str = (admit_dt - timedelta(days=2)).strftime("%d/%m/%Y %H:%M")
                
            # --- ANOMALY: Impossible date (~1%) ---
            if random.random() < 0.01:
                discharge_str = "31/02/2026 14:00" # February 31st doesn't exist!
                
            # --- ANOMALY: Missing/Text in date (~1%) ---
            if random.random() < 0.01:
                discharge_str = "Unknown"
                
            ward = random.choice(WARD_CODES)
            reason = random.choice(REASONS)
            
            # --- ANOMALY: Mixed case in reason (~5%) ---
            if random.random() < 0.05:
                reason = reason.upper()
                
            writer.writerow([a_id, patient_mrn, doctor_mrn, admit_str, discharge_str, ward, reason])

    print(f"Wrote {OUTPUT_FILE} with {NUM_ADMISSIONS} admission records.")

if __name__ == "__main__":
    generate_admissions()