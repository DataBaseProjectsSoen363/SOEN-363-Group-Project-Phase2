import pandas as pd

import os
os.makedirs("Profiles", exist_ok=True)

def profile_dataframe(df, output_file):
    df = df.copy()
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str)

    with open(output_file, "w") as f:
        f.write("===== RECORD COUNT =====\n")
        f.write(f"{len(df)}\n\n")

        f.write("===== SHAPE =====\n")
        f.write(f"{df.shape}\n\n")

        f.write("===== FIELD NAMES =====\n")
        f.write(f"{df.columns.tolist()}\n\n")

        f.write("===== DATA TYPES =====\n")
        f.write(df.dtypes.to_string())
        f.write("\n\n")

        f.write("===== MISSING VALUES =====\n")
        f.write(df.isna().sum().to_string())
        f.write("\n\n")

        f.write("===== HIDDEN MISSING VALUES (String 'N/A') =====\n")
        f.write(df.eq("N/A").sum().to_string())
        f.write("\n\n")

        f.write("===== DUPLICATE ROWS =====\n")
        f.write(f"{df.duplicated().sum()}\n\n")

        f.write("===== SAMPLE RECORDS =====\n")
        if len(df) > 0:
            f.write(df.sample(min(5, len(df))).to_string())
        else:
            f.write("(empty dataframe — no sample available)")
        f.write("\n\n")

        f.write("===== SUMMARY STATISTICS =====\n")
        if len(df) > 0 and len(df.columns) > 0:
            try:
                f.write(df.describe(include="all").to_string())
            except Exception as e:
                f.write(f"(describe failed: {e})")
        else:
            f.write("(empty dataframe — no statistics available)")
        f.write("\n")