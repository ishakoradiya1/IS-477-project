# Storage & Organization Strategy

## Filesystem Layout
Our project uses the following structured file system based storage model:

data/
raw/
schools.csv
crime.csv
processed/
schools_cleaned.csv
crime_cleaned.csv
merged_school_crime.csv
notebooks/
scripts/
docs/
reports/

## Rationale
We selected CSV + filesystem storage for the following reasons:

- The Chicago datasets are naturally tabular and provided as CSV.
- The datasets are small enough (<150MB each) to fit comfortably in GitHub.
- The project does not require relational joins beyond simple merges, so a full RDBMS was unnecessary.
- CSVs maximize transparency and reproducibility.
- Scripts in `clean_data.py` and `integrate_data.py` automatically read/write these files.

This organizational scheme directly supports:
- reproducibility  
- workflow automation  
- data provenance  
