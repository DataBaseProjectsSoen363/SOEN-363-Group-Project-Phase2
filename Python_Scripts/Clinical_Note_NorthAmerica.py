"""
Generate the CLINICAL_NOTE table for Source A (North America / TXT).
Output: SourceA_clinical_notes.txt

Reads SourceA_admissions.txt to anchor notes to valid admissions.
Links to physicians (IDs 1-15).

Record layout (pipe-delimited):
  note_id | admission_id | physician_id | type | creation_date 
  | patient_symptoms | physical_examination | initial_clinical_findings 
  | suspected_condition | planned_diagnostic_examinations | initial_treatment

Anomalies injected (documented):
  - Missing note text (~3%): blank clinical findings or treatments
  - Broken admission FK (~2%): admission_id = 9999
  - Duplicate notes (~2%): exact copy-paste of a previous note
  - Inconsistent note type formatting (~5%): " progress note ", "PROGRESS NOTE"
  - Garbage text / truncation (~1%): "ERROR - STRING TRUNCATED" in symptoms
"""
import random
from datetime import datetime, timedelta

ADMISSIONS_FILE = "SourceA_admissions.txt"
OUTPUT_FILE = "SourceA_clinical_notes.txt"
SEED = 888

PHYSICIAN_IDS = list(range(1, 16))     # professionals 1..15
NOTE_TYPES = ["Progress Note", "Admission Note", "Consultation Note"]

SYMPTOMS = [
    "Patient reports severe chest pain radiating to the left arm.",
    "Shortness of breath and mild dizziness upon standing.",
    "Abdominal tenderness and nausea since this morning.",
    "Fever and chills, accompanied by a persistent cough."
]
EXAM = [
    "Vitals stable, alert and oriented.",
    "Mild discomfort on palpation of the abdomen.",
    "Lungs clear to auscultation bilaterally.",
    "Heart rate regular, no murmurs detected."
]
FINDINGS = [
    "Mild elevation in troponin levels.",
    "ECG shows normal sinus rhythm.",
    "Slight leukocytosis noted in blood work.",
    "No acute abnormalities found on initial review."
]
SUSPECTED = [
    "Acute coronary syndrome suspected.",
    "Rule out pulmonary embolism.",
    "Likely viral gastroenteritis.",
    "Possible early-stage pneumonia."
]
PLANNED = [
    "ECG and chest imaging ordered.",
    "Basic metabolic panel and CBC ordered.",
    "Abdominal ultrasound requested.",
    "Awaiting lab results before further intervention."
]
TREATMENT = [
    "Oxygen therapy administered.",
    "IV fluids started.",
    "Analgesics provided for pain management.",
    "Antibiotics initiated."
]

def load_admissions(path=ADMISSIONS_FILE):
    """Returns a list of dicts with admission_id and admission_date_time."""
    admissions = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("---") or line.startswith("admission_id"):
                continue
            parts = line.split("|")
            try:
                a_id = int(parts[0])
                admit_dt = datetime.strptime(parts[2], "%Y-%m-%d %H:%M:%S")
                # Only use clean admissions as our baseline
                if a_id <= 1200:
                    admissions.append({"admission_id": a_id, "admit_dt": admit_dt})
            except (ValueError, IndexError):
                continue
    return admissions

def generate_clinical_notes():
    random.seed(SEED)
    admissions = load_admissions()

    lines = [
        "--- [CLINICAL_NOTE] ---",
        "note_id|admission_id|physician_id|type|creation_date"
        "|patient_symptoms|physical_examination|initial_clinical_findings"
        "|suspected_condition|planned_diagnostic_examinations|initial_treatment"
    ]

    note_id = 1
    # Most admissions get at least one clinical note (90%)
    for adm in admissions:
        if random.random() > 0.90:
            continue

        a_id = adm["admission_id"]
        doc_id = random.choice(PHYSICIAN_IDS)
        
        # Note created shortly after admission
        note_dt = adm["admit_dt"] + timedelta(hours=random.randint(1, 4))
        note_str = note_dt.strftime("%Y-%m-%d %H:%M:%S")

        # --- ANOMALY: Broken admission FK (~2%) ---
        output_a_id = a_id
        if random.random() < 0.02:
            output_a_id = 9999

        # --- ANOMALY: Inconsistent note type formatting (~5%) ---
        note_type = random.choice(NOTE_TYPES)
        if random.random() < 0.05:
            note_type = random.choice([note_type.lower(), note_type.upper(), f" {note_type} "])

        symptoms = random.choice(SYMPTOMS)
        exam = random.choice(EXAM)
        findings = random.choice(FINDINGS)
        suspected = random.choice(SUSPECTED)
        planned = random.choice(PLANNED)
        treatment = random.choice(TREATMENT)

        # --- ANOMALY: Garbage text / truncation (~1%) ---
        if random.random() < 0.01:
            symptoms = "ERROR - STRING TRUNCATED"

        # --- ANOMALY: Missing note text (~3%) ---
        if random.random() < 0.03:
            findings = ""
        if random.random() < 0.03:
            treatment = ""

        # Base clinical note row
        base_row = (
            f"{note_id}|{output_a_id}|{doc_id}|{note_type}|{note_str}"
            f"|{symptoms}|{exam}|{findings}|{suspected}|{planned}|{treatment}"
        )
        lines.append(base_row)
        note_id += 1

        # --- ANOMALY: Duplicate Note (~2%) ---
        if random.random() < 0.02:
            # Copy-paste the exact same note (with a new note_id)
            duplicate_row = (
                f"{note_id}|{output_a_id}|{doc_id}|{note_type}|{note_str}"
                f"|{symptoms}|{exam}|{findings}|{suspected}|{planned}|{treatment}"
            )
            lines.append(duplicate_row)
            note_id += 1

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Wrote {OUTPUT_FILE} with {note_id - 1} clinical note records.")

if __name__ == "__main__":
    generate_clinical_notes()