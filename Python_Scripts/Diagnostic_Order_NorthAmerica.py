"""
Generate the DIAGNOSTIC_ORDER table for Source A (North America / TXT).
Output: SourceA_diagnostic_orders.txt

Reads SourceA_admissions.txt to enforce strict patient consistency
and detect chronological errors against admission/discharge dates.

Record layout (pipe-delimited):
  order_id | admission_id | patient_id | requesting_physician_id 
  | requested_examination | request_date_time | clinical_reason_examination 
  | priority | order_status

Anomalies injected (documented):
  - Wrong-patient anomaly (~2%): patient_id != admission.patient_id
  - Missing order_status (~3%): blank value
  - Broken admission FK (~2%): admission_id = 9999
  - Inconsistent priority formatting (~5%): mixed case / spaces
  - Temporal error (~3%): request time before admission or after discharge
"""
import random
from datetime import datetime, timedelta

ADMISSIONS_FILE = "SourceA_admissions.txt"
OUTPUT_FILE = "SourceA_diagnostic_orders.txt"
SEED = 999

PHYSICIAN_IDS = list(range(1, 16))     # professionals 1..15
EXAMS = ["Chest X-Ray", "CT Scan - Chest", "Abdominal Ultrasound", "MRI Brain"]
PRIORITIES = ["Routine", "Urgent", "STAT"]
STATUSES = ["Completed", "Pending", "Cancelled"]

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

def generate_diagnostic_orders():
    random.seed(SEED)
    admissions = load_admissions()

    lines = [
        "--- [DIAGNOSTIC_ORDER] ---",
        "order_id|admission_id|patient_id|requesting_physician_id"
        "|requested_examination|request_date_time|clinical_reason_examination"
        "|priority|order_status"
    ]

    order_id = 1
    # Only generate orders for ~25% of admissions
    for adm in admissions:
        if random.random() > 0.25:
            continue

        a_id = adm["admission_id"]
        true_p_id = adm["patient_id"]
        admit_dt = adm["admit_dt"]
        discharge_dt = adm["discharge_dt"]

        doc_id = random.choice(PHYSICIAN_IDS)
        exam = random.choice(EXAMS)
        
        # Order typically placed 1-12 hours after admission
        req_dt = admit_dt + timedelta(hours=random.randint(1, 12))

        # --- ANOMALY: Temporal error (~3%) ---
        if random.random() < 0.03:
            if random.random() < 0.5:
                req_dt = admit_dt - timedelta(hours=5) # Before admission
            elif discharge_dt:
                req_dt = discharge_dt + timedelta(hours=5) # After discharge

        req_str = req_dt.strftime("%Y-%m-%d %H:%M:%S")

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

        # --- ANOMALY: Inconsistent priority (~5%) ---
        priority = random.choice(PRIORITIES)
        if random.random() < 0.05:
            priority = random.choice([priority.lower(), priority.upper(), f" {priority} "])

        # --- ANOMALY: Missing order status (~3%) ---
        status = random.choice(STATUSES)
        if random.random() < 0.03:
            status = ""

        reason = "Rule out pulmonary embolism." if exam == "CT Scan - Chest" else "Evaluate for acute pathology."

        lines.append(
            f"{order_id}|{output_a_id}|{output_p_id}|{doc_id}"
            f"|{exam}|{req_str}|{reason}|{priority}|{status}"
        )
        order_id += 1

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Wrote {OUTPUT_FILE} with {order_id - 1} diagnostic order records.")

if __name__ == "__main__":
    generate_diagnostic_orders()