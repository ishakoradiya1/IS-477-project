import pandas as pd
import os

def clean_schools():
    df = pd.read_csv("data/raw/schools.csv")
    df_cleaned = df.dropna(subset=["LATITUDE", "LONGITUDE"])
    os.makedirs("data/processed", exist_ok=True)
    df_cleaned.to_csv("data/processed/schools_cleaned.csv", index=False)
    return df_cleaned

def clean_crime():
    df = pd.read_csv("data/raw/crime.csv")
    df_cleaned = df[df["Latitude"].notnull() & df["Longitude"].notnull()]
    os.makedirs("data/processed", exist_ok=True)
    df_cleaned.to_csv("data/processed/crime_cleaned.csv", index=False)
    return df_cleaned
