"""
Generate the DIAGNOSIS table for Source A (North America / TXT).
Output: SourceA_diagnoses.txt

Reads SourceA_admissions.txt to guarantee referential consistency between
diagnosis.patient_id and admission.patient_id, then injects controlled anomalies.

Record layout (pipe-delimited):
  diagnosis_id | patient_id | admission_id | icd9_code | diagnosis_date_time 
  | primary_diagnosis | secondary_diagnosis | diagnosing_physician_id

Anomalies injected (documented):
  - Missing diagnoses entirely (~10% of admissions have none)
  - Wrong-patient anomaly (~2% of rows: diagnosis.patient_id != admission.patient_id)
  - Broken admission_id FK (~2% of rows point to non-existent admissions)
  - Mixed case in boolean flags (~5%: "TRUE", "True", "FALSE", "false")
"""
import random
from datetime import datetime, timedelta

PATIENTS_FILE = "SourceA_patients.txt"
ADMISSIONS_FILE = "SourceA_admissions.txt"
OUTPUT_FILE = "SourceA_diagnoses.txt"
SEED = 404

PHYSICIAN_IDS = list(range(1, 16))     # professionals 1..15
ICD9_CODES = ["401.9", "410.9", "250.00", "272.4"]

def load_admissions(path=ADMISSIONS_FILE):
    """Returns a list of dicts: {'admission_id': int, 'patient_id': int, 'admit_dt': datetime}"""
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
                # Only consider admissions with valid patient IDs for our baseline
                if p_id <= 800: 
                    admissions.append({"admission_id": a_id, "patient_id": p_id, "admit_dt": admit_dt})
            except (ValueError, IndexError):
                continue
    return admissions

def fmt_bool(val):
    """Inject mixed-case formatting for boolean strings (~5%)"""
    if random.random() < 0.05:
        return random.choice(["TRUE", "True", "FALSE", "false"])
    return "TRUE" if val else "FALSE"

def generate_diagnoses():
    random.seed(SEED)
    admissions = load_admissions()
    
    lines = [
        "--- [DIAGNOSIS] ---",
        "diagnosis_id|patient_id|admission_id|icd9_code|diagnosis_date_time"
        "|primary_diagnosis|secondary_diagnosis|diagnosing_physician_id"
    ]

    diag_id = 1
    total_rows = 0
    wrong_patient_count = 0
    broken_fk_count = 0

    # Process each admission
    for adm in admissions:
        # ~10% of admissions get NO diagnosis at all
        if random.random() < 0.10:
            continue

        a_id = adm["admission_id"]
        true_p_id = adm["patient_id"]
        base_dt = adm["admit_dt"]

        # Generate 1 to 3 diagnoses for this admission
        num_diagnoses = random.randint(1, 3)
        codes = random.sample(ICD9_CODES, k=num_diagnoses)

        for i, code in enumerate(codes):
            is_primary = (i == 0)
            is_secondary = not is_primary
            
            doc_id = random.choice(PHYSICIAN_IDS)
            
            # Diagnosis usually happens shortly after admission
            diag_dt = base_dt + timedelta(hours=random.randint(1, 12))
            dt_str = diag_dt.strftime("%Y-%m-%d %H:%M:%S")

            # --- ANOMALY: Broken FK (~2%) ---
            output_a_id = a_id
            if random.random() < 0.02:
                output_a_id = 9999  # Guaranteed invalid
                broken_fk_count += 1

            # --- ANOMALY: Wrong Patient (~2%) ---
            output_p_id = true_p_id
            if random.random() < 0.02 and output_a_id != 9999:
                output_p_id = random.randint(1, 800) # Randomly pick a different patient
                while output_p_id == true_p_id:       # Ensure it's actually wrong
                    output_p_id = random.randint(1, 800)
                wrong_patient_count += 1

            lines.append(
                f"{diag_id}|{output_p_id}|{output_a_id}|{code}|{dt_str}"
                f"|{fmt_bool(is_primary)}|{fmt_bool(is_secondary)}|{doc_id}"
            )
            diag_id += 1
            total_rows += 1

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Wrote {OUTPUT_FILE} with {total_rows} diagnosis records.")
    print(f"  - Admissions processed: {len(admissions)}")
    print(f"  - Deliberately broken FKs: {broken_fk_count}")
    print(f"  - Deliberately wrong-patient rows: {wrong_patient_count}")

if __name__ == "__main__":
    generate_diagnoses()