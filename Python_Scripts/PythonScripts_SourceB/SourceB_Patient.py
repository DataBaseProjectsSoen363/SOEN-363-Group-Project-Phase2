"""
Generate the PATIENT table for Source B (Continent B / CSV format).
Output: SourceB_Patient.csv

Differences from Source A:
  - CSV format (comma separated)
  - Primary key is a string "mrn" instead of integer "patient_id"
  - Date format: DD/MM/YYYY
  - Missing values use "N/A" instead of blank
  - Gender uses "M" / "F"
"""
import csv
import random
from datetime import datetime, timedelta

NUM_PATIENTS = 800
OUTPUT_FILE = "SourceB_Patient.csv"
SEED = 101

FIRST_NAMES = ["Lucas", "Mia", "Ethan", "Chloe", "Noah", "Ava", "Liam", "Zoe"]
LAST_NAMES = ["Dubois", "Lefebvre", "Moreau", "Laurent", "Simon", "Michel", "Leroy"]
CITIES = ["Paris", "Lyon", "Marseille", "Toulouse", "Nice"]

def generate_patients():
    random.seed(SEED)
    
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        
        # Headers for Source B
        writer.writerow(["mrn", "full_name", "insurance_id", "dob", "gender_cd", "contact_phone", "home_address"])
        
        for p_id in range(1, NUM_PATIENTS + 1):
            # Create a realistic Medical Record Number (String)
            mrn = f"MRN-{random.randint(10000, 99999)}"
            
            name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
            insurance = f"INS-{random.randint(100000, 999999)}"
            
            # Date formatting: DD/MM/YYYY
            dob_dt = datetime.now() - timedelta(days=random.randint(6500, 30000))
            dob_str = dob_dt.strftime("%d/%m/%Y")
            
            gender = random.choice(["M", "F"])
            
            # Missing value anomaly: Use "N/A" instead of blank
            phone = f"01-{random.randint(10, 99)}-{random.randint(10, 99)}-{random.randint(10, 99)}-{random.randint(10, 99)}"
            if random.random() < 0.05:
                phone = "N/A"
                
            address = f"{random.randint(1, 100)} Rue {random.choice(['de la Paix', 'Victor Hugo', 'Pasteur'])}, {random.choice(CITIES)}"
            
            # ANOMALY: Inconsistent casing on address (~5%)
            if random.random() < 0.05:
                address = address.lower()
                
            writer.writerow([mrn, name, insurance, dob_str, gender, phone, address])

    print(f"Wrote {OUTPUT_FILE} with {NUM_PATIENTS} patient records.")

if __name__ == "__main__":
    generate_patients()