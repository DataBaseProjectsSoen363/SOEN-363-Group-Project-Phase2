"""
Generate the RADIOLOGY_REPORT table for Source A (North America / TXT).
Output: SourceA_radiology_reports.txt

Reads SourceA_radiology_examinations.txt to enforce the 1:1 relationship.
(Note: radiology_report_id acts as both the PK and the FK to examination_id).

Record layout (pipe-delimited):
  radiology_report_id | radiologist_findings | interpretation | clinical_conclusion

Anomalies injected (documented):py
  - Missing reports (~5%): not every exam gets a report
  - Missing interpretation (~3%): blank field
  - Inconsistent formatting (~5%): lowercase or padded clinical_conclusion
  - Broken FK (~2%): radiology_report_id points to a non-existent exam
"""
import random

EXAMS_FILE = "SourceA_radiology_examinations.txt"
OUTPUT_FILE = "SourceA_radiology_reports.txt"
SEED = 222

FINDINGS = [
    "Lungs appear clear. No focal consolidation.",
    "Mild cardiomegaly noted. No pleural effusion.",
    "No acute bony abnormalities identified.",
    "Mild degenerative changes in the lumbar spine.",
    "Soft tissues are unremarkable."
]
INTERPRETATIONS = [
    "No major effusion detected.",
    "Findings are consistent with early congestive heart failure.",
    "No evidence of acute fracture or dislocation.",
    "Likely benign etiology. Routine follow-up recommended.",
    "Unremarkable study."
]
CONCLUSIONS = [
    "Normal structural limits.",
    "Recommend clinical correlation.",
    "No acute findings.",
    "Stable compared to prior imaging.",
    "Further evaluation suggested if symptoms persist."
]

def load_exams(path=EXAMS_FILE):
    """Returns a list of valid examination_ids."""
    exams = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("---") or line.startswith("examination_id"):
                continue
            parts = line.split("|")
            try:
                e_id = int(parts[0])
                # Only use clean exams as our baseline
                if e_id <= 1200:
                    exams.append(e_id)
            except (ValueError, IndexError):
                continue
    return exams

def generate_radiology_reports():
    random.seed(SEED)
    exams = load_exams()

    lines = [
        "--- [RADIOLOGY_REPORT] ---",
        "radiology_report_id|radiologist_findings|interpretation|clinical_conclusion"
    ]

    report_count = 0
    for e_id in exams:
        # --- ANOMALY: Missing Reports (~5%) ---
        if random.random() < 0.05:
            continue

        # --- ANOMALY: Broken FK (~2%) ---
        output_e_id = e_id
        if random.random() < 0.02:
            output_e_id = 9999

        findings = random.choice(FINDINGS)
        interpretation = random.choice(INTERPRETATIONS)
        conclusion = random.choice(CONCLUSIONS)

        # --- ANOMALY: Missing interpretation (~3%) ---
        if random.random() < 0.03:
            interpretation = ""

        # --- ANOMALY: Inconsistent formatting (~5%) ---
        if random.random() < 0.05:
            conclusion = random.choice([conclusion.lower(), conclusion.upper(), f"  {conclusion}  "])

        lines.append(
            f"{output_e_id}|{findings}|{interpretation}|{conclusion}"
        )
        report_count += 1

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Wrote {OUTPUT_FILE} with {report_count} radiology report records.")

if __name__ == "__main__":
    generate_radiology_reports()