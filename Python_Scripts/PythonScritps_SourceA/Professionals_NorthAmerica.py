"""
Generate the PROFESSIONALS roster for Source A (North America / TXT).
Output: SourceA_professionals.txt

This is ONE raw source file that will be split into TWO target tables
(physician, nurse) during the Phase 2 load step, using `role` as the
discriminator. This mirrors a real HR/staffing export.

Record layout:
  professional_id | full_name | role | specialty | license_number

FK targets downstream:
  physician(physician_id)  <- admissions, diagnoses, icu_stay, clinical_note,
                              diagnostic_order, radiology_examination,
                              surgical_procedure, discharge_record
  nurse(nurse_id)          <- triage_assessment

Anomalies injected (documented):
  - role capitalization / whitespace variants (~10% of all staff)
  - specialty missing for nurses (expected — nurses have no specialty)
  - specialty occasionally blank for a physician (~7%) -> optional-missing
  - full_name occasionally has double spaces / leading space (~5%)
"""
import random

NUM_PHYSICIANS = 15
NUM_NURSES = 10
OUTPUT_FILE = "SourceA_professionals.txt"
SEED = 7

FIRST = ["Daniel", "Sarah", "John", "Emily", "Michael",
         "Amelie", "David", "Jessica", "Robert", "Rachel"]
LAST = ["Tremblay", "Smith", "Roy", "Gagnon", "Jones",
        "Williams", "Brown", "Charette", "Taylor", "Miller"]
SPECIALTIES = ["Cardiology", "Internal Medicine", "Emergency Medicine",
               "Pulmonology", "General Surgery"]


def dirty_name(name: str) -> str:
    if random.random() < 0.05:
        return random.choice([f" {name}", f"{name} ", name.replace(" ", "  ")])
    return name


def dirty_role(role: str) -> str:
    if random.random() < 0.10:
        return random.choice([role.lower(), role.upper(), f" {role} "])
    return role


def generate_professionals():
    random.seed(SEED)
    lines = [
        "--- [PROFESSIONAL] ---",
        "professional_id|full_name|role|specialty|license_number",
    ]

    pid = 1  # roster-local ID, spans physicians THEN nurses

    # ---- Physicians ----
    for _ in range(NUM_PHYSICIANS):
        name = dirty_name(f"Dr. {random.choice(FIRST)} {random.choice(LAST)}")
        spec = random.choice(SPECIALTIES)
        if random.random() < 0.07:      # physician w/ missing specialty
            spec = ""
        lic = f"MD-{random.randint(10000, 99999)}"
        role = dirty_role("Physician")
        lines.append(f"{pid}|{name}|{role}|{spec}|{lic}")
        pid += 1

    # ---- Nurses ----
    for _ in range(NUM_NURSES):
        name = dirty_name(f"{random.choice(FIRST)} {random.choice(LAST)}")
        # nurses have no specialty -> always blank (optional-missing)
        spec = ""
        lic = f"RN-{random.randint(10000, 99999)}"
        role = dirty_role("Nurse")
        lines.append(f"{pid}|{name}|{role}|{spec}|{lic}")
        pid += 1

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Wrote {OUTPUT_FILE} with {pid - 1} professionals "
          f"({NUM_PHYSICIANS} physicians, {NUM_NURSES} nurses).")


if __name__ == "__main__":
    generate_professionals()