import random
from datetime import datetime, timedelta

# ---- CONFIGURATION ----
NUM_RECORDS = 6500  # Target sizing between 5,000 and 10,000 records
OUTPUT_FILE = "source_b_europe.csv"

# ---- EUROPEAN CONSTANTS & MEDICAL CODES ----
ICD9_POOL = ["401.9", "410.9", "250.00", "272.4"]
FIRST_NAMES = ["Lucas", "Emma", "Louis", "Léa", "Gabriel", "Chloé", "Matteo", "Sofia", "Finn", "Anna"]
LAST_NAMES = ["Müller", "Dubois", "Rossi", "Martin", "Sanz", "De Jong", "Ivanov", "Hansen", "Zimmermann", "Ricci"]
CITIES = ["Paris", "Berlin", "Rome", "Amsterdam", "Madrid"]
STREETS = ["Rue de la Paix", "Hauptstraße", "Via Roma", "Prinsengracht", "Gran Via"]
UNIT_TYPES = ["ICU", "CCU", "MICU", "SICU"]

def generate_europe_csv():
    random.seed(101) # Unique seed for distinct variance
    lines = []
    
    # Intentionally reuse overlapping short local IDs starting at 1 to test ID management strategies
    patient_ids = list(range(1, 850))
    admission_ids = list(range(1, 1300))
    
    # --- 1. PATIENTS SECTION ---
    lines.append("--- [PATIENT] ---")
    lines.append("patient_id,name,health_insurance_number,life_status,address,date_birth,gender,emergency_contact_number,phone_number")
    for p_id in patient_ids:
        name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
        hin = f"EU-NAV{random.randint(100000, 999999)}"
        addr = f"{random.randint(10, 400)} {random.choice(STREETS)}, {random.choice(CITIES)}"
        dob = (datetime.now() - timedelta(days=random.randint(6000, 29000))).strftime("%Y-%m-%d")
        gender = random.choice(["Male", "Female"])
        phone = f"+33-555-{random.randint(1000, 9999)}"
        
        # Inject textual inconsistency anomaly: excessive spacing and chaotic casing
        if random.random() < 0.05:
            name = f"  {name.lower()}  "
        lines.append(f"{p_id},{name},{hin},Alive,\"{addr}\",{dob},{gender},{phone},{phone}")
        
    # --- 2. ADMISSIONS SECTION ---
    lines.append("\n--- [ADMISSION] ---")
    lines.append("admission_id,patient_id,admission_date_time,discharge_date_time,admission_type,admission_source,reason_admission,insurance_information,current_condition,admitting_professional_id")
    base_date = datetime(2026, 1, 1)
    for a_id in admission_ids:
        p_id = random.choice(patient_ids)
        doc_id = random.randint(1, 15)
        admit_dt = base_date + timedelta(days=random.randint(0, 250), hours=random.randint(0, 23))
        discharge_dt = admit_dt + timedelta(days=random.randint(1, 12))
        
        admit_str = admit_dt.strftime("%Y-%m-%d %H:%M:%S")
        discharge_str = discharge_dt.strftime("%Y-%m-%d %H:%M:%S")
        
        # Inject structural anomaly: Missing optional field or completely blank values
        if random.random() < 0.03:
            discharge_str = ""
        lines.append(f"{a_id},{p_id},{admit_str},{discharge_str},Urgent,Emergency Room,Chest Discomfort,National Health Insurance,Stable,{doc_id}")

    # --- 3. DIAGNOSIS SECTION ---
    lines.append("\n--- [DIAGNOSIS] ---")
    lines.append("diagnosis_id,patient_id,admission_id,icd9_code,diagnosis_date_time,primary_diagnosis,secondary_diagnosis,diagnosing_physician_id")
    for diag_id in range(1, 1600):
        a_id = random.choice(admission_ids)
        p_id = random.choice(patient_ids)
        code = random.choice(ICD9_POOL)
        diag_date = (base_date + timedelta(days=random.randint(0, 250))).strftime("%Y-%m-%d %H:%M:%S")
        doc_id = random.randint(1, 15)
        lines.append(f"{diag_id},{p_id},{a_id},{code},{diag_date},True,False,{doc_id}")

    # --- 4. TRIAGE ASSESSMENT SECTION ---
    lines.append("\n--- [TRIAGE_ASSESSMENT] ---")
    lines.append("triage_id,admission_id,nurse_id,blood_pressure,heart_rate,respiratory_rate,body_temperature,oxygen_saturation,pain_level,reported_symptoms,known_allergies,current_medications,triage_priority_level")
    for t_id in range(1, 1100):
        a_id = random.choice(admission_ids)
        nurse_id = random.randint(1, 10)
        hr = random.randint(60, 110)
        temp = round(random.uniform(36.0, 39.0), 1)
        
        # Inject invalid out-of-bounds numeric anomaly
        if random.random() < 0.04:
            temp = 12.5
        lines.append(f"{t_id},{a_id},{nurse_id},130/80,{hr},18,{temp},97,6,Shortness of Breath,None,None,Urgent")

    # --- 5. ICU STAY SECTION ---
    lines.append("\n--- [ICU_STAY] ---")
    lines.append("unit_stay_id,admission_id,responsible_physician_id,unit_type,room_number,bed_number,entry_date_time,exit_date_time,reason_transfer")
    for stay_id in range(1, 450):
        a_id = random.choice(admission_ids)
        doc_id = random.randint(1, 15)
        entry_dt = base_date + timedelta(days=random.randint(0, 240))
        # Inject chronological error anomaly: exit occurs prior to entry window
        if random.random() < 0.03:
            exit_dt = entry_dt - timedelta(days=3)
        else:
            exit_dt = entry_dt + timedelta(days=4)
        lines.append(f"{stay_id},{a_id},{doc_id},CCU,Ward 3B,Bed 12,{entry_dt.strftime('%Y-%m-%d %H:%M:%S')},{exit_dt.strftime('%Y-%m-%d %H:%M:%S')},Cardiac Monitoring")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
        
    print(f"Successfully generated Europe raw data file '{OUTPUT_FILE}' containing balanced relational tables.")

if __name__ == "__main__":
    generate_europe_csv()
