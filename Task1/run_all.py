import subprocess

scripts = [
    "ETL_Load_SourceA.py",
    "ETL_Load_SourceB.py",
    "ETL_Load_SourceC.py",
    "ETL_Load_SourceD.py"
]

print("\nStarting Task 1 ETL Pipeline...\n")

for script in scripts:
    print(f"Running {script}...")
  
    result = subprocess.run(["python", script],text=True)
    
    if result.returncode == 0:
        print(f" {script} completed successfully.\n")
    else:
        print(f" {script} failed with error:\n{result.stderr}")

print("\n All Source Loaders Finished.\n")