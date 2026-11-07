"""
Generate the DIAGNOSTIC_ORDER table for Source B (Continent B / CSV format).
Output: SourceB_Diagnostic_Order.csv

Differences from Source A:
  - Numeric priority (1-4) instead of text (STAT/Routine)
  - Date format: DD/MM/YYYY HH:MM
  - Inconsistent status casing (~5%)
"""
import csv
import random
from datetime import datetime, timedelta

ADMISSIONS_FILE = "SourceB_Admission.csv"
OUTPUT_FILE = "SourceB_Diagnostic_Order.csv"
SEED = 808

DOCTOR_MRNS = [f"MRN-{10000 + i}" for i in range(1, 16)]
EXAMS = ["X-Ray Thorax", "CT Scan Thorax", "Echographie Abdominale", "IRM Cerveau"]
PRIORITIES = ["1", "2", "3", "4"]  # 1 is highest, 4 is lowest
STATUSES = ["Completed", "Pending", "Cancelled"]

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

def generate_orders():
    random.seed(SEED)
    admissions = load_admissions()

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        
        # Custom headers
        writer.writerow([
            "order_id", "visit_id", "doctor_mrn", 
            "exam_type", "order_datetime", "priority_level", "order_status"
        ])
        
        order_id = 1
        # Orders happen in ~25% of admissions
        for adm in admissions:
            if random.random() > 0.25:
                continue
                
            v_id = adm["visit_id"]
            admit_dt = adm["admit_dt"]
            doctor_mrn = random.choice(DOCTOR_MRNS)

            exam = random.choice(EXAMS)
            
            # Order happens 1-12 hours after admission
            order_dt = admit_dt + timedelta(hours=random.randint(1, 12))
            order_str = order_dt.strftime("%d/%m/%Y %H:%M")

            # --- ANOMALY: Broken visit FK (~2%) ---
            output_v_id = v_id
            if random.random() < 0.02:
                output_v_id = 9999

            priority = random.choice(PRIORITIES)
            
            status = random.choice(STATUSES)
            # --- ANOMALY: Inconsistent status casing (~5%) ---
            if random.random() < 0.05:
                status = random.choice([status.lower(), status.upper()])

            # --- ANOMALY: Missing status (~3%) ---
            if random.random() < 0.03:
                status = ""

            writer.writerow([
                order_id, output_v_id, doctor_mrn, 
                exam, order_str, priority, status
            ])
            order_id += 1

    print(f"Wrote {OUTPUT_FILE} with {order_id - 1} diagnostic orders.")

if __name__ == "__main__":
    generate_orders()