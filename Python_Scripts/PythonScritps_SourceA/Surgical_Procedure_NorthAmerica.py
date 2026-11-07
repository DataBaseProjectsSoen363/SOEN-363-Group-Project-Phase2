"""
Generate the SURGICAL_PROCEDURE table for Source A (North America / TXT).
Output: SourceA_surgical_procedures.txt

Reads SourceA_admissions.txt to enforce strict patient_id consistency 
and detect chronological errors against discharge dates.

Record layout (pipe-delimited):
  procedure_id | admission_id | patient_id | procedure_name 
  | body_site | procedure_date_time | surgeon_id

Anomalies injected (documented):
  - Chronological error (~4%): procedure_date_time > discharge_date_time
  - Wrong-patient anomaly (~2%): patient_id != admission.patient_id
  - Broken admission FK (~2%): admission_id = 9999
  - Inconsistent procedure_name formatting (~5%): mixed case / spaces
"""
import random
from datetime import datetime, timedelta

ADMISSIONS_FILE = "SourceA_admissions.txt"
OUTPUT_FILE = "SourceA_surgical_procedures.txt"
SEED = 777

PHYSICIAN_IDS = list(range(1, 16))     # surgeons are physicians 1..15
PROCEDURES = [
    ("Appendectomy", "Appendix"),
    ("Cholecystectomy", "Gallbladder"),
    ("Knee Replacement", "Left Knee"),
    ("Coronary Artery Bypass Graft", "Heart"),
    ("Bowel Resection", "Small Intestine")
]

def load_admissions(path=ADMISSIONS_FILE):
    """Returns a list of dicts with admission_id, patient_id, and datetime objects."""
    admissions = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("---") or line.startswith("admission_id"):
                continue
            parts = line.split("|")
            try:
                a_id = int(parts[0])
                p_id = int(parts[1])
                admit_dt = datetime.strptime(parts[2], "%Y-%m-%d %H:%M:%S")
                
                # Handle missing discharge dates (open admissions) gracefully
                discharge_dt = None
                if parts[3]:
                    discharge_dt = datetime.strptime(parts[3], "%Y-%m-%d %H:%M:%S")
                
                # Only use clean admissions as our baseline
                if p_id <= 800 and a_id <= 1200:
                    admissions.append({
                        "admission_id": a_id, 
                        "patient_id": p_id, 
                        "admit_dt": admit_dt,
                        "discharge_dt": discharge_dt
                    })
            except (ValueError, IndexError):
                continue
    return admissions

def generate_surgical_procedures():
    random.seed(SEED)
    admissions = load_admissions()

    lines = [
        "--- [SURGICAL_PROCEDURE] ---",
        "procedure_id|admission_id|patient_id|procedure_name"
        "|body_site|procedure_date_time|surgeon_id"
    ]

    proc_id = 1
    # Surgeries only happen in ~20% of admissions
    for adm in admissions:
        if random.random() > 0.20:
            continue

        a_id = adm["admission_id"]
        true_p_id = adm["patient_id"]
        admit_dt = adm["admit_dt"]
        discharge_dt = adm["discharge_dt"]

        proc_name, body_site = random.choice(PROCEDURES)
        doc_id = random.choice(PHYSICIAN_IDS)

        # Surgery usually happens 1 to 3 days into the stay
        proc_dt = admit_dt + timedelta(days=random.randint(1, 3), hours=random.randint(0, 12))

        # --- ANOMALY: Post-discharge surgery (~4%) ---
        if discharge_dt and random.random() < 0.04:
            proc_dt = discharge_dt + timedelta(days=2) # Surgery happens after leaving!

        proc_str = proc_dt.strftime("%Y-%m-%d %H:%M:%S")

        # --- ANOMALY: Broken admission FK (~2%) ---
        output_a_id = a_id
        if random.random() < 0.02:
            output_a_id = 9999

        # --- ANOMALY: Wrong-patient (~2%) ---
        output_p_id = true_p_id
        if random.random() < 0.02 and output_a_id != 9999:
            output_p_id = random.randint(1, 800)
            while output_p_id == true_p_id:
                output_p_id = random.randint(1, 800)

        # --- ANOMALY: Inconsistent formatting (~5%) ---
        formatted_name = proc_name
        if random.random() < 0.05:
            formatted_name = random.choice([proc_name.lower(), proc_name.upper(), f" {proc_name} "])

        lines.append(
            f"{proc_id}|{output_a_id}|{output_p_id}|{formatted_name}"
            f"|{body_site}|{proc_str}|{doc_id}"
        )
        proc_id += 1

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Wrote {OUTPUT_FILE} with {proc_id - 1} surgical procedure records.")

if __name__ == "__main__":
    generate_surgical_procedures()