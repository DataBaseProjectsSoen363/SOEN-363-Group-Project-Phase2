"""
Generate the CLINICAL_NOTE table for Source B (Continent B / CSV format).
Output: SourceB_Clinical_Note.csv

Differences from Source A:
  - Uses a single unstructured `note_text` column instead of split columns.
  - Uses a `note_format` column (SOAP, Narrative, etc.)
  - Contains newline characters (\n) inside the text blocks.
"""
import csv
import random
from datetime import datetime, timedelta

ADMISSIONS_FILE = "SourceB_Admission.csv"
OUTPUT_FILE = "SourceB_Clinical_Note.csv"
SEED = 707

DOCTOR_MRNS = [f"MRN-{10000 + i}" for i in range(1, 16)]
NOTE_FORMATS = ["SOAP", "Narrative", "Discharge Summary"]

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

def generate_notes():
    random.seed(SEED)
    admissions = load_admissions()

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        
        # Custom headers
        writer.writerow(["note_id", "visit_id", "author_mrn", "note_format", "created_datetime", "note_text"])
        
        note_id = 1
        # Most admissions get a note (~90%)
        for adm in admissions:
            if random.random() > 0.90:
                continue
                
            v_id = adm["visit_id"]
            admit_dt = adm["admit_dt"]
            doctor_mrn = random.choice(DOCTOR_MRNS)
            
            note_dt = admit_dt + timedelta(hours=random.randint(1, 4))
            note_str = note_dt.strftime("%d/%m/%Y %H:%M")

            note_format = random.choice(NOTE_FORMATS)

            # Multi-line free-text note
            note_text = (
                f"Subjective: Patient presents with acute discomfort.\n"
                f"Objective: Vitals show mild elevation. Patient is alert.\n"
                f"Assessment: Suspected acute condition requiring observation.\n"
                f"Plan: Admit for further testing and continuous monitoring."
            )

            # --- ANOMALY: Missing note text (~3%) ---
            if random.random() < 0.03:
                note_text = ""

            # --- ANOMALY: Broken visit FK (~2%) ---
            output_v_id = v_id
            if random.random() < 0.02:
                output_v_id = 9999

            writer.writerow([
                note_id, output_v_id, doctor_mrn, 
                note_format, note_str, note_text
            ])
            note_id += 1

    print(f"Wrote {OUTPUT_FILE} with {note_id - 1} clinical note records.")

if __name__ == "__main__":
    generate_notes()