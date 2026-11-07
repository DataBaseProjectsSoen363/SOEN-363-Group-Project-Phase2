"""
Generate the PATIENT table for Source D (Continent D / JSON format).
Output: SourceD_patients.json

Differences from A, B, C:
  - JSON array of objects
  - Nested objects for names {"first": "...", "last": "..."}
  - UNIX timestamps for dates (e.g., 1735689600)
  - camelCase keys (e.g., "patientId")
"""
import json
import random
import time
from datetime import datetime, timedelta
from datetime import datetime, timedelta, timezone

OUTPUT_FILE = "SourceD_patients.json"
SEED = 1111
NUM_PATIENTS = 800

FIRST_NAMES = ["Yuki", "Haruto", "Sakura", "Aoi", "Ren", "Hina", "Sota", "Yui"]
LAST_NAMES = ["Tanaka", "Sato", "Suzuki", "Takahashi", "Watanabe", "Ito"]
CITIES = ["Tokyo", "Osaka", "Kyoto", "Nagoya", "Sapporo"]

def generate_patients():
    random.seed(SEED)
    
    patients_list = []
    
    for p_id in range(1, NUM_PATIENTS + 1):
        # Calculate UNIX timestamp (seconds) for date of birth
        dob_dt = datetime.now() - timedelta(days=random.randint(6500, 30000))
        dob_timestamp = int(dob_dt.replace(tzinfo=timezone.utc).timestamp())
        
        # --- ANOMALY: Missing phone (~5%) ---
        phone = f"+81-{random.randint(80, 90)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
        if random.random() < 0.05:
            phone = None  # JSON null
            
        patient = {
            "patientId": p_id,
            "name": {
                "first": random.choice(FIRST_NAMES),
                "last": random.choice(LAST_NAMES)
            },
            "dobTimestamp": dob_timestamp,
            "gender": random.choice(["M", "F"]),
            "contact": {
                "phone": phone,
                "city": random.choice(CITIES)
            }
        }
        patients_list.append(patient)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        # indent=2 makes it human-readable
        json.dump(patients_list, f, indent=2)
        
    print(f"Wrote {OUTPUT_FILE} with {NUM_PATIENTS} patient records.")

if __name__ == "__main__":
    generate_patients()