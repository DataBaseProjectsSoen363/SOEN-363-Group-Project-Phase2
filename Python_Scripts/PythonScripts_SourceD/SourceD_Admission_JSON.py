import json
import random
from datetime import datetime, timedelta, timezone

OUTPUT_FILE = "SourceD_admissions.json"
SEED = 2222
NUM_ADMISSIONS = 1200

def generate_admissions():
    random.seed(SEED)
    
    admissions_list = []
    base_dt = datetime(2026, 1, 1, tzinfo=timezone.utc)
    
    for a_id in range(1, NUM_ADMISSIONS + 1):
        p_id = random.randint(1, 800)
        if random.random() < 0.02:
            p_id = 9999
            
        admit_dt = base_dt + timedelta(days=random.randint(0, 250), hours=random.randint(0, 23))
        discharge_dt = admit_dt + timedelta(days=random.randint(1, 10))
        
        admit_ts = int(admit_dt.timestamp())
        discharge_ts = int(discharge_dt.timestamp())
        
        admission = {
            "visitId": a_id,
            "patientId": p_id,
            "admitTimestamp": admit_ts,
            "admissionType": random.choice(["EMERGENCY", "ELECTIVE", "URGENT"]),
            "reason": random.choice(["Chest Pain", "Shortness of Breath", "Fever"]),
            "doctorId": random.randint(1, 15),
            "dischargeTimestamp": None  # Default to None (JSON null)
        }
        
        if random.random() > 0.03:
            admission["dischargeTimestamp"] = discharge_ts
            if random.random() < 0.02:
                admission["dischargeTimestamp"] = admit_ts - (86400 * 2)
                
        admissions_list.append(admission)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(admissions_list, f, indent=2)
        
    print(f"Wrote {OUTPUT_FILE} with {NUM_ADMISSIONS} admission records.")

if __name__ == "__main__":
    generate_admissions()