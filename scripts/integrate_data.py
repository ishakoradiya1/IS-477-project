import pandas as pd
import os

def merge_datasets():
    schools = pd.read_csv("data/processed/schools_cleaned.csv")
    crime = pd.read_csv("data/processed/crime_cleaned.csv")

    merged = pd.merge(
        schools,
        crime,
        how="left",
        left_on="SCHOOL_ID",
        right_on="school_id"
    )

    os.makedirs("data/processed", exist_ok=True)
    merged.to_csv("data/processed/merged_school_crime.csv", index=False)
    return merged
