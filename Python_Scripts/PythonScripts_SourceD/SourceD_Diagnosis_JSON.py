import json
import random

FILE_NAME = "SourceD_admissions.json"
SEED = 3333
ICD9_CODES = ["401.9", "410.9", "250.00", "272.4"]

def generate_diagnoses():
    random.seed(SEED)
    
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        admissions = json.load(f)
        
    for adm in admissions:
        # Default all diagnosis fields to None so the keys always exist
        adm["diagnosis_codes"] = None
        adm["primary_diagnosis"] = None
        adm["diagnosis_timestamp"] = None
        
        # ~90% of admissions get diagnoses
        if random.random() > 0.90:
            continue
            
        num_diags = random.randint(1, 3)
        codes = random.sample(ICD9_CODES, k=num_diags)
        
        # Flatten the list to a single string
        adm["diagnosis_codes"] = ", ".join(codes)
        adm["primary_diagnosis"] = codes[0]
        
        if random.random() > 0.02:
            admit_ts = adm["admitTimestamp"]
            adm["diagnosis_timestamp"] = admit_ts + (3600 * random.randint(1, 12))

    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(admissions, f, indent=2)
        
    print(f"Added flattened diagnoses to {FILE_NAME}.")

if __name__ == "__main__":
    generate_diagnoses()