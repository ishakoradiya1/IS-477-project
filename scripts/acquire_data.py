import pandas as pd
import requests
import hashlib
import os

"""
# Data Acquisition 

Datasets were downloaded from the Chicago Open Data Portal:
- Schools: https://data.cityofchicago.org/api/views/9xs2-f89t/rows.csv?accessType=DOWNLOAD
- Crimes: https://data.cityofchicago.org/api/views/ijzp-q8t2/rows.csv?where=year%20=%202011

To acquire the data programmatically:
1. Run `scripts/acquire_data.py`
2. Verify SHA-256 checksums printed after download.
"""

# URLs from Chicago Data Portal
school_data_url = "https://data.cityofchicago.org/api/views/9xs2-f89t/rows.csv?accessType=DOWNLOAD"
crime_data_url = "https://data.cityofchicago.org/api/views/ijzp-q8t2/rows.csv?where=year%20=%202011"

RAW_DIR = "data/raw"
os.makedirs(RAW_DIR, exist_ok=True)

def download(url, filename):
    print(f"Downloading {filename}...")
    response = requests.get(url)
    response.raise_for_status()

    filepath = os.path.join(RAW_DIR, filename)
    with open(filepath, "wb") as f:
        f.write(response.content)

    print(f"Saved to {filepath}")
    return filepath

def sha256_checksum(path):
    sha = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha.update(chunk)
    return sha.hexdigest()


def main():
    school_path = os.path.join(RAW_DIR, "chicago_schools.csv")
    crime_path = os.path.join(RAW_DIR, "crimes_2011.csv")

    # Download only if files do not already exist
    if not os.path.exists(school_path):
        school_path = download(school_data_url, "chicago_schools.csv")
    else:
        print("chicago_schools.csv already exists")

    if not os.path.exists(crime_path):
        crime_path = download(crime_data_url, "crimes_2011.csv")
    else:
        print("crimes_2011.csv already exists")

    with open("checksums.txt", "w") as f:
        f.write(f"chicago_schools.csv: {sha256_checksum(school_path)}\n")
        f.write(f"crimes_2011.csv: {sha256_checksum(crime_path)}\n")

    print("\nChecksums saved to checksums.txt")


if __name__ == "__main__":
    main()
