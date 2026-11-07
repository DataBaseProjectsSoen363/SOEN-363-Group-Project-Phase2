"""
Generate the COMBINED RADIOLOGY table for Source B (Continent B / CSV format).
Output: SourceB_Radiology.csv

Differences from Source A:
  - Examinations and Reports are combined into one file.
  - Uses boolean flags (Y/N) for "contrast_used".
  - Report findings are in French.
  - Date format: DD/MM/YYYY HH:MM
"""
import csv
import random
from datetime import datetime, timedelta

ORDERS_FILE = "SourceB_Diagnostic_Order.csv"
OUTPUT_FILE = "SourceB_Radiology.csv"
SEED = 909

TECHS = ["Tech A. Dupont", "Tech B. Martin", "Tech C. Bernard"]
FINDINGS = [
    "Aucune anomalie détectée.",
    "Légère opacité au lobe inférieur droit.",
    "Pas d'épanchement pleural.",
    "Fracture non déplacée visible."
]

def load_orders(path=ORDERS_FILE):
    valid_orders = []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["visit_id"] != "9999":
                try:
                    dt = datetime.strptime(row["order_datetime"], "%d/%m/%Y %H:%M")
                    valid_orders.append({
                        "order_id": int(row["order_id"]),
                        "exam_type": row["exam_type"],
                        "order_dt": dt
                    })
                except ValueError:
                    continue
    return valid_orders

def generate_radiology():
    random.seed(SEED)
    orders = load_orders()

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        
        # Custom headers (Combined Exam + Report)
        writer.writerow([
            "exam_id", "order_id", "technician_name", "scan_datetime", 
            "contrast_used", "findings_text", "radiologist_conclusion"
        ])
        
        exam_id = 1
        for order in orders:
            o_id = order["order_id"]
            exam_type = order["exam_type"]
            order_dt = order["order_dt"]

            # Scan happens 1-4 hours after order
            scan_dt = order_dt + timedelta(hours=random.randint(1, 4))
            scan_str = scan_dt.strftime("%d/%m/%Y %H:%M")

            # --- ANOMALY: Broken order FK (~2%) ---
            output_o_id = o_id
            if random.random() < 0.02:
                output_o_id = 9999

            tech = random.choice(TECHS)
            contrast = random.choice(["Y", "N"])
            
            findings = random.choice(FINDINGS)
            
            # --- ANOMALY: Missing findings/report (~5%) ---
            conclusion = "Normal." if "Aucune" in findings else "Corrélation clinique recommandée."
            if random.random() < 0.05:
                findings = ""
                conclusion = ""

            writer.writerow([
                exam_id, output_o_id, tech, scan_str, 
                contrast, findings, conclusion
            ])
            exam_id += 1

    print(f"Wrote {OUTPUT_FILE} with {exam_id - 1} combined radiology records.")

if __name__ == "__main__":
    generate_radiology()