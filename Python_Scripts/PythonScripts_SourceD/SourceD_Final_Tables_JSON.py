"""
Generate the final tables for Source D (Continent D / JSON format).
Output: SourceD_notes.json, SourceD_orders.json, SourceD_discharge.json
"""
import json
import random

NOTES_FILE = "SourceD_notes.json"
ORDERS_FILE = "SourceD_orders.json"
DISCHARGE_FILE = "SourceD_discharge.json"
SEED = 6666

def generate_final_tables():
    random.seed(SEED)
    
    notes_list = []
    orders_list = []
    discharge_list = []
    
    for v_id in range(1, 1201):
        base_ts = 1767225600 + (86400 * random.randint(0, 250))
        
        # ==========================================
        # CLINICAL NOTES (~90% of admissions)
        # ==========================================
        if random.random() < 0.90:
            note_text = "**Subjective:** Patient reports mild pain.\n**Objective:** Vitals stable.\n**Plan:** Continue monitoring."
            
            # --- ANOMALY: Missing note text (~3%) ---
            if random.random() < 0.03:
                note_text = None
                
            notes_list.append({
                "noteId": len(notes_list) + 1,
                "visitId": v_id,
                "authorId": random.randint(1, 15),
                "noteTimestamp": base_ts + 3600,
                "noteText": note_text
            })

        # ==========================================
        # ORDERS -> RADIOLOGY -> REPORTS (~25% of admissions)
        # ==========================================
        if random.random() < 0.25:
            order_ts = base_ts + (3600 * random.randint(1, 12))
            
            # Nested Report object
            report_obj = {
                "findings": random.choice(["Normal", "Mild opacity", "Clear"]),
                "conclusion": "No acute findings."
            }
            
            # --- ANOMALY: Missing report (~5%) ---
            if random.random() < 0.05:
                report_obj = None

            # Nested Exam object (contains the report)
            exam_obj = {
                "examTimestamp": order_ts + 7200,
                "technician": f"Tech_{random.randint(1, 10)}",
                "report": report_obj
            }

            # Parent Order object (contains the exam)
            order_record = {
                "orderId": len(orders_list) + 1,
                "visitId": v_id,
                "doctorId": random.randint(1, 15),
                "examType": random.choice(["X-Ray", "CT Scan", "MRI"]),
                "orderTimestamp": order_ts,
                "radiologyExam": exam_obj
            }
            orders_list.append(order_record)

        # ==========================================
        # DISCHARGE RECORDS
        # ==========================================
        # We assume ~95% of patients are discharged (5% still in hospital)
        if random.random() < 0.95:
            discharge_ts = base_ts + (86400 * random.randint(1, 10))
            
            discharge_list.append({
                "dischargeId": len(discharge_list) + 1,
                "visitId": v_id,
                "dischargeTimestamp": discharge_ts,
                "destination": random.choice(["HOME", "SNF", "REHAB"]),
                "condition": random.choice(["Stable", "Improved", "Critical"])
            })

    # Write all files
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(notes_list, f, indent=2)
    print(f"Wrote {NOTES_FILE} with {len(notes_list)} records.")

    with open(ORDERS_FILE, "w", encoding="utf-8") as f:
        json.dump(orders_list, f, indent=2)
    print(f"Wrote {ORDERS_FILE} with {len(orders_list)} records.")

    with open(DISCHARGE_FILE, "w", encoding="utf-8") as f:
        json.dump(discharge_list, f, indent=2)
    print(f"Wrote {DISCHARGE_FILE} with {len(discharge_list)} records.")

if __name__ == "__main__":
    generate_final_tables()
    print(" Source D (JSON) is complete! All 4 continents are generated.")