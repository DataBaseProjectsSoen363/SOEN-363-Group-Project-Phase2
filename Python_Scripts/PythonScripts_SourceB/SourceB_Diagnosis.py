"""
Generate the DIAGNOSIS table for Source B (Continent B / CSV format).
Output: SourceB_Diagnosis.csv

Differences from Source A:
  - No patient MRN column (must be joined via visit_id)
  - Boolean flags are "Yes" / "No"
  - Date format: DD/MM/YYYY HH:MM
"""
import csv
import random
from datetime import datetime, timedelta

ADMISSIONS_FILE = "SourceB_Admission.csv"
OUTPUT_FILE = "SourceB_Diagnosis.csv"
SEED = 303

ICD9_CODES = ["401.9", "410.9", "250.00", "272.4"]
DOCTOR_MRNS = [f"MRN-{10000 + i}" for i in range(1, 16)]

def load_admissions(path=ADMISSIONS_FILE):
    """Returns a list of valid visit_ids and their dates."""
    valid_admissions = []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # We only want to attach diagnoses to valid visits
            if row["patient_mrn"] != "MRN-99999":
                valid_admissions.append({
                    "visit_id": int(row["visit_id"]),
                    "admit_date_str": row["admit_date"]
                })
    return valid_admissions

def generate_diagnoses():
    random.seed(SEED)
    admissions = load_admissions()

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        
        # Custom headers
        writer.writerow(["diag_id", "visit_id", "icd9_code", "diag_datetime", "is_primary", "attending_doctor"])
        
        diag_id = 1
        
        # Only generate diagnoses for ~90% of admissions
        for adm in admissions:
            if random.random() > 0.90:
                continue
                
            v_id = adm["visit_id"]
            # Parse the Source B date string to add a few hours
            admit_dt = datetime.strptime(adm["admit_date_str"], "%d/%m/%Y %H:%M")
            diag_dt = admit_dt + timedelta(hours=random.randint(1, 12))
            diag_str = diag_dt.strftime("%d/%m/%Y %H:%M")
            
            doctor_mrn = random.choice(DOCTOR_MRNS)
            
            # 1 to 3 diagnoses per visit
            num_diags = random.randint(1, 3)
            codes = random.sample(ICD9_CODES, k=num_diags)
            
            for i, code in enumerate(codes):
                is_primary = "Yes" if i == 0 else "No"
                
                # --- ANOMALY: Broken visit FK (~2%) ---
                output_v_id = v_id
                if random.random() < 0.02:
                    output_v_id = 9999
                
                # --- ANOMALY: Inconsistent boolean casing (~5%) ---
                primary_val = is_primary
                if random.random() < 0.05:
                    primary_val = random.choice(["YES", "yes", " Yes "])

                writer.writerow([diag_id, output_v_id, code, diag_str, primary_val, doctor_mrn])
                diag_id += 1

    print(f"Wrote {OUTPUT_FILE} with {diag_id - 1} diagnosis records.")

if __name__ == "__main__":
    generate_diagnoses()