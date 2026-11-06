"""
Generate the DISCHARGE_RECORD table for Source A (North America / TXT).
Output: SourceA_discharge_records.txt

Reads SourceA_admissions.txt to enforce 1:1 mapping for closed admissions.

Record layout (pipe-delimited):
  discharge_record_id | admission_id | discharge_date_time | discharge_destination 
  | condition_at_discharge | discharge_status | followup_instructions 
  | followup_appointments | responsible_physician

Anomalies injected (documented):
  - Temporal mismatch (~4%): record date differs from admission discharge date
  - Deceased condition mismatch (~3%): status 'Deceased' but condition 'Stable'
  - Missing follow-up (~10%): blank followup_appointments
  - Broken admission FK (~2%): admission_id = 9999
  - Inconsistent formatting (~5%): mixed case / whitespace on destinations
"""
import random
from datetime import datetime, timedelta

ADMISSIONS_FILE = "SourceA_admissions.txt"
OUTPUT_FILE = "SourceA_discharge_records.txt"
SEED = 333

PHYSICIAN_IDS = list(range(1, 16))     # professionals 1..15
DESTINATIONS = ["Home", "Rehab Facility", "Long-Term Care", "Transfer to Another Hospital"]
CONDITIONS = ["Stable", "Improved", "Fully Recovered", "Deceased"]
STATUSES = ["Discharged", "Deceased"]

def load_admissions(path=ADMISSIONS_FILE):
    """Returns a list of dicts with admission_id and discharge_dt."""
    admissions = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("---") or line.startswith("admission_id"):
                continue
            parts = line.split("|")
            try:
                a_id = int(parts[0])
                
                # Skip open admissions (no discharge date yet)
                if not parts[3]:
                    continue
                    
                discharge_dt = datetime.strptime(parts[3], "%Y-%m-%d %H:%M:%S")
                current_condition = parts[8]

                # Only use clean admissions as our baseline
                if a_id <= 1200:
                    admissions.append({
                        "admission_id": a_id,
                        "discharge_dt": discharge_dt,
                        "current_condition": current_condition
                    })
            except (ValueError, IndexError):
                continue
    return admissions

def generate_discharge_records():
    random.seed(SEED)
    admissions = load_admissions()

    lines = [
        "--- [DISCHARGE_RECORD] ---",
        "discharge_record_id|admission_id|discharge_date_time|discharge_destination"
        "|condition_at_discharge|discharge_status|followup_instructions"
        "|followup_appointments|responsible_physician"
    ]

    rec_id = 1
    for adm in admissions:
        a_id = adm["admission_id"]
        discharge_dt = adm["discharge_dt"]
        adm_condition = adm["current_condition"]

        doc_id = random.choice(PHYSICIAN_IDS)

        # --- ANOMALY: Temporal mismatch (~4%) ---
        output_dt = discharge_dt
        if random.random() < 0.04:
            output_dt = discharge_dt + timedelta(hours=random.choice([-12, 12, 24]))
        
        dt_str = output_dt.strftime("%Y-%m-%d %H:%M:%S")

        # --- ANOMALY: Broken admission FK (~2%) ---
        output_a_id = a_id
        if random.random() < 0.02:
            output_a_id = 9999

        # Determine status and condition
        if adm_condition == "Deceased":
            status = "Deceased"
            condition = "Deceased"
            dest = "Mortuary"
            followup_inst = "N/A"
            followup_appt = "N/A"
        else:
            status = "Discharged"
            
            # --- ANOMALY: Deceased condition mismatch (~3%) ---
            if random.random() < 0.03:
                status = "Deceased"
                condition = "Stable" # Logical mismatch!
                dest = "Mortuary"
            else:
                condition = random.choice(["Stable", "Improved", "Fully Recovered"])
                dest = random.choice(DESTINATIONS)

            followup_inst = "Follow up with primary care in 2 weeks."
            followup_appt = (discharge_dt + timedelta(days=14)).strftime("%Y-%m-%d")

            # --- ANOMALY: Missing follow-up (~10%) ---
            if random.random() < 0.10:
                followup_appt = ""

        # --- ANOMALY: Inconsistent formatting (~5%) ---
        if dest not in ["Mortuary", "N/A"] and random.random() < 0.05:
            dest = random.choice([dest.lower(), dest.upper(), f" {dest} "])

        lines.append(
            f"{rec_id}|{output_a_id}|{dt_str}|{dest}"
            f"|{condition}|{status}|{followup_inst}|{followup_appt}|{doc_id}"
        )
        rec_id += 1

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Wrote {OUTPUT_FILE} with {rec_id - 1} discharge record records.")

if __name__ == "__main__":
    generate_discharge_records()