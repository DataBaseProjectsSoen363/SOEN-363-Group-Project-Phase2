"""
Generate the PATIENT table for Source C (Continent C / XML format).
Output: SourceC_Hospital.xml (Part 1: Patients)

Differences from A & B:
  - XML hierarchical format
  - ISO 8601 Dates (YYYY-MM-DDTHH:MM:SS)
  - Uses nested tags for names and addresses
"""
import xml.etree.ElementTree as ET
import random
from datetime import datetime, timedelta

OUTPUT_FILE = "SourceC_Hospital.xml"
SEED = 1111
NUM_PATIENTS = 800

FIRST_NAMES = ["Mateo", "Lucia", "Hugo", "Valeria", "Daniel", "Sofia", "Alejandro", "Carmen"]
LAST_NAMES = ["Garcia", "Rodriguez", "Martinez", "Lopez", "Gonzalez", "Perez", "Sanchez"]
CITIES = ["Madrid", "Barcelona", "Valencia", "Seville", "Zaragoza"]

def generate_patients():
    random.seed(SEED)
    
    # 1. Create the root element
    hospital = ET.Element("Hospital")
    patients_node = ET.SubElement(hospital, "Patients")

    for p_id in range(1, NUM_PATIENTS + 1):
        # 2. Create a Patient element and add attributes
        patient = ET.SubElement(patients_node, "Patient", id=str(p_id))
        
        # 3. Nest the elements
        ET.SubElement(patient, "FirstName").text = random.choice(FIRST_NAMES)
        ET.SubElement(patient, "LastName").text = random.choice(LAST_NAMES)
        
        # Nested address
        address = ET.SubElement(patient, "Address")
        ET.SubElement(address, "Street").text = f"Calle {random.randint(1, 100)}"
        ET.SubElement(address, "City").text = random.choice(CITIES)
        
        # Date of Birth (ISO 8601 format)
        dob = datetime.now() - timedelta(days=random.randint(6500, 30000))
        ET.SubElement(patient, "DateOfBirth").text = dob.strftime("%Y-%m-%dT%H:%M:%S")
        
        # Gender and Contact
        ET.SubElement(patient, "Gender").text = random.choice(["M", "F"])
        ET.SubElement(patient, "Phone").text = f"+34-{random.randint(600, 699)}-{random.randint(100, 999)}-{random.randint(100, 999)}"
        
        # --- ANOMALY: Missing phone (~5%) ---
        if random.random() < 0.05:
            patient.find("Phone").text = "" # Empty tag

    # 4. Write to file (with pretty-printing for readability)
    tree = ET.ElementTree(hospital)
    ET.indent(tree, space="  ") # Python 3.9+ feature
    tree.write(OUTPUT_FILE, encoding="utf-8", xml_declaration=True)
    
    print(f"Wrote {OUTPUT_FILE} with {NUM_PATIENTS} patients.")

if __name__ == "__main__":
    generate_patients()