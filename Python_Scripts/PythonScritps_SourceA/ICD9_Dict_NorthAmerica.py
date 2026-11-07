"""
Generate the ICD9_DICT reference table for Source A (North America / TXT).
Output: SourceA_icd9_dict.txt

This is a standardized reference/lookup table. No anomalies are injected.
The codes are stored as strings to preserve leading/trailing zeros.

Record layout (pipe-delimited):
  icd9_code | official_diagnosis_title | description | disease_category
"""

OUTPUT_FILE = "SourceA_icd9_dict.txt"

# The 4 canonical codes from your original Phase 1 script + 16 more for realism
ICD9_DATA = [
    # Original 4
    ("401.9", "Unspecified essential hypertension", "High blood pressure with no specific cause.", "Circulatory System"),
    ("410.9", "Acute myocardial infarction, unspecified site", "Heart attack occurring in an unspecified heart region.", "Circulatory System"),
    ("250.00", "Diabetes mellitus without complication", "Type II or unspecified diabetes managed stably.", "Endocrine/Metabolic"),
    ("272.4", "Other and unspecified hyperlipidemia", "Elevated cholesterol and lipids.", "Endocrine/Metabolic"),
    
    # Additional codes for realism
    ("428.0", "Congestive heart failure, unspecified", "Inability of the heart to pump enough blood.", "Circulatory System"),
    ("427.31", "Atrial fibrillation", "Irregular and often rapid heart rate.", "Circulatory System"),
    ("486", "Pneumonia, organism unspecified", "Infection of the lungs.", "Respiratory System"),
    ("491.21", "Obstructive chronic bronchitis with acute exacerbation", "Worsening of chronic bronchitis.", "Respiratory System"),
    ("530.81", "Esophageal reflux", "Gastroesophageal reflux disease (GERD).", "Digestive System"),
    ("531.90", "Gastric ulcer, unspecified as acute or chronic", "Ulcer in the stomach lining.", "Digestive System"),
    ("584.9", "Acute kidney failure, unspecified", "Sudden loss of kidney function.", "Genitourinary System"),
    ("599.0", "Urinary tract infection, site not specified", "Infection in the urinary system.", "Genitourinary System"),
    ("780.2", "Syncope and collapse", "Fainting or passing out.", "Nervous System"),
    ("780.39", "Other convulsions", "Seizures or convulsions.", "Nervous System"),
    ("784.0", "Headache", "Pain in the head.", "Nervous System"),
    ("786.50", "Chest pain, unspecified", "Pain in the chest area.", "Respiratory System"),
    ("789.00", "Abdominal pain, unspecified site", "Pain in the abdomen.", "Digestive System"),
    ("790.6", "Other abnormal blood chemistry", "Abnormal findings in blood tests.", "Endocrine/Metabolic"),
    ("995.3", "Allergy, unspecified", "Allergic reaction of unspecified type.", "Immune System"),
    ("V58.69", "Long-term use of other medications", "Patient is on long-term medication therapy.", "Factors Influencing Health")
]

def generate_icd9_dict():
    lines = [
        "--- [ICD9_DICT] ---",
        "icd9_code|official_diagnosis_title|description|disease_category"
    ]

    for code, title, desc, category in ICD9_DATA:
        # Note: We wrap the code in quotes inside the f-string implicitly 
        # by ensuring it is passed as a string, preserving leading/trailing zeros.
        lines.append(f"{code}|{title}|{desc}|{category}")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Wrote {OUTPUT_FILE} with {len(ICD9_DATA)} reference entries.")

if __name__ == "__main__":
    generate_icd9_dict()