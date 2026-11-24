import subprocess

scripts = [
    "Clean_SourceA.py",
    "Clean_SourceB.py",
    "Clean_SourceC.py",
    "Clean_SourceD.py"
]

print(" Starting Task 2 cleaning Pipeline...\n")

for script in scripts:
    print(f"Running {script}...")
  
    result = subprocess.run(["python", script],text=True)
    
    if result.returncode == 0:
        print(f" {script} completed successfully.\n")
    else:
        print(f" {script} failed with error:\n{result.stderr}")

print("\n All Source cleaner Finished.")