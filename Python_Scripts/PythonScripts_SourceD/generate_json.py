import subprocess

scripts = [
    "SourceD_Admission_JSON.py",
    "SourceD_Diagnosis_JSON.py",
    "SourceD_Final_Tables_JSON.py",
    "SourceD_ICU_Surgery_JSON.py",
    "SourceD_Patient_JSON.py",
    "SourceD_Triage_JSON.py"
]

print(" Generate JSON files for Source D...\n")

for script in scripts:
    print(f"Running {script}...")
  
    result = subprocess.run(["python", script], capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f" {script} completed successfully.")
    else:
        print(f" {script} failed with error:\n{result.stderr}")

print("\n All Source Loaders Finished.")