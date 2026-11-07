
def clean(df):

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing values
    df= df.fillna("Unknown")

    # Replace values
    df["Gender"] = df["Gender"].replace(
        {"M": "Male", "F": "Female"}
    )