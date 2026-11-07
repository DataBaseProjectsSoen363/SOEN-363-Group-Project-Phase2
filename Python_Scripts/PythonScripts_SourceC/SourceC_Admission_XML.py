"""
Generate the ADMISSION data for Source C (Continent C / XML format).
Output: SourceC_Hospital.xml (Part 2: Admissions)

Reads the existing XML, adds an <Admissions> node, and saves it.
"""
import xml.etree.ElementTree as ET
import random
from datetime import datetime, timedelta

FILE_NAME = "SourceC_Hospital.xml"
SEED = 2222
NUM_ADMISSIONS = 1200

def generate_admissions():
    random.seed(SEED)
    
    # 1. Parse the existing XML file
    tree = ET.parse(FILE_NAME)
    root = tree.getroot()
    
    # 2. Create the Admissions container
    admissions_node = ET.SubElement(root, "Admissions")
    
    for a_id in range(1, NUM_ADMISSIONS + 1):
        # 3. Create an Admission node
        adm = ET.SubElement(admissions_node, "Admission", id=str(a_id))
        
        # --- ANOMALY: Broken patient reference (~2%) ---
        p_id = random.randint(1, 800)
        if random.random() < 0.02:
            p_id = 9999
        adm.set("patient_ref", str(p_id))
        
        # Dates (ISO 8601)
        admit_dt = datetime(2026, 1, 1) + timedelta(days=random.randint(0, 250), hours=random.randint(0, 23))
        discharge_dt = admit_dt + timedelta(days=random.randint(1, 10))
        
        ET.SubElement(adm, "AdmissionDate").text = admit_dt.strftime("%Y-%m-%dT%H:%M:%S")
        
        # --- ANOMALY: Missing Discharge Date (~3%) ---
        if random.random() > 0.03:
            ET.SubElement(adm, "DischargeDate").text = discharge_dt.strftime("%Y-%m-%dT%H:%M:%S")
            
        # --- ANOMALY: Impossible Date (~1%) ---
        if random.random() < 0.01:
            adm.find("DischargeDate").text = "2026-02-31T14:00:00" # Feb 31 doesn't exist
            
        ET.SubElement(adm, "AdmissionType").text = random.choice(["Emergency", "Elective", "Urgent"])
        ET.SubElement(adm, "Reason").text = random.choice(["Dolor torácico", "Dificultad respiratoria", "Fiebre"])
        
        # --- ANOMALY: Mixed case in reason (~5%) ---
        if random.random() < 0.05:
            adm.find("Reason").text = adm.find("Reason").text.upper()

        ET.SubElement(adm, "DoctorId").text = str(random.randint(1, 15))

    # 4. Save back to the same file
    ET.indent(tree, space="  ")
    tree.write(FILE_NAME, encoding="utf-8", xml_declaration=True)
    print(f"Appended {NUM_ADMISSIONS} admissions to {FILE_NAME}.")

if __name__ == "__main__":
    generate_admissions()