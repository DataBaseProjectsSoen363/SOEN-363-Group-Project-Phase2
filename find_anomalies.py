import pandas as pd
import os

# Configuration for the sources we want to check
sources = {
    "SourceA (ICU Stays)": {
        "path": "./Data_Sources/SourceA/SourceA_icu_stays.txt",
        "type": "csv",
        "sep": "|",
        "skiprows": 1
    },
    "SourceB (Clinical Notes)": {
        "path": "./Data_Sources/SourceB/SourceB_clinical_note.csv",
        "type": "csv",
        "sep": ",",
        "skiprows": 0
    },
    "SourceC (Patients)": {
        "path": "./Data_Sources/SourceC/SourceC_Hospital.xml",
        "type": "xml",
        "xpath": ".//Patient"
    },
    "SourceD (Admissions)": {
        "path": "./Data_Sources/SourceD/SourceD_admissions.json",
        "type": "json"
    }
}

def find_one_anomaly(name, config):
    print(f"\n{'='*50}")
    print(f"Checking Source: {name}")
    print(f"{'='*50}")
    
    try:
        # Load the file based on the type specified in the config
        if config["type"] == "json":
            df = pd.read_json(config["path"])
            
        elif config["type"] == "xml":
            df = pd.read_xml(config["path"], xpath=config["xpath"])
            
        elif config["type"] == "csv":
            df = pd.read_csv(
                config["path"], 
                sep=config["sep"], 
                skiprows=config["skiprows"]
            )
            
    except Exception as e:
        print(f"Could not load {name}: {e}")
        return

    # Look for rows where ANY cell is 'N/A', empty string, or NaN
    # We use df.isna() to catch missing values and df.isin() for literal strings
    anomaly_mask = (
        df.isin(["N/A", ""]).any(axis=1) | 
        df.isna().any(axis=1)
    )
    
    bad_rows = df[anomaly_mask]
    
    if bad_rows.empty:
        print("No obvious 'N/A' or empty anomalies found in this file.")
    else:
        print(f"Found {len(bad_rows)} rows with anomalies :\n")
        # Print bad row
        print(bad_rows.iloc[0].to_string())
        print("\n")

# Run it
for name, config in sources.items():
    find_one_anomaly(name, config)