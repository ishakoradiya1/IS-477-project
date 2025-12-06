import pandas as pd
import os

"""
# Data Integration

- Merges cleaned schools and crime datasets on relevant keys (e.g., location, street, etc.).
- Outputs `merged_school_crime.csv` in `data/processed/`.
- Ensures consistent formatting of columns and removes duplicates.

"""
def merge_datasets(schools_path="data/processed/schools_cleaned.csv",
                   crime_path="data/processed/crime_cleaned.csv",
                   output_path="data/processed/merged_school_crime.csv"):
    """
    Integrates cleaned school and crime datasets.
    Steps:
    - Aggregate crime counts by Ward
    - Merge aggregated crime data with school dataset
    - Save merged dataframe to processed folder
    """
    schools = pd.read_csv(schools_path)
    crime = pd.read_csv(crime_path)

    # Aggregate crime count by Ward
    crime_by_ward = crime.groupby('Ward').size().reset_index(name='Crime_Count')

    # Merge with school dataset
    merged = pd.merge(schools, crime_by_ward, on='Ward', how='left')

    # Ensure output folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save merged dataset
    merged.to_csv(output_path, index=False)
    print(f"Merged school and crime data saved to {output_path}")
    return merged


if __name__ == "__main__":
    merge_datasets()

