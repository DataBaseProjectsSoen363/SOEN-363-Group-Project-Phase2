"""
Generate the final tables for Source C (Continent C / XML format).
Output: SourceC_Hospital.xml (Part 5: Notes, Orders, Radiology, Discharge)

Appends the remaining tables and saves the complete XML file.
"""
import xml.etree.ElementTree as ET
import random
from datetime import datetime, timedelta

FILE_NAME = "SourceC_Hospital.xml"
SEED = 5555

def generate_final_tables():
    random.seed(SEED)
    
    # 1. Parse existing XML
    tree = ET.parse(FILE_NAME)
    root = tree.getroot()
    
    admissions_node = root.find("Admissions")
    
    # Create containers for the remaining tables
    notes_node = ET.SubElement(root, "ClinicalNotes")
    orders_node = ET.SubElement(root, "DiagnosticOrders")
    radiology_node = ET.SubElement(root, "RadiologyExaminations")
    discharge_node = ET.SubElement(root, "DischargeRecords")
    
    note_id = 1
    order_id = 1
    exam_id = 1
    discharge_id = 1

    for adm in admissions_node.findall("Admission"):
        a_id = int(adm.get("id"))
        admit_dt_str = adm.find("AdmissionDate").text
        admit_dt = datetime.strptime(admit_dt_str, "%Y-%m-%dT%H:%M:%S")
        
        # ==========================================
        # CLINICAL NOTES (~90% of admissions)
        # ==========================================
        if random.random() < 0.90:
            note = ET.SubElement(notes_node, "Note", id=str(note_id))
            note.set("admission_ref", str(a_id))
            
            ET.SubElement(note, "DoctorId").text = str(random.randint(1, 15))
            
            # --- ANOMALY: CDATA section for free text ---
            note_body = ET.SubElement(note, "Body")
            # We use CDATA so the XML parser doesn't treat '<' or '>' as tags
            note_body.text = "<![CDATA[Subjective: Patient presents with acute distress. <br/> Objective: Vitals stable.]]>"
            
            # --- ANOMALY: Empty Note Body (~3%) ---
            if random.random() < 0.03:
                note_body.text = "<![CDATA[]]>"
                
            note_id += 1

        # ==========================================
        # DIAGNOSTIC ORDERS & RADIOLOGY (~25% of admissions)
        # ==========================================
        if random.random() < 0.25:
            order = ET.SubElement(orders_node, "Order", id=str(order_id))
            order.set("admission_ref", str(a_id))
            
            ET.SubElement(order, "ExamType").text = random.choice(["X-Ray", "CT Scan", "MRI"])
            ET.SubElement(order, "DoctorId").text = str(random.randint(1, 15))
            
            order_dt = admit_dt + timedelta(hours=random.randint(1, 5))
            ET.SubElement(order, "OrderDate").text = order_dt.strftime("%Y-%m-%dT%H:%M:%S")
            
            # Nested Radiology inside the Order
            rad = ET.SubElement(radiology_node, "Exam", id=str(exam_id))
            rad.set("order_ref", str(order_id))
            
            ET.SubElement(rad, "ScanDate").text = (order_dt + timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%S")
            ET.SubElement(rad, "Technician").text = f"Tech_{random.randint(1, 10)}"
            
            # Nested Report inside the Radiology Exam
            report = ET.SubElement(rad, "Report")
            ET.SubElement(report, "Findings").text = random.choice(["Normal", "Mild opacity", "Clear lungs"])
            ET.SubElement(report, "Conclusion").text = "No acute intervention required."
            
            # --- ANOMALY: Missing report (~5%) ---
            if random.random() < 0.05:
                rad.remove(report)

            order_id += 1
            exam_id += 1

        # ==========================================
        # DISCHARGE RECORDS (Only if there is a discharge date)
        # ==========================================
        discharge_date_tag = adm.find("DischargeDate")
        if discharge_date_tag is not None and discharge_date_tag.text:
            try:
                discharge_dt = datetime.strptime(discharge_date_tag.text, "%Y-%m-%dT%H:%M:%S")
                
                disc = ET.SubElement(discharge_node, "Discharge", id=str(discharge_id))
                disc.set("admission_ref", str(a_id))
                
                ET.SubElement(disc, "DischargeDate").text = discharge_dt.strftime("%Y-%m-%dT%H:%M:%S")
                ET.SubElement(disc, "Destination").text = random.choice(["Home", "Rehab", "Transfer"])
                ET.SubElement(disc, "Condition").text = random.choice(["Stable", "Improved"])
                
                discharge_id += 1
            except ValueError:
                # Catch the impossible dates (e.g., Feb 31)
                pass

    # Save
    ET.indent(tree, space="  ")
    tree.write(FILE_NAME, encoding="utf-8", xml_declaration=True)
    print(f"Appended Notes, Orders, Radiology, and {discharge_id - 1} Discharges to {FILE_NAME}.")
    print("🎉 Source C (XML) is complete!")

if __name__ == "__main__":
    generate_final_tables()