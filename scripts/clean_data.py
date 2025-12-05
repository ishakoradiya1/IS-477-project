import pandas as pd
import os

def clean_schools(input_path="../data/raw/chicago_schools.csv",
                  output_path="../data/processed/schools_cleaned.csv"):
    """
    Cleans the Chicago schools dataset.
    Steps:
    - Select relevant columns
    - Drop rows with missing critical values
    - Standardize column names
    - Save cleaned dataframe to processed folder
    """
    df = pd.read_csv(input_path)
    
    # Select relevant columns
    cols = [
        'School ID', 'Name of School', 'Elementary, Middle, or High School',
        'Safety Score', 'Average Student Attendance',
        'ISAT Exceeding Reading %', 'Community Area Name',
        'Community Area Number', 'Latitude', 'Longitude', 'Ward'
    ]
    df_cleaned = df[cols].copy()

    # Drop rows with missing critical values
    df_cleaned = df_cleaned.dropna(subset=['Safety Score', 'Average Student Attendance', 'ISAT Exceeding Reading %'])

    # Standardize column names
    df_cleaned.columns = (
        df_cleaned.columns
        .str.strip()
        .str.replace(' ', '_')
        .str.replace('%', 'Percent')
        .str.replace(',', '')
    )

    # Ensure output folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save cleaned data
    df_cleaned.to_csv(output_path, index=False)
    print(f"Cleaned schools data saved to {output_path}")
    return df_cleaned


def clean_crime(input_path="../data/raw/crimes_2011.csv",
                output_path="../data/processed/crime_cleaned.csv"):
    """
    Cleans the Chicago crime dataset.
    Steps:
    - Filter for relevant year(s)
    - Drop duplicates
    - Select relevant columns
    - Drop rows with missing coordinates or Ward
    - Save cleaned dataframe to processed folder
    """
    df = pd.read_csv(input_path)

    # Filter by year
    df = df[df['Year'] == 2011]

    # Drop duplicates
    df = df.drop_duplicates()

    # Select relevant columns
    df_cleaned = df[['Primary Type', 'Ward', 'Latitude', 'Longitude']].copy()
    df_cleaned = df_cleaned.dropna(subset=['Ward', 'Latitude', 'Longitude'])
    df_cleaned.rename(columns={'Primary Type': 'Crime_Type'}, inplace=True)

    # Ensure output folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save cleaned data
    df_cleaned.to_csv(output_path, index=False)
    print(f"Cleaned crime data saved to {output_path}")
    return df_cleaned


if __name__ == "__main__":
    clean_schools()
    clean_crime()

