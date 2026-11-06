import random
import uuid
from datetime import datetime, timedelta

# ---- CONFIGURATION ----
NUM_RECORDS = 6000  # Sets target size between 5,000 and 10,000 records
OUTPUT_FILE = "source_a_north_america.txt"

# ---- LOOKUPS & MATPLOTLIB DICTIONARY CONSTANTS ----
ICD9_POOL = [
    ("401.9", "Unspecified essential hypertension", "Circulatory System"),
    ("410.9", "Acute myocardial infarction", "Circulatory System"),
    ("250.00", "Diabetes mellitus without complication", "Endocrine/Metabolic"),
    ("272.4", "Other and unspecified hyperlipidemia", "Endocrine/Metabolic")
]
FIRST_NAMES = ["Daniel", "Sarah", "John", "Emily", "Michael", "Amelie", "David", "Jessica", "Robert", "Rachel"]
LAST_NAMES = ["Tremblay", "Smith", "Roy", "Gagnon", "Jones", "Williams", "Brown", "Charette", "Taylor", "Miller"]
CITIES = ["Montreal", "Laval", "Longueuil", "Sherbrooke", "Quebec City"]
STREETS = ["Sherbrooke St", "Sainte-Catherine St", "Papineau Ave", "Guy St", "Atwater Ave"]
UNIT_TYPES = ["ICU", "CCU", "MICU", "SICU"]
EXAM_TYPES = ["Chest X-Ray", "CT Scan - Chest", "Abdominal Ultrasound", "MRI Brain"]
SPECIALTIES = ["Cardiology", "Internal Medicine", "Emergency Medicine", "Pulmonology", "General Surgery"]
ALLERGIES = ["None", "Penicillin", "Sulfa drugs", "Latex", "Peanuts"]
MEDS = ["None", "Metformin", "Atorvastatin", "Lisinopril", "Aspirin", "Metoprolol"]
PRIORITIES = ["Routine", "Urgent", "STAT"]

def generate_data():
    random.seed(42)
    lines = []
    
    # Track generated primary keys locally to link dependent records properly
    patient_ids = list(range(1, 800))
    admission_ids = list(range(1, 1200))
    
    # --- 1. PATIENTS SECTION ---
    lines.append("--- [PATIENT] ---")
    lines.append("patient_id|name|health_insurance_number|life_status|address|date_birth|gender|emergency_contact_number|phone_number")
    
    for p_id in patient_ids:
        name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
        hin = f"RAMQ{random.randint(100000, 999999)}"
        addr = f"{random.randint(100, 5000)} {random.choice(STREETS)}, {random.choice(CITIES)}"
        dob = (datetime.now() - timedelta(days=random.randint(6500, 30000))).strftime("%Y-%m-%d")
        gender = random.choice(["Male", "Female"])
        phone = f"514-555-{random.randint(1000, 9999)}"
        
        # Inject structural anomaly: Inconsistent text capitalization or padding (approx 5% rate)
        if random.random() < 0.05:
            addr = f"   {addr.upper()}   "
            
        lines.append(f"{p_id}|{name}|{hin}|Alive|{addr}|{dob}|{gender}|{phone}|{phone}")
        
    # --- 2. ADMISSIONS SECTION ---
    lines.append("\n--- [ADMISSION] ---")
    lines.append("admission_id|patient_id|admission_date_time|discharge_date_time|admission_type|admission_source|reason_admission|insurance_information|current_condition|admitting_professional_id")
    
    base_date = datetime(2026, 1, 1)
    
    for a_id in admission_ids:
        p_id = random.choice(patient_ids)
        doc_id = random.randint(1, 15)
        
        admit_dt = base_date + timedelta(days=random.randint(0, 250), hours=random.randint(0, 23))
        discharge_dt = admit_dt + timedelta(days=random.randint(1, 10))
        
        admit_str = admit_dt.strftime("%Y-%m-%d %H:%M:%S")
        discharge_str = discharge_dt.strftime("%Y-%m-%d %H:%M:%S")
        
        # Inject structural anomaly: Chronological error (Discharge before admission)
        if random.random() < 0.02:
            discharge_str = (admit_dt - timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")
            
        # Inject structural anomaly: Missing values on required fields
        if random.random() < 0.02:
            discharge_str = ""
            
        lines.append(f"{a_id}|{p_id}|{admit_str}|{discharge_str}|Emergency|Emergency Room|Chest Pain|Private Insurance|Stable|{doc_id}")

    # --- 3. DIAGNOSIS SECTION ---
    lines.append("\n--- [DIAGNOSIS] ---")
    lines.append("diagnosis_id|patient_id|admission_id|icd9_code|diagnosis_date_time|primary_diagnosis|secondary_diagnosis|diagnosing_physician_id")
    
    for diag_id in range(1, 1500):
        a_id = random.choice(admission_ids)
        p_id = random.choice(patient_ids)
        code = random.choice(ICD9_POOL)[0]
        diag_date = (base_date + timedelta(days=random.randint(0, 250))).strftime("%Y-%m-%d %H:%M:%S")
        doc_id = random.randint(1, 15)
        
        lines.append(f"{diag_id}|{p_id}|{a_id}|{code}|{diag_date}|True|False|{doc_id}")

    # --- 4. TRIAGE ASSESSMENT SECTION ---
    lines.append("\n--- [TRIAGE_ASSESSMENT] ---")
    lines.append("triage_id|admission_id|nurse_id|blood_pressure|heart_rate|respiratory_rate|body_temperature|oxygen_saturation|pain_level|reported_symptoms|known_allergies|current_medications|triage_priority_level")
    
    for t_id in range(1, 1200):
        a_id = random.choice(admission_ids)
        nurse_id = random.randint(1, 10)
        hr = random.randint(60, 110)
        temp = round(random.uniform(36.0, 39.0), 1)
        
        # Inject structural anomaly: Out of bounds invalid numeric entry
        if random.random() < 0.03:
            hr = -99 
            temp = 45.2
            
        lines.append(f"{t_id}|{a_id}|{nurse_id}|120/80|{hr}|18|{temp}|98|5|Chest Discomfort|None|None|Routine")

    # --- 5. ICU STAY SECTION ---
    lines.append("\n--- [ICU_STAY] ---")
    lines.append("unit_stay_id|admission_id|responsible_physician_id|unit_type|room_number|bed_number|entry_date_time|exit_date_time|reason_transfer")
    
    for stay_id in range(1, 500):
        a_id = random.choice(admission_ids)
        doc_id = random.randint(1, 15)
        entry_str = (base_date + timedelta(days=random.randint(0, 250))).strftime("%Y-%m-%d %H:%M:%S")
        exit_str = (base_date + timedelta(days=random.randint(0, 250))).strftime("%Y-%m-%d %H:%M:%S")
        
        lines.append(f"{stay_id}|{a_id}|{doc_id}|ICU|Room A|Bed 1|{entry_str}|{exit_str}|Continuous Monitoring")

    # --- 6. SURGICAL PROCEDURE SECTION ---
    lines.append("\n--- [SURGICAL_PROCEDURE] ---")
    lines.append("procedure_id|admission_id|patient_id|procedure_name|body_site|procedure_date_time|surgeon_id")
    
    for proc_id in range(1, 400):
        a_id = random.choice(admission_ids)
        p_id = random.choice(patient_ids)
        proc_date = (base_date + timedelta(days=random.randint(0, 250))).strftime("%Y-%m-%d %H:%M:%S")
        doc_id = random.randint(1, 15)
        
        lines.append(f"{proc_id}|{a_id}|{p_id}|Appendectomy|Appendix|{proc_date}|{doc_id}")

    # Write all lines out into a flat file pipeline block
    with open(OUTPUT_FILE, "w") as f:
        f.write("\n".join(lines))
        
    print(f"Success! Generated raw dirty data file '{OUTPUT_FILE}' with {len(lines) - 7} total entity table entries.")

if __name__ == "__main__":
    generate_data()
