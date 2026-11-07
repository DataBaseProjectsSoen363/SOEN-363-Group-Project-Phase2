"""
Generate the SURGICAL_PROCEDURE table for Source B (Continent B / CSV format).
Output: SourceB_Surgical_Procedure.csv

Differences from Source A:
  - Uses procedure codes (e.g., "PROC-APP") instead of plain text names.
  - Date format: DD/MM/YYYY HH:MM
  - Missing surgery dates (~2%)
"""
import csv
import random
from datetime import datetime, timedelta

ADMISSIONS_FILE = "SourceB_Admission.csv"
OUTPUT_FILE = "SourceB_Surgical_Procedure.csv"
SEED = 606

DOCTOR_MRNS = [f"MRN-{10000 + i}" for i in range(1, 16)]
# Using medical codes for procedures
PROCEDURES = [
    ("PROC-APP", "Appendectomy"),
    ("PROC-CHOL", "Cholecystectomy"),
    ("PROC-KNEE", "Knee Replacement"),
    ("PROC-CABG", "Coronary Artery Bypass"),
    ("PROC-BOWEL", "Bowel Resection")
]

def load_admissions(path=ADMISSIONS_FILE):
    valid_admissions = []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["patient_mrn"] != "MRN-99999":
                try:
                    dt = datetime.strptime(row["admit_date"], "%d/%m/%Y %H:%M")
                    valid_admissions.append({
                        "visit_id": int(row["visit_id"]),
                        "admit_dt": dt
                    })
                except ValueError:
                    continue
    return valid_admissions

def generate_surgeries():
    random.seed(SEED)
    admissions = load_admissions()

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        
        # Custom headers
        writer.writerow([
            "surgery_id", "visit_id", "surgeon_mrn", 
            "proc_code", "proc_name", "surgery_datetime"
        ])
        
        surgery_id = 1
        # Surgeries happen in ~20% of admissions
        for adm in admissions:
            if random.random() > 0.20:
                continue
                
            v_id = adm["visit_id"]
            admit_dt = adm["admit_dt"]
            doctor_mrn = random.choice(DOCTOR_MRNS)

            proc_code, proc_name = random.choice(PROCEDURES)

            # Surgery happens 1-3 days after admission
            surg_dt = admit_dt + timedelta(days=random.randint(1, 3), hours=random.randint(0, 12))
            surg_str = surg_dt.strftime("%d/%m/%Y %H:%M")

            # --- ANOMALY: Broken visit FK (~2%) ---
            output_v_id = v_id
            if random.random() < 0.02:
                output_v_id = 9999

            # --- ANOMALY: Missing surgery date (~2%) ---
            if random.random() < 0.02:
                surg_str = ""

            writer.writerow([
                surgery_id, output_v_id, doctor_mrn, 
                proc_code, proc_name, surg_str
            ])
            surgery_id += 1

    print(f"Wrote {OUTPUT_FILE} with {surgery_id - 1} surgical records.")

if __name__ == "__main__":
    generate_surgeries()