"""
Generate the ICU_STAY and SURGICAL_PROCEDURE tables for Source D (JSON format).
Output: SourceD_icu.json and SourceD_surgery.json
"""
import json
import random

ICU_FILE = "SourceD_icu.json"
SURGERY_FILE = "SourceD_surgery.json"
SEED = 5555

def generate_icu_and_surgery():
    random.seed(SEED)
    
    icu_list = []
    surgery_list = []
    
    # Simulating only generating them for valid visits (1 to 1200)
    for v_id in range(1, 1201):
        
        # ==========================================
        # ICU STAYS (~30% of admissions)
        # ==========================================
        if random.random() < 0.30:
            # Base admit timestamp (approx Jan 1 2026) + some random days
            admit_ts = 1767225600 + (86400 * random.randint(0, 250))
            entry_ts = admit_ts + (3600 * random.randint(1, 24))
            exit_ts = entry_ts + (86400 * random.randint(1, 7))
            
            # --- ANOMALY: Chronological error (~3%) ---
            if random.random() < 0.03:
                exit_ts = entry_ts - (3600 * 5)
                
            # --- ANOMALY: Missing Exit Date (~5%) ---
            if random.random() < 0.05:
                exit_ts = None
                
            # --- ANOMALY: Broken FK (~2%) ---
            output_v_id = v_id
            if random.random() < 0.02:
                output_v_id = 9999

            icu_record = {
                "stayId": len(icu_list) + 1,
                "visitId": output_v_id,
                "wardType": random.choice(["ICU", "CCU", "MICU", "SICU"]),
                "doctorId": random.randint(1, 15),
                "entryTimestamp": entry_ts,
                "exitTimestamp": exit_ts
            }
            icu_list.append(icu_record)

        # ==========================================
        # SURGERIES (~20% of admissions)
        # ==========================================
        if random.random() < 0.20:
            admit_ts = 1767225600 + (86400 * random.randint(0, 250))
            surg_ts = admit_ts + (86400 * random.randint(1, 3))
            
            # --- ANOMALY: Broken FK (~2%) ---
            output_v_id = v_id
            if random.random() < 0.02:
                output_v_id = 9999

            surgery_record = {
                "surgeryId": len(surgery_list) + 1,
                "visitId": output_v_id,
                "procedureCode": random.choice(["PROC-APP", "PROC-CHOL", "PROC-CABG"]),
                "surgeonId": random.randint(1, 15),
                "surgeryTimestamp": surg_ts
            }
            surgery_list.append(surgery_record)

    # Write ICU JSON
    with open(ICU_FILE, "w", encoding="utf-8") as f:
        json.dump(icu_list, f, indent=2)
    print(f"Wrote {ICU_FILE} with {len(icu_list)} records.")

    # Write Surgery JSON
    with open(SURGERY_FILE, "w", encoding="utf-8") as f:
        json.dump(surgery_list, f, indent=2)
    print(f"Wrote {SURGERY_FILE} with {len(surgery_list)} records.")

if __name__ == "__main__":
    generate_icu_and_surgery()