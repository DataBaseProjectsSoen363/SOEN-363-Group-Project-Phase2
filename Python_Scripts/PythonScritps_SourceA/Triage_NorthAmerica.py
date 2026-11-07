"""
Generate the TRIAGE_ASSESSMENT table for Source A (North America / TXT).
Output: SourceA_triage_assessments.txt

Reads SourceA_admissions.txt to guarantee 1 triage per admission.
Links to nurses (IDs 16-25 from the professionals roster).

Record layout (pipe-delimited):
  triage_id | admission_id | nurse_id | blood_pressure | heart_rate 
  | respiratory_rate | body_temperature | oxygen_saturation | pain_level 
  | reported_symptoms | known_allergies | current_medications | triage_priority_level

Anomalies injected (documented):
  - Out-of-bounds vitals (~3%): heart_rate = -99, temp = 45.2, oxygen = 0
  - Broken admission FK (~2%): admission_id = 9999
  - Missing nurse_id (~2%): left blank
  - Inconsistent triage priority formatting (~5%): " Routine ", "STAT", "urgent"
  - Data type mismatch in pain_level (~2%): "5/10" instead of integer
"""
import random
from datetime import datetime, timedelta

ADMISSIONS_FILE = "SourceA_admissions.txt"
OUTPUT_FILE = "SourceA_triage_assessments.txt"
SEED = 555

NURSE_IDS = list(range(16, 26))  # professionals 16..25 are nurses

PRIORITIES = ["Routine", "Urgent", "STAT", "High-Priority Emergency"]
ALLERGIES = ["None", "Penicillin", "Sulfa drugs", "Latex", "Peanuts"]
MEDS = ["None", "Metformin", "Atorvastatin", "Lisinopril", "Aspirin", "Metoprolol"]
SYMPTOMS = ["Chest Discomfort", "Shortness of Breath", "Abdominal Pain", "Fever", "Dizziness"]

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
                admissions.append({"admission_id": a_id, "admit_dt": admit_dt})
            except (ValueError, IndexError):
                continue
    return admissions

def generate_triage():
    random.seed(SEED)
    admissions = load_admissions()

    lines = [
        "--- [TRIAGE_ASSESSMENT] ---",
        "triage_id|admission_id|nurse_id|blood_pressure|heart_rate"
        "|respiratory_rate|body_temperature|oxygen_saturation|pain_level"
        "|reported_symptoms|known_allergies|current_medications|triage_priority_level"
    ]

    triage_id = 1
    for adm in admissions:
        a_id = adm["admission_id"]
        # Triage happens typically within 1 hour of admission
        triage_dt = adm["admit_dt"] + timedelta(minutes=random.randint(10, 60))

        # --- ANOMALY: Broken admission FK (~2%) ---
        output_a_id = a_id
        if random.random() < 0.02:
            output_a_id = 9999

        # --- ANOMALY: Missing Nurse (~2%) ---
        nurse_id = str(random.choice(NURSE_IDS))
        if random.random() < 0.02:
            nurse_id = ""  # Missing value

        # --- Base Vitals ---
        bp_sys = random.randint(100, 140)
        bp_dia = random.randint(60, 90)
        blood_pressure = f"{bp_sys}/{bp_dia}"
        
        heart_rate = random.randint(60, 110)
        resp_rate = random.randint(12, 22)
        temp = round(random.uniform(36.0, 38.5), 1)
        o2 = random.randint(92, 100)
        pain = random.randint(0, 10)

        # --- ANOMALY: Out-of-bounds vitals (~3%) ---
        if random.random() < 0.03:
            heart_rate = -99
            temp = 45.2
            o2 = 0

        # --- ANOMALY: Data type mismatch in pain_level (~2%) ---
        pain_str = str(pain)
        if random.random() < 0.02:
            pain_str = f"{pain}/10"

        # --- ANOMALY: Inconsistent priority formatting (~5%) ---
        priority = random.choice(PRIORITIES)
        if random.random() < 0.05:
            priority = random.choice([priority.lower(), priority.upper(), f" {priority} "])

        lines.append(
            f"{triage_id}|{output_a_id}|{nurse_id}|{blood_pressure}|{heart_rate}"
            f"|{resp_rate}|{temp}|{o2}|{pain_str}"
            f"|{random.choice(SYMPTOMS)}|{random.choice(ALLERGIES)}|{random.choice(MEDS)}|{priority}"
        )
        triage_id += 1

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Wrote {OUTPUT_FILE} with {triage_id - 1} triage records.")

if __name__ == "__main__":
    generate_triage()