"""
Generate the TRIAGE_ASSESSMENT table for Source D (Continent D / JSON format).
Output: SourceD_triage.json

Differences from A, B, C:
  - Vitals are grouped in a nested object
  - Symptoms are an array of strings
  - UNIX timestamps for dates
"""
import json
import random

OUTPUT_FILE = "SourceD_triage.json"
SEED = 4444
NUM_RECORDS = 1200

SYMPTOMS_POOL = ["Chest Pain", "Shortness of Breath", "Nausea", "Dizziness", "Fatigue"]
PRIORITIES = ["ESI-1", "ESI-2", "ESI-3", "ESI-4", "ESI-5"]

def generate_triage():
    random.seed(SEED)
    
    triage_list = []
    
    for t_id in range(1, NUM_RECORDS + 1):
        # --- ANOMALY: Broken visit FK (~2%) ---
        v_id = t_id
        if random.random() < 0.02:
            v_id = 9999
            
        # Select 1 to 3 random symptoms (array)
        num_symptoms = random.randint(1, 3)
        symptom_list = random.sample(SYMPTOMS_POOL, k=num_symptoms)
        
        hr = random.randint(60, 100)
        o2 = random.randint(95, 100)
        
        # --- ANOMALY: Out of bounds vitals (~3%) ---
        if random.random() < 0.03:
            hr = -99
            o2 = 0

        triage = {
            "triageId": t_id,
            "visitId": v_id,
            "nurseId": random.randint(16, 25),
            "vitals": {
                "heartRate": hr,
                "oxygenSaturation": o2,
                "bloodPressure": f"{random.randint(100, 140)}/{random.randint(60, 90)}"
            },
            "symptoms": symptom_list,
            "triagePriority": random.choice(PRIORITIES)
        }
        
        # --- ANOMALY: Missing nurse (~2%) ---
        if random.random() < 0.02:
            triage["nurseId"] = None

        triage_list.append(triage)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(triage_list, f, indent=2)
        
    print(f"Wrote {OUTPUT_FILE} with {NUM_RECORDS} triage records.")

if __name__ == "__main__":
    generate_triage()