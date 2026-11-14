import subprocess
import os

scripts = [
    "SourceD_Patient_JSON.py",
    "SourceD_Admission_JSON.py",
    "SourceD_Diagnosis_JSON.py",
    "SourceD_Triage_JSON.py",
    "SourceD_ICU_Surgery_JSON.py",
    "SourceD_Final_Tables_JSON.py"
]

# Get the directory where THIS script lives (PythonScripts_SourceD)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Define where the files should be saved (../Data_Sources/SourceD)
OUTPUT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", "Data_Sources", "SourceD"))

print("Generate JSON files for Source D...\n")
print(f"Target directory: {OUTPUT_DIR}\n")

for script in scripts:
    print(f"Running {script}...")
    
    # 1. Construct the full path to the script
    script_path = os.path.join(SCRIPT_DIR, script)
    
    # 2. Run it, forcing the output to go to OUTPUT_DIR
    result = subprocess.run(
        ["python", script_path], 
        capture_output=True, 
        text=True,
        cwd=OUTPUT_DIR 
    )
    
    if result.returncode == 0:
        print(f"  {script} completed successfully.")
    else:
        print(f"  {script} FAILED.")
        print(f"  Error:\n{result.stderr}")
        break

print("\nAll Source D JSON files generated.")