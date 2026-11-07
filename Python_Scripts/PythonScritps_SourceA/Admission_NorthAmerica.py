"""
Generate the ADMISSION table for Source A (North America / TXT).
Output: SourceA_admissions.txt

Reads SourceA_patients.txt to get the real patient_id universe, so
clean FKs are guaranteed and the only broken FKs are the deliberate ~2%.
"""
import random
from datetime import datetime, timedelta

NUM_ADMISSIONS = 1200
PATIENTS_FILE = "SourceA_patients.txt"
OUTPUT_FILE = "SourceA_admissions.txt"
SEED = 99

PHYSICIAN_IDS = list(range(1, 16))     # professionals 1..15
BASE_DATE = datetime(2026, 1, 1)
BROKEN_FK_RATE = 0.02                  # ~2% broken patient references
MAX_BROKEN_OFFSET = 50                 # invalid IDs = max(real)+1 .. +50

VALID_TYPES = ["Emergency", "Elective", "Urgent", "Observation"]
ADMISSION_SOURCES = ["Emergency Room", "Physician Referral",
                     "Transfer", "Walk-in"]
REASONS = ["Chest Pain", "Shortness of Breath", "Abdominal Pain",
           "Fever", "Trauma", "Syncope"]
INSURANCE = ["Private Insurance", "Public (RAMQ)", "Self-pay", "None"]
CONDITIONS = ["Stable", "Critical", "Improving", "Observation"]


def load_patient_ids(path=PATIENTS_FILE):
    """Return the list of patient_id values actually written by
    Patient_NorthAmerica.py."""
    ids = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("---"):
                continue
            parts = line.split("|")
            if parts[0] == "patient_id":     # column header
                continue
            try:
                ids.append(int(parts[0]))
            except (ValueError, IndexError):
                continue
    if not ids:
        raise RuntimeError(f"No patient IDs found in {path}")
    return ids


def fmt(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def generate_admissions():
    random.seed(SEED)
    patient_ids = load_patient_ids()
    max_pid = max(patient_ids)
    broken_pool = list(range(max_pid + 1, max_pid + MAX_BROKEN_OFFSET + 1))

    lines = [
        "--- [ADMISSION] ---",
        "admission_id|patient_id|admission_date_time|discharge_date_time"
        "|admission_type|admission_source|reason_admission"
        "|insurance_information|current_condition|admitting_professional_id"
    ]

    for a_id in range(1, NUM_ADMISSIONS + 1):
        # ~2% broken FK, otherwise a real patient
        if random.random() < BROKEN_FK_RATE:
            p_id = random.choice(broken_pool)
        else:
            p_id = random.choice(patient_ids)

        doc_id = random.choice(PHYSICIAN_IDS)
        admit_dt = BASE_DATE + timedelta(
            days=random.randint(0, 250),
            hours=random.randint(0, 23),
            minutes=random.choice([0, 15, 30, 45]))
        discharge_dt = admit_dt + timedelta(days=random.randint(1, 10))

        admit_str = fmt(admit_dt)
        discharge_str = fmt(discharge_dt)

        if random.random() < 0.02:                   # chronological error
            discharge_str = fmt(admit_dt - timedelta(days=2))
        if random.random() < 0.02:                   # open admission
            discharge_str = ""

        a_type = random.choice(VALID_TYPES)
        if random.random() < 0.05:
            a_type = random.choice([a_type.lower(), a_type.upper(),
                                    f" {a_type} "])

        reason = random.choice(REASONS)
        if random.random() < 0.03:
            reason = f"  {reason}  "

        lines.append(
            f"{a_id}|{p_id}|{admit_str}|{discharge_str}"
            f"|{a_type}|{random.choice(ADMISSION_SOURCES)}|{reason}"
            f"|{random.choice(INSURANCE)}|{random.choice(CONDITIONS)}|{doc_id}"
        )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Wrote {OUTPUT_FILE} with {NUM_ADMISSIONS} admissions "
          f"({len(patient_ids)} real patients, ~{BROKEN_FK_RATE:.0%} broken FKs).")


if __name__ == "__main__":
    generate_admissions()