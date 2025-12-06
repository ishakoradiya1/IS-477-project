"""
Run the full end-to-end workflow for the IS 477 project.

This script automates:
1. Data acquisition
2. Data cleaning
3. Data integration
4. Data analysis and visualization

Usage:
    python scripts/run_workflow.py
"""

import acquire_data
import clean_data
import integrate_data
import analyze_data

def main():
    print(" STEP 1 — Acquire Raw Data ")
    acquire_data.main() if hasattr(acquire_data, "main") else None

    print(" STEP 2 — Clean Raw Data ")
    clean_data.clean_schools()
    clean_data.clean_crime()

    print(" STEP 3 — Integrate Cleaned Datasets ")
    integrate_data.merge_datasets()

    print(" STEP 4 — Analyze + Visualize Results ")
    analyze_data.main()

    print(" WORKFLOW COMPLETE ")
    print("All outputs generated in data/processed/ and figures/\n")

if __name__ == "__main__":
    main()
