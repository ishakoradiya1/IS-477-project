import pandas as pd
import requests
import hashlib
import os

"""
# Data Acquisition 

Datasets were downloaded from the Chicago Open Data Portal:
- Schools: [link]
- Crimes: [link]

To acquire the data programmatically:
1. Run `scripts/acquire_data.py`
2. Verify SHA-256 checksums printed after download.

Checksum ensures that the files were not corrupted or modified.
"""
# URLS are from Chicago Data Portal
school_data_url = "https://data.cityofchicago.org/api/views/9xs2-f89t/rows.csv?accessType=DOWNLOAD"
crime_data_url = "https://data.cityofchicago.org/api/views/ijzp-q8t2/rows.csv?accessType=DOWNLOAD"

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

if __name__ == "__main__":
    school_path = download(school_data_url, "chicago_schools.csv")
    crime_path = download(crime_data_url, "crimes_2011.csv")


    with open("checksums.txt", "w") as f:
        f.write(f"schools.csv: {sha256_checksum(school_path)}\n")
        f.write(f"crime.csv: {sha256_checksum(crime_path)}\n")
