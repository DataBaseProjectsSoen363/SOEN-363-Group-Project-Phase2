"""
Generate the ADMISSION table for Source D (Continent D / JSON format).
Output: SourceD_admissions.json

Differences from A, B, C:
  - JSON array of objects
  - UNIX timestamps for dates
  - Missing keys instead of nulls for open admissions
"""
import json
import random
from datetime import datetime, timedelta, timezone

OUTPUT_FILE = "SourceD_admissions.json"
SEED = 2222
NUM_ADMISSIONS = 1200

def generate_admissions():
    random.seed(SEED)
    
    admissions_list = []
    
    # Base date: Jan 1, 2026 in UTC
    base_dt = datetime(2026, 1, 1, tzinfo=timezone.utc)
    
    for a_id in range(1, NUM_ADMISSIONS + 1):
        # --- ANOMALY: Broken patient FK (~2%) ---
        p_id = random.randint(1, 800)
        if random.random() < 0.02:
            p_id = 9999
            
        admit_dt = base_dt + timedelta(days=random.randint(0, 250), hours=random.randint(0, 23))
        discharge_dt = admit_dt + timedelta(days=random.randint(1, 10))
        
        # Convert to UNIX timestamps (integers)
        admit_ts = int(admit_dt.timestamp())
        discharge_ts = int(discharge_dt.timestamp())
        
        admission = {
            "visitId": a_id,
            "patientId": p_id,
            "admitTimestamp": admit_ts,
            "admissionType": random.choice(["EMERGENCY", "ELECTIVE", "URGENT"]),
            "reason": random.choice(["Chest Pain", "Shortness of Breath", "Fever"]),
            "doctorId": random.randint(1, 15)
        }
        
        # --- ANOMALY: Missing Discharge Date (~3%) ---
        # We simply don't add the key at all
        if random.random() > 0.03:
            admission["dischargeTimestamp"] = discharge_ts
            
            # --- ANOMALY: Chronological error (~2%) ---
            if random.random() < 0.02:
                admission["dischargeTimestamp"] = admit_ts - (86400 * 2) # 2 days before admit
                
        admissions_list.append(admission)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(admissions_list, f, indent=2)
        
    print(f"Wrote {OUTPUT_FILE} with {NUM_ADMISSIONS} admission records.")

if __name__ == "__main__":
    generate_admissions()