"""
Generate the ICU_STAY table for Source B (Continent B / CSV format).
Output: SourceB_ICU_Stay.csv

Differences from Source A:
  - Uses "WARD-ICU" / "WARD-CCU" naming
  - Adds a ventilator_used column (Y/N)
  - French language reason_text
  - Date format: DD/MM/YYYY HH:MM
"""
import csv
import random
from datetime import datetime, timedelta

ADMISSIONS_FILE = "SourceB_Admission.csv"
OUTPUT_FILE = "SourceB_ICU_Stay.csv"
SEED = 505

DOCTOR_MRNS = [f"MRN-{10000 + i}" for i in range(1, 16)]
WARD_TYPES = ["WARD-ICU", "WARD-CCU", "WARD-SICU"]
REASONS = ["Surveillance continue", "Détresse respiratoire", "Post-opératoire"]

def load_admissions(path=ADMISSIONS_FILE):
    valid_admissions = []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["patient_mrn"] != "MRN-99999":
                # We only want admissions with a valid date string
                try:
                    dt = datetime.strptime(row["admit_date"], "%d/%m/%Y %H:%M")
                    valid_admissions.append({
                        "visit_id": int(row["visit_id"]),
                        "admit_dt": dt
                    })
                except ValueError:
                    continue
    return valid_admissions

def generate_icu_stays():
    random.seed(SEED)
    admissions = load_admissions()

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        
        # Custom headers
        writer.writerow([
            "stay_id", "visit_id", "doctor_mrn", "ward_type", 
            "ventilator_used", "in_date", "out_date", "transfer_reason"
        ])
        
        stay_id = 1
        # Only ~30% of admissions get an ICU stay
        for adm in admissions:
            if random.random() > 0.30:
                continue
                
            v_id = adm["visit_id"]
            admit_dt = adm["admit_dt"]
            doctor_mrn = random.choice(DOCTOR_MRNS)

            # Entry happens 1-24 hours after admission
            entry_dt = admit_dt + timedelta(hours=random.randint(1, 24))
            # Exit happens 1-7 days later
            exit_dt = entry_dt + timedelta(days=random.randint(1, 7))
            
            entry_str = entry_dt.strftime("%d/%m/%Y %H:%M")
            exit_str = exit_dt.strftime("%d/%m/%Y %H:%M")

            # --- ANOMALY: Chronological error (~3%) ---
            if random.random() < 0.03:
                exit_str = (entry_dt - timedelta(hours=5)).strftime("%d/%m/%Y %H:%M")

            # --- ANOMALY: Missing exit date (~5%) ---
            if random.random() < 0.05:
                exit_str = ""

            # --- ANOMALY: Broken visit FK (~2%) ---
            output_v_id = v_id
            if random.random() < 0.02:
                output_v_id = 9999

            ward = random.choice(WARD_TYPES)
            vent = random.choice(["Y", "N"])
            
            reason = random.choice(REASONS)
            # --- ANOMALY: Inconsistent casing (~5%) ---
            if random.random() < 0.05:
                reason = reason.upper()

            writer.writerow([
                stay_id, output_v_id, doctor_mrn, ward, 
                vent, entry_str, exit_str, reason
            ])
            stay_id += 1

    print(f"Wrote {OUTPUT_FILE} with {stay_id - 1} ICU stay records.")

if __name__ == "__main__":
    generate_icu_stays()