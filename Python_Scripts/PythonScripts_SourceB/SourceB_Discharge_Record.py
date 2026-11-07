"""
Generate the DISCHARGE_RECORD table for Source B (Continent B / CSV format).
Output: SourceB_Discharge_Record.csv

Differences from Source A:
  - Disposition uses medical abbreviations (HOME, SNF, EXP, REHAB)
  - Date format: DD/MM/YYYY HH:MM
  - Missing followup dates (~10% for living patients)
"""
import csv
import random
from datetime import datetime, timedelta

ADMISSIONS_FILE = "SourceB_Admission.csv"
OUTPUT_FILE = "SourceB_Discharge_Record.csv"
SEED = 1010

DOCTOR_MRNS = [f"MRN-{10000 + i}" for i in range(1, 16)]
DISPOSITIONS = ["HOME", "SNF", "REHAB", "EXP"] # EXP = Expired

def load_admissions(path=ADMISSIONS_FILE):
    valid_admissions = []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["patient_mrn"] == "MRN-99999":
                continue
            # Only process admissions that have a valid, parsable discharge date
            if not row["discharge_date"] or row["discharge_date"] == "Unknown":
                continue
            try:
                admit_dt = datetime.strptime(row["admit_date"], "%d/%m/%Y %H:%M")
                discharge_dt = datetime.strptime(row["discharge_date"], "%d/%m/%Y %H:%M")
                valid_admissions.append({
                    "visit_id": int(row["visit_id"]),
                    "discharge_dt": discharge_dt
                })
            except ValueError:
                # Skips impossible dates like 31/02/2026
                continue
    return valid_admissions

def generate_discharges():
    random.seed(SEED)
    admissions = load_admissions()

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        
        # Custom headers
        writer.writerow([
            "discharge_id", "visit_id", "discharge_datetime", 
            "disposition_code", "followup_date", "discharging_doctor_mrn"
        ])
        
        discharge_id = 1
        for adm in admissions:
            v_id = adm["visit_id"]
            discharge_dt = adm["discharge_dt"]
            discharge_str = discharge_dt.strftime("%d/%m/%Y %H:%M")

            # --- ANOMALY: Broken visit FK (~2%) ---
            output_v_id = v_id
            if random.random() < 0.02:
                output_v_id = 9999

            doctor_mrn = random.choice(DOCTOR_MRNS)
            disposition = random.choice(DISPOSITIONS)
            
            if disposition == "EXP":
                followup_str = "N/A"
            else:
                followup_dt = discharge_dt + timedelta(days=14)
                followup_str = followup_dt.strftime("%d/%m/%Y")
                
                # --- ANOMALY: Missing followup (~10%) ---
                if random.random() < 0.10:
                    followup_str = ""

            writer.writerow([
                discharge_id, output_v_id, discharge_str, 
                disposition, followup_str, doctor_mrn
            ])
            discharge_id += 1

    print(f"Wrote {OUTPUT_FILE} with {discharge_id - 1} discharge records.")

if __name__ == "__main__":
    generate_discharges()