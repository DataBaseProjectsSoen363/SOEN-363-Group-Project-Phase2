"""
Generate the ICU_STAY and SURGICAL_PROCEDURE data for Source C (XML format).
Output: SourceC_Hospital.xml (Part 4)

Appends <ICUStays> and <SurgicalProcedures> to the root.
"""
import xml.etree.ElementTree as ET
import random
from datetime import datetime, timedelta

FILE_NAME = "SourceC_Hospital.xml"
SEED = 4444

def generate_icu_and_surgery():
    random.seed(SEED)
    
    # 1. Parse existing XML
    tree = ET.parse(FILE_NAME)
    root = tree.getroot()
    
    admissions_node = root.find("Admissions")
    
    # Create containers
    icu_node = ET.SubElement(root, "ICUStays")
    surgery_node = ET.SubElement(root, "SurgicalProcedures")
    
    icu_id = 1
    surg_id = 1

    # 2. Iterate through admissions to attach records
    for adm in admissions_node.findall("Admission"):
        a_id = int(adm.get("id"))
        
        # Parse admission date to generate realistic timelines
        admit_dt_str = adm.find("AdmissionDate").text
        admit_dt = datetime.strptime(admit_dt_str, "%Y-%m-%dT%H:%M:%S")

        # ==========================================
        # ICU STAYS (~30% of admissions)
        # ==========================================
        if random.random() < 0.30:
            stay = ET.SubElement(icu_node, "Stay", id=str(icu_id))
            stay.set("admission_ref", str(a_id))
            
            ET.SubElement(stay, "WardType").text = random.choice(["ICU", "CCU", "MICU"])
            ET.SubElement(stay, "DoctorId").text = str(random.randint(1, 15))
            
            entry_dt = admit_dt + timedelta(hours=random.randint(1, 24))
            exit_dt = entry_dt + timedelta(days=random.randint(1, 5))
            
            ET.SubElement(stay, "EntryDate").text = entry_dt.strftime("%Y-%m-%dT%H:%M:%S")
            
            # --- ANOMALY: Chronological error / Empty tag (~3%) ---
            if random.random() < 0.03:
                ET.SubElement(stay, "ExitDate").text = (entry_dt - timedelta(hours=5)).strftime("%Y-%m-%dT%H:%M:%S")
            elif random.random() < 0.05:
                ET.SubElement(stay, "ExitDate") # Completely empty tag
            else:
                ET.SubElement(stay, "ExitDate").text = exit_dt.strftime("%Y-%m-%dT%H:%M:%S")
                
            icu_id += 1

        # ==========================================
        # SURGICAL PROCEDURES (~20% of admissions)
        # ==========================================
        if random.random() < 0.20:
            surg = ET.SubElement(surgery_node, "Procedure", id=str(surg_id))
            surg.set("admission_ref", str(a_id))
            
            # Using an attribute for the name instead of a nested tag
            proc_name = random.choice(["Appendectomy", "Cholecystectomy", "CABG"])
            surg.set("name", proc_name)
            
            surg_dt = admit_dt + timedelta(days=random.randint(1, 2))
            ET.SubElement(surg, "Date").text = surg_dt.strftime("%Y-%m-%dT%H:%M:%S")
            ET.SubElement(surg, "SurgeonId").text = str(random.randint(1, 15))
            
            # --- ANOMALY: Missing Surgeon ID (~2%) ---
            if random.random() < 0.02:
                surg.find("SurgeonId").text = ""

            surg_id += 1

    # Save
    ET.indent(tree, space="  ")
    tree.write(FILE_NAME, encoding="utf-8", xml_declaration=True)
    print(f"Appended {icu_id - 1} ICU stays and {surg_id - 1} surgeries to {FILE_NAME}.")

if __name__ == "__main__":
    generate_icu_and_surgery()