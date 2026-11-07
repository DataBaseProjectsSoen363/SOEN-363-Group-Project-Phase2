"""
Generate the DIAGNOSIS data for Source D (Continent D / JSON format).
Output: SourceD_admissions.json (Updated with nested diagnoses)

Differences from A, B, C:
  - Diagnoses are nested arrays inside the Admission object
  - Uses true/false booleans
  - No explicit patientId (inherited from the parent admission)
"""
import json
import random

FILE_NAME = "SourceD_admissions.json"
SEED = 3333
ICD9_CODES = ["401.9", "410.9", "250.00", "272.4"]

def generate_diagnoses():
    random.seed(SEED)
    
    # 1. Read the existing admissions JSON
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        admissions = json.load(f)
        
    # 2. Iterate through and add diagnoses
    for adm in admissions:
        # ~90% of admissions get diagnoses
        if random.random() > 0.90:
            continue
            
        num_diags = random.randint(1, 3)
        codes = random.sample(ICD9_CODES, k=num_diags)
        
        diagnoses_list = []
        for i, code in enumerate(codes):
            diag = {
                "icd9Code": code,
                "isPrimary": True if i == 0 else False,
                "doctorId": random.randint(1, 15)
            }
            
            # --- ANOMALY: Missing diagnosis date (~2%) ---
            # We'll calculate a timestamp a few hours after admission
            if random.random() > 0.02:
                admit_ts = adm["admitTimestamp"]
                diag_ts = admit_ts + (3600 * random.randint(1, 12))
                diag["diagnosisTimestamp"] = diag_ts
                
            diagnoses_list.append(diag)
            
        # Attach the array to the admission object
        adm["diagnoses"] = diagnoses_list

    # 3. Save back to file
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(admissions, f, indent=2)
        
    print(f"Added nested diagnoses to {FILE_NAME}.")

if __name__ == "__main__":
    generate_diagnoses()