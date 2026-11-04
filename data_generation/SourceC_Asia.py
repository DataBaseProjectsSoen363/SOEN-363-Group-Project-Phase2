import random
import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime, timedelta

# ---- CONFIGURATION ----
OUTPUT_FILE = "source_c_asia.xml"

# ---- ASIAN LOOKUPS & VARIANCE CODES ----
ICD9_POOL = ["401.9", "410.9", "250.00", "272.4"]
FIRST_NAMES = ["Hiroshi", "Mei", "Arjun", "Aanya", "Zheng", "Ananya", "Chao", "Haruto", "Yuki", "Siddharth"]
LAST_NAMES = ["Sato", "Tanaka", "Kumar", "Sharma", "Li", "Wang", "Suzuki", "Patel", "Chen", "Gupta"]
CITIES = ["Tokyo", "Mumbai", "Shanghai", "Singapore", "Seoul"]
STREETS = ["Chuo-ku Lane", "MG Road", "Nanjing Road", "Orchard Orchard", "Gangnam Ave"]
UNIT_TYPES = ["ICU", "CCU", "MICU", "SICU"]

def generate_asia_xml():
    random.seed(202) # Explicit seed for clean structural variation

    # Root container node
    root = ET.Element("HospitalSystem", continent="Asia", source="Source_C")

    patient_ids = list(range(1, 800))
    admission_ids = list(range(1, 1200))

    # --- 1. PATIENTS SECTION ---
    patients_node = ET.SubElement(root, "Patients")
    for p_id in patient_ids:
        p_elem = ET.SubElement(patients_node, "Patient")
        ET.SubElement(p_elem, "patient_id").text = str(p_id)

        name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
        # Inject textual anomaly: irregular chaotic casing (approx 5% rate)
        if random.random() < 0.05:
            name = name.upper()
            
        ET.SubElement(p_elem, "name").text = name
        ET.SubElement(p_elem, "health_insurance_number").text = f"AS-INS{random.randint(100000, 999999)}"
        ET.SubElement(p_elem, "life_status").text = "Alive"
        ET.SubElement(p_elem, "address").text = f"{random.randint(1, 99)} {random.choice(STREETS)}, {random.choice(CITIES)}"
        ET.SubElement(p_elem, "date_birth").text = (datetime.now() - timedelta(days=random.randint(6500, 30000))).strftime("%Y-%m-%d")
        ET.SubElement(p_elem, "gender").text = random.choice(["Male", "Female"])
        ET.SubElement(p_elem, "phone_number").text = f"+81-3-{random.randint(1000, 9999)}"

    # --- 2. ADMISSIONS SECTION ---
    admissions_node = ET.SubElement(root, "Admissions")
    base_date = datetime(2026, 1, 1)
    for a_id in admission_ids:
        a_elem = ET.SubElement(admissions_node, "Admission")
        ET.SubElement(a_elem, "admission_id").text = str(a_id)
        ET.SubElement(a_elem, "patient_id").text = str(random.choice(patient_ids))
        
        admit_dt = base_date + timedelta(days=random.randint(0, 250), hours=random.randint(0, 23))
        discharge_dt = admit_dt + timedelta(days=random.randint(1, 9))
        
        ET.SubElement(a_elem, "admission_date_time").text = admit_dt.strftime("%Y-%m-%d %H:%M:%S")
        
        # Inject structural anomaly: drop a child tag completely to mimic missing optional data values
        if random.random() >= 0.04:
            ET.SubElement(a_elem, "discharge_date_time").text = discharge_dt.strftime("%Y-%m-%d %H:%M:%S")
            
        ET.SubElement(a_elem, "admission_type").text = "Elective"
        ET.SubElement(a_elem, "admission_source").text = "Referral"
        ET.SubElement(a_elem, "reason_admission").text = "Routine Evaluation"
        ET.SubElement(a_elem, "current_condition").text = "Stable"
        ET.SubElement(a_elem, "admitting_professional_id").text = str(random.randint(1, 15))

    # --- 3. DIAGNOSIS SECTION ---
    diagnoses_node = ET.SubElement(root, "Diagnoses")
    for diag_id in range(1, 1500):
        d_elem = ET.SubElement(diagnoses_node, "Diagnosis")
        ET.SubElement(d_elem, "diagnosis_id").text = str(diag_id)
        ET.SubElement(d_elem, "admission_id").text = str(random.choice(admission_ids))
        ET.SubElement(d_elem, "icd9_code").text = random.choice(ICD9_POOL)
        ET.SubElement(d_elem, "primary_diagnosis").text = "True"

    # --- 4. TRIAGE ASSESSMENT SECTION ---
    triage_node = ET.SubElement(root, "TriageAssessments")
    for t_id in range(1, 1200):
        t_elem = ET.SubElement(triage_node, "TriageAssessment")
        ET.SubElement(t_elem, "triage_id").text = str(t_id)
        ET.SubElement(t_elem, "admission_id").text = str(random.choice(admission_ids))

        hr = random.randint(60, 110)
        # Inject invalid data anomaly: negative impossible values
        if random.random() < 0.03:
            hr = -5
            
        ET.SubElement(t_elem, "heart_rate").text = str(hr)
        ET.SubElement(t_elem, "body_temperature").text = "36.8"
        ET.SubElement(t_elem, "triage_priority_level").text = "Routine"

    # Convert node map to clean string using minidom for pretty formatting indentation lines
    xml_str = ET.tostring(root, encoding="utf-8")
    parsed_xml = minidom.parseString(xml_str)
    pretty_xml = parsed_xml.toprettyxml(indent="  ")
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(pretty_xml)
        
    print(f"Success! Generated Asian structural XML data file '{OUTPUT_FILE}' cleanly with matching sub-elements.")

if __name__ == "__main__":
    generate_asia_xml()

