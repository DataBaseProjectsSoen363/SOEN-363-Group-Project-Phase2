"""
Generate the RADIOLOGY_EXAMINATION table for Source A (North America / TXT).
Output: SourceA_radiology_examinations.txt

Reads SourceA_diagnostic_orders.txt to ensure every exam is linked to
a real order. Links to physicians (IDs 1-15).

Record layout (pipe-delimited):
  examination_id | order_id | examination_type | examination_date_time 
  | body_area_examined | referring_physician_id | radiology_technician 
  | examination_status | medical_images

Anomalies injected (documented):
  - Missing body area (~4%): blank body_area_examined
  - Inconsistent status formatting (~5%): mixed case / spaces
  - Broken order FK (~2%): order_id = 9999
  - Missing medical images (~3%): blank DICOM link
"""
import random
from datetime import datetime, timedelta

ORDERS_FILE = "SourceA_diagnostic_orders.txt"
OUTPUT_FILE = "SourceA_radiology_examinations.txt"
SEED = 111

TECHS = ["Tech A. Roy", "Tech B. Gagnon", "Tech C. Smith", "Tech D. Tremblay"]
STATUSES = ["Finalized", "Pending", "In Progress"]

def load_orders(path=ORDERS_FILE):
    """Returns a list of dicts with order_id, exam_type, and request_dt."""
    orders = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("---") or line.startswith("order_id"):
                continue
            parts = line.split("|")
            try:
                o_id = int(parts[0])
                # We only want to create exams for orders that actually exist in our clean baseline
                if o_id <= 1200:
                    exam_type = parts[4]
                    req_dt = datetime.strptime(parts[5], "%Y-%m-%d %H:%M:%S")
                    orders.append({
                        "order_id": o_id,
                        "exam_type": exam_type,
                        "request_dt": req_dt
                    })
            except (ValueError, IndexError):
                continue
    return orders

def generate_radiology_exams():
    random.seed(SEED)
    orders = load_orders()

    lines = [
        "--- [RADIOLOGY_EXAMINATION] ---",
        "examination_id|order_id|examination_type|examination_date_time"
        "|body_area_examined|referring_physician_id|radiology_technician"
        "|examination_status|medical_images"
    ]

    exam_id = 1
    for order in orders:
        o_id = order["order_id"]
        exam_type = order["exam_type"]
        
        # Exam happens 1-4 hours after the order is placed
        exam_dt = order["request_dt"] + timedelta(hours=random.randint(1, 4))
        exam_str = exam_dt.strftime("%Y-%m-%d %H:%M:%S")

        # --- ANOMALY: Broken order FK (~2%) ---
        output_o_id = o_id
        if random.random() < 0.02:
            output_o_id = 9999

        # Pick a referring physician (in a real system, this should match the order's physician)
        doc_id = random.randint(1, 15)

        # Infer body area from exam type
        if "Chest" in exam_type:
            body_area = "Chest"
        elif "Abdominal" in exam_type:
            body_area = "Abdomen"
        elif "Brain" in exam_type:
            body_area = "Head"
        else:
            body_area = "Unspecified"

        # --- ANOMALY: Missing body area (~4%) ---
        if random.random() < 0.04:
            body_area = ""

        # --- ANOMALY: Inconsistent status formatting (~5%) ---
        status = random.choice(STATUSES)
        if random.random() < 0.05:
            status = random.choice([status.lower(), status.upper(), f" {status} "])

        # --- ANOMALY: Missing medical images (~3%) ---
        dicom_link = f"DICOM-{random.randint(1000, 9999)}"
        if random.random() < 0.03:
            dicom_link = ""

        tech = random.choice(TECHS)

        lines.append(
            f"{exam_id}|{output_o_id}|{exam_type}|{exam_str}"
            f"|{body_area}|{doc_id}|{tech}|{status}|{dicom_link}"
        )
        exam_id += 1

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Wrote {OUTPUT_FILE} with {exam_id - 1} radiology exam records.")

if __name__ == "__main__":
    generate_radiology_exams()