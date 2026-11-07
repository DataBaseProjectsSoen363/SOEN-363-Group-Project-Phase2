"""
Generate the PATIENT table for Source A (North America / TXT format).
Output: SourceA_patients.txt

Record layout (pipe-delimited):
  patient_id | name | health_insurance_number | life_status | address
  | date_birth | gender | emergency_contact_number | phone_number

Anomalies injected (documented for cleaning practice):
  - Inconsistent capitalization / whitespace in address (~5%)
  - Missing phone_number (~2%)
  - Invalid gender value (~1%)
  - Future / impossible date_birth (~1%)
  - Duplicate health_insurance_number (~2%)
"""
import random
from datetime import datetime, timedelta

# ---- CONFIG ----
NUM_PATIENTS = 800
OUTPUT_FILE = "SourceA_patients.txt"
SEED = 42

FIRST_NAMES = ["Daniel", "Sarah", "John", "Emily", "Michael",
               "Amelie", "David", "Jessica", "Robert", "Rachel"]
LAST_NAMES = ["Tremblay", "Smith", "Roy", "Gagnon", "Jones",
              "Williams", "Brown", "Charette", "Taylor", "Miller"]
CITIES = ["Montreal", "Laval", "Longueuil", "Sherbrooke", "Quebec City"]
STREETS = ["Sherbrooke St", "Sainte-Catherine St", "Papineau Ave",
           "Guy St", "Atwater Ave"]
VALID_GENDERS = ["Male", "Female"]

def generate_patients():
    random.seed(SEED)
    lines = []
    lines.append("--- [PATIENT] ---")
    lines.append(
        "patient_id|name|health_insurance_number|life_status|address"
        "|date_birth|gender|emergency_contact_number|phone_number"
    )

    used_hin = set()
    used_dupe_hin = []

    for p_id in range(1, NUM_PATIENTS + 1):
        name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"

        # --- health_insurance_number: mostly unique, ~2% duplicate ---
        if used_dupe_hin and random.random() < 0.02:
            hin = random.choice(used_dupe_hin)  # duplicate
        else:
            hin = f"RAMQ{random.randint(100000, 999999)}"
            while hin in used_hin:
                hin = f"RAMQ{random.randint(100000, 999999)}"
            used_hin.add(hin)
            used_dupe_hin.append(hin)

        addr = (f"{random.randint(100, 5000)} "
                f"{random.choice(STREETS)}, {random.choice(CITIES)}")

        # --- address formatting anomaly (~5%) ---
        if random.random() < 0.05:
            addr = f"   {addr.upper()}   "

        # --- date_birth ---
        dob = (datetime.now() -
               timedelta(days=random.randint(6500, 30000))
               ).strftime("%Y-%m-%d")
        # --- invalid future birth date (~1%) ---
        if random.random() < 0.01:
            dob = (datetime.now() + timedelta(days=365)).strftime("%Y-%m-%d")

        # --- gender ---
        gender = random.choice(VALID_GENDERS)
        if random.random() < 0.01:
            gender = random.choice(["M", "F", "Unknown", ""])  # invalid

        phone = f"514-555-{random.randint(1000, 9999)}"
        # --- missing phone (~2%) ---
        if random.random() < 0.02:
            phone = ""

        lines.append(
            f"{p_id}|{name}|{hin}|Alive|{addr}|{dob}|{gender}|{phone}|{phone}"
        )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    data_rows = len(lines) - 2  # subtract section header + column header
    print(f"Wrote {OUTPUT_FILE} with {data_rows} patient records.")

if __name__ == "__main__":
    generate_patients()