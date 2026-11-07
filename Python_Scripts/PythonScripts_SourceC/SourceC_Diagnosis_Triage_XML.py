"""
Generate the DIAGNOSIS and TRIAGE data for Source C (Continent C / XML format).
Output: SourceC_Hospital.xml (Part 3: Diagnoses and Triage)

Appends nested <Diagnoses> inside each <Admission>, and creates a
top-level <TriageAssessments> node.
"""
import xml.etree.ElementTree as ET
import random
from datetime import datetime, timedelta

FILE_NAME = "SourceC_Hospital.xml"
SEED = 3333

ICD9_CODES = ["401.9", "410.9", "250.00", "272.4"]

def generate_diagnoses_and_triage():
    random.seed(SEED)
    
    # 1. Parse the existing XML
    tree = ET.parse(FILE_NAME)
    root = tree.getroot()
    
    # Get all admissions
    admissions_node = root.find("Admissions")
    
    # Create a top-level node for Triage (since it's a separate entity in your schema)
    triage_node = ET.SubElement(root, "TriageAssessments")
    
    triage_id = 1

    for adm in admissions_node.findall("Admission"):
        a_id = int(adm.get("id"))
        admit_dt = datetime.strptime(adm.find("AdmissionDate").text, "%Y-%m-%dT%H:%M:%S")
        
        # ==========================================
        # DIAGNOSES (Nested inside the Admission)
        # ==========================================
        if random.random() < 0.90:
            diagnoses_node = ET.SubElement(adm, "Diagnoses")
            
            num_diags = random.randint(1, 3)
            codes = random.sample(ICD9_CODES, k=num_diags)
            
            for i, code in enumerate(codes):
                diag = ET.SubElement(diagnoses_node, "Diagnosis")
                ET.SubElement(diag, "ICD9Code").text = code
                
                # --- ANOMALY: Missing Diagnosis Date (~2%) ---
                if random.random() > 0.02:
                    diag_dt = admit_dt + timedelta(hours=random.randint(1, 12))
                    ET.SubElement(diag, "Date").text = diag_dt.strftime("%Y-%m-%dT%H:%M:%S")
                    
                # Lowercase boolean for XML
                is_primary = "true" if i == 0 else "false"
                ET.SubElement(diag, "IsPrimary").text = is_primary
                ET.SubElement(diag, "DoctorId").text = str(random.randint(1, 15))

        # ==========================================
        # TRIAGE (Top-level node)
        # ==========================================
        triage = ET.SubElement(triage_node, "Triage", id=str(triage_id))
        triage.set("admission_ref", str(a_id))
        
        # --- ANOMALY: Broken admission FK (~2%) ---
        if random.random() < 0.02:
            triage.set("admission_ref", "9999")

        ET.SubElement(triage, "NurseId").text = str(random.randint(16, 25))
        
        # --- ANOMALY: Out of bounds vitals (~3%) ---
        hr = random.randint(60, 100)
        if random.random() < 0.03:
            hr = -99
        ET.SubElement(triage, "HeartRate").text = str(hr)
        
        ET.SubElement(triage, "OxygenSaturation").text = str(random.randint(92, 100))
        ET.SubElement(triage, "Priority").text = random.choice(["ESI-1", "ESI-2", "ESI-3", "ESI-4", "ESI-5"])
        
        triage_id += 1

    # Save the tree
    ET.indent(tree, space="  ")
    tree.write(FILE_NAME, encoding="utf-8", xml_declaration=True)
    print(f"Appended Diagnoses (nested) and {triage_id - 1} Triage records to {FILE_NAME}.")

if __name__ == "__main__":
    generate_diagnoses_and_triage()