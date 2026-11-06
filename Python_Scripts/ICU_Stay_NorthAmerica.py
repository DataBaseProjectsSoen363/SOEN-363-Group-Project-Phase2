"""
Generate the ICU_STAY table for Source A (North America / TXT).
Output: SourceA_icu_stays.txt

Reads SourceA_admissions.txt to anchor ICU stays to real admission timelines.
Links to physicians (IDs 1-15).

Record layout (pipe-delimited):
  unit_stay_id | admission_id | responsible_physician_id | unit_type 
  | room_number | bed_number | entry_date_time | exit_date_time | reason_transfer

Anomalies injected (documented):
  - Chronological error (~3%): exit_date_time < entry_date_time
  - Missing exit date (~5%): patient is still in the ICU (open stay)
  - Broken admission FK (~2%): admission_id = 9999
  - Inconsistent unit_type formatting (~5%): "icu", " CCU "
"""
import random
from datetime import datetime, timedelta

ADMISSIONS_FILE = "SourceA_admissions.txt"
OUTPUT_FILE = "SourceA_icu_stays.txt"
SEED = 666

PHYSICIAN_IDS = list(range(1, 16))     # professionals 1..15
UNIT_TYPES = ["ICU", "CCU", "MICU", "SICU"]

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

def generate_icu_stays():
    random.seed(SEED)
    admissions = load_admissions()

    lines = [
        "--- [ICU_STAY] ---",
        "unit_stay_id|admission_id|responsible_physician_id|unit_type"
        "|room_number|bed_number|entry_date_time|exit_date_time|reason_transfer"
    ]

    stay_id = 1
    # Not every admission requires an ICU stay. 
    # We will generate ICU stays for ~30% of the admissions.
    for adm in admissions:
        if random.random() > 0.30:
            continue

        a_id = adm["admission_id"]
        doc_id = random.choice(PHYSICIAN_IDS)

        # --- ANOMALY: Broken admission FK (~2%) ---
        output_a_id = a_id
        if random.random() < 0.02:
            output_a_id = 9999

        # ICU entry happens typically 1-24 hours after admission
        entry_dt = adm["admit_dt"] + timedelta(hours=random.randint(1, 24))
        
        # ICU stay lasts between 1 and 7 days
        exit_dt = entry_dt + timedelta(days=random.randint(1, 7), hours=random.randint(0, 23))

        # --- ANOMALY: Chronological error (~3%) ---
        if random.random() < 0.03:
            exit_dt = entry_dt - timedelta(days=2) # Exits before entering!

        entry_str = entry_dt.strftime("%Y-%m-%d %H:%M:%S")
        exit_str = exit_dt.strftime("%Y-%m-%d %H:%M:%S")

        # --- ANOMALY: Missing exit date (~5%) ---
        if random.random() < 0.05:
            exit_str = ""

        # --- ANOMALY: Inconsistent unit_type formatting (~5%) ---
        unit = random.choice(UNIT_TYPES)
        if random.random() < 0.05:
            unit = random.choice([unit.lower(), f" {unit} "])

        room = f"Room {random.choice(['A', 'B', 'C'])}"
        bed = f"Bed {random.randint(1, 4)}"
        
        lines.append(
            f"{stay_id}|{output_a_id}|{doc_id}|{unit}|{room}|{bed}"
            f"|{entry_str}|{exit_str}|Continuous Monitoring Required"
        )
        stay_id += 1

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Wrote {OUTPUT_FILE} with {stay_id - 1} ICU stay records.")

if __name__ == "__main__":
    generate_icu_stays()