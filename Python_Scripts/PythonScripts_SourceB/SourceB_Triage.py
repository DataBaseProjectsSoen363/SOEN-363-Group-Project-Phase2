"""
Generate the TRIAGE_ASSESSMENT table for Source B (Continent B / CSV format).
Output: SourceB_Triage.csv

Differences from Source A:
  - Temperature in Fahrenheit (e.g., 98.6 instead of 37.0)
  - Blood pressure split into two integer columns (systolic / diastolic)
  - Triage priority uses ESI scale (ESI-1 to ESI-5)
  - Missing values use "UNK"
"""
import csv
import random
from datetime import datetime, timedelta

ADMISSIONS_FILE = "SourceB_Admission.csv"
OUTPUT_FILE = "SourceB_Triage.csv"
SEED = 404

# We will use MRNs 16-25 to represent nurses
NURSE_MRNS = [f"MRN-{10000 + i}" for i in range(16, 26)]
ESI_SCALES = ["ESI-1", "ESI-2", "ESI-3", "ESI-4", "ESI-5"]
ALLERGIES = ["None", "Penicillin", "Sulfa", "Latex", "UNK"]

def load_admissions(path=ADMISSIONS_FILE):
    valid_admissions = []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["patient_mrn"] != "MRN-99999":
                valid_admissions.append({
                    "visit_id": int(row["visit_id"]),
                    "admit_date_str": row["admit_date"]
                })
    return valid_admissions

def generate_triage():
    random.seed(SEED)
    admissions = load_admissions()

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        
        # Custom headers
        writer.writerow([
            "triage_id", "visit_id", "nurse_mrn", "bp_systolic", "bp_diastolic", 
            "hr_bpm", "temp_fahrenheit", "o2_sat", "esi_priority", "allergy_note"
        ])
        
        triage_id = 1
        for adm in admissions:
            v_id = adm["visit_id"]
            
            # --- ANOMALY: Broken visit FK (~2%) ---
            output_v_id = v_id
            if random.random() < 0.02:
                output_v_id = 9999

            nurse_mrn = random.choice(NURSE_MRNS)
            
            # Base vitals (normal ranges)
            bp_sys = random.randint(100, 140)
            bp_dia = random.randint(60, 90)
            hr = random.randint(60, 100)
            # Temperature in Fahrenheit (Normal is ~98.6)
            temp_f = round(random.uniform(97.0, 101.0), 1)
            o2 = random.randint(95, 100)
            
            # --- ANOMALY: Out of bounds vitals (~3%) ---
            if random.random() < 0.03:
                hr = -99
                temp_f = 113.0 # Fatal fever in F

            esi = random.choice(ESI_SCALES)
            allergy = random.choice(ALLERGIES)

            writer.writerow([
                triage_id, output_v_id, nurse_mrn, bp_sys, bp_dia, 
                hr, temp_f, o2, esi, allergy
            ])
            triage_id += 1

    print(f"Wrote {OUTPUT_FILE} with {triage_id - 1} triage records.")

if __name__ == "__main__":
    generate_triage()