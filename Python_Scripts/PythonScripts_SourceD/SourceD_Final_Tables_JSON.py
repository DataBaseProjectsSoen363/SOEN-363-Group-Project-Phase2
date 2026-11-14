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
        
        # CLINICAL NOTES
        if random.random() < 0.90:
            note_text = "**Subjective:** Patient reports mild pain.\n**Objective:** Vitals stable.\n**Plan:** Continue monitoring."
            if random.random() < 0.03:
                note_text = None
                
            notes_list.append({
                "noteId": len(notes_list) + 1,
                "visitId": v_id,
                "authorId": random.randint(1, 15),
                "noteTimestamp": base_ts + 3600,
                "noteText": note_text
            })

        # ORDERS (Flattened)
        if random.random() < 0.25:
            order_ts = base_ts + (3600 * random.randint(1, 12))
            
            findings = random.choice(["Normal", "Mild opacity", "Clear"])
            conclusion = "No acute findings."
            
            if random.random() < 0.05:
                findings = None
                conclusion = None

            order_record = {
                "orderId": len(orders_list) + 1,
                "visitId": v_id,
                "doctorId": random.randint(1, 15),
                "examType": random.choice(["X-Ray", "CT Scan", "MRI"]),
                "orderTimestamp": order_ts,
                "examTimestamp": order_ts + 7200,
                "technician": f"Tech_{random.randint(1, 10)}",
                "report_findings": findings,
                "report_conclusion": conclusion
            }
            orders_list.append(order_record)

        # DISCHARGE RECORDS
        if random.random() < 0.95:
            discharge_ts = base_ts + (86400 * random.randint(1, 10))
            discharge_list.append({
                "dischargeId": len(discharge_list) + 1,
                "visitId": v_id,
                "dischargeTimestamp": discharge_ts,
                "destination": random.choice(["HOME", "SNF", "REHAB"]),
                "condition": random.choice(["Stable", "Improved", "Critical"])
            })

    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(notes_list, f, indent=2)
    with open(ORDERS_FILE, "w", encoding="utf-8") as f:
        json.dump(orders_list, f, indent=2)
    with open(DISCHARGE_FILE, "w", encoding="utf-8") as f:
        json.dump(discharge_list, f, indent=2)
        
    print(f"Wrote {NOTES_FILE}, {ORDERS_FILE}, and {DISCHARGE_FILE}.")

if __name__ == "__main__":
    generate_final_tables()