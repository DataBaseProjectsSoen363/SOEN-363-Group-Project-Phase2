import random
import json
from datetime import datetime, timedelta

# ---- CONFIGURATION ----
OUTPUT_FILE = "source_d_africa.json"

# ---- AFRICAN LOOKUPS & CORE VALUES ----
ICD9_POOL = ["401.9", "410.9", "250.00", "272.4"]
FIRST_NAMES = ["Kofi", "Amina", "Kwame", "Zola", "Sadio", "Fatoumata", "Amara", "Tendai", "Chinedu", "Imane"]
LAST_NAMES = ["Mensah", "Diallo", "Traoré", "Bekker", "Osei", "Baloyi", "Keita", "Ndiaye", "Obi", "Toure"]
CITIES = ["Abidjan", "Nairobi", "Johannesburg", "Dakar", "Casablanca"]
STREETS = ["Boulevard de la République", "Harambee Avenue", "Vilakazi St", "Avenue Cheikh Anta Diop", "Rue Zerktouni"]
UNIT_TYPES = ["ICU", "CCU", "MICU", "SICU"]

def generate_africa_json():
    random.seed(303) # Unique seed for distinct variation
    
    patient_ids = list(range(1, 800))
    admission_ids = list(range(1, 1200))
    
    data_store = {
        "metadata": {
            "continent": "Africa",
            "source": "Source_D",
            "generation_date": datetime.now().strftime("%Y-%m-%d")
        },
        "patients": [],
        "admissions": [],
        "diagnoses": [],
        "triage_assessments": []
    }
    
    # --- 1. PATIENTS SECTION ---
    for p_id in patient_ids:
        addr = f"{random.randint(5, 500)} {random.choice(STREETS)}, {random.choice(CITIES)}"
        
        # Inject structural anomaly: irregular whitespace padding (approx 5% rate)
        if random.random() < 0.05:
            addr = f"     {addr}     "
            
        patient = {
            "patient_id": p_id,
            "name": f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}",
            "health_insurance_number": f"AF-INS{random.randint(100000, 999999)}",
            "life_status": "Alive",
            "address": addr,
            "date_birth": (datetime.now() - timedelta(days=random.randint(6500, 29500))).strftime("%Y-%m-%d"),
            "gender": random.choice(["Male", "Female"]),
            "phone_number": f"+225-{random.randint(10, 99)}-{random.randint(1000, 9999)}"
        }
        data_store["patients"].append(patient)
        
    # --- 2. ADMISSIONS SECTION ---
    base_date = datetime(2026, 1, 1)
    for a_id in admission_ids:
        admit_dt = base_date + timedelta(days=random.randint(0, 250), hours=random.randint(0, 23))
        discharge_dt = admit_dt + timedelta(days=random.randint(1, 11))
        
        admission = {
            "admission_id": a_id,
            "patient_id": random.choice(patient_ids),
            "admission_date_time": admit_dt.strftime("%Y-%m-%d %H:%M:%S"),
            "discharge_date_time": discharge_dt.strftime("%Y-%m-%d %H:%M:%S"),
            "admission_type": "Emergency",
            "admission_source": "Emergency Room",
            "reason_admission": "Acute Respiratory Distress",
            "current_condition": "Stable",
            "admitting_professional_id": random.randint(1, 15)
        }
        
        # Inject structural anomaly: drop key entirely to test for null pointer safety
        if random.random() < 0.04:
            del admission["discharge_date_time"]
            
        data_store["admissions"].append(admission)

    # --- 3. DIAGNOSIS SECTION ---
    for diag_id in range(1, 1500):
        diagnosis = {
            "diagnosis_id": diag_id,
            "admission_id": random.choice(admission_ids),
            "icd9_code": random.choice(ICD9_POOL),
            "primary_diagnosis": True
        }
        data_store["diagnoses"].append(diagnosis)

    # --- 4. TRIAGE ASSESSMENT SECTION ---
    for t_id in range(1, 1200):
        triage = {
            "triage_id": t_id,
            "admission_id": random.choice(admission_ids),
            "heart_rate": random.randint(60, 110),
            "body_temperature": 37.0,
            "triage_priority_level": "Urgent"
        }
        data_store["triage_assessments"].append(triage)

    # Save out file into pretty formatted JSON structure
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data_store, f, indent=4, ensure_ascii=False)
        
    print(f"Success! Generated African JSON dataset file '{OUTPUT_FILE}' with nested sub-arrays.")

if __name__ == "__main__":
    generate_africa_json()
