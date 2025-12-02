# Status Report

## Task Updates
Our team started by downloading the Chicago Schools dataset (2011–2012) and the Chicago Crime dataset (2011–present). Upon reviewing the data, we found that the crime dataset was extremely large, including multiple years beyond the scope of our analysis, and could not be fully uploaded to GitHub due to size limitations. We resolved this by creating a subset of the crime data limited to 2011–2012 and relevant columns (Year, Primary Type, Ward, Latitude, Longitude). This ensures we focus on the period consistent with the school dataset while keeping the repository manageable.

We also verified data integrity by checking file formats, reviewing column types, and confirming that the datasets contained the expected number of rows and columns. Licensing was reviewed to ensure that the datasets were publicly available for research and educational purposes. Both datasets are publicly hosted by the City of Chicago and are under an open data license allowing for non-commercial use. This review ensures compliance with data usage requirements. Also, we established a clear folder structure in our repository for organization and reproducibility:

* notebooks/ for exploratory analysis and initial cleaning scripts
* data/ for raw, processed, and integrated datasets
* scripts/ for automation scripts (.py files)
* reports/ for figures, visualizations, and markdown summaries

Data Cleaning and basic profiling: We examined the dataset to see what columns are available and the data type for each column. Then we performed missing value analysis, renamed columns for consistency, and focused on a subset of columns as the original Chicago Schools dataset has 40+ columns. We narrowed our focus to key columns relevant to safety, attendance, and academic performance. Column names were standardized for consistency (spaces replaced with underscores, % replaced with Percent). For the crime dataset, we filtered for crimes in 2011, removed duplicates, and kept only relevant columns (Primary Type, Ward, Latitude, Longitude). This subset became crime_cleaned.csv. Then we did some basic profiling which included value counts for categorical variables and summary statistics for numeric variables. This step allowed us to detect any inconsistencies and prepare the datasets for integration.

Data Integration: To combine the datasets, we aggregated the crime data by Ward to calculate total Crime_Count per Ward. We then merged this aggregated crime dataset with the cleaned school dataset using the Ward column, creating merged_school_crime.csv. This approach ensured alignment between school locations and crime statistics while maintaining consistency across datasets. We verified the merged dataset by checking row counts and basic summary statistics to confirm that all schools were correctly matched with their corresponding crime counts. The integration process was documented in notebooks/data_cleaning_and_integration.ipynb and later automated in Python scripts (scripts/clean_data.py and scripts/integrate_data.py). These scripts read the raw datasets, clean them, and produce the integrated dataset programmatically, supporting reproducibility.

Data Visualization: We generated several plots and visualizations to explore initial relationships, saved within the reports/ folder. This includes a count plot of the Top 10 Primary Crime Types to characterize the local crime environment. We created box plots to compare the distribution of safety scores and reading performance across elementary, middle, and high Schools. Finally, we generated a scatterplot showing the relationship between ward crime count and average student attendance, categorized by school type. Creating these visualizations are important to allow others to easily understand our analysis and the underlying patterns of the dataset.

Data Analysis: We completed the initial statistical analysis to quantify the relationships. We ran an OLS regression using crime countsto predict safety score, finding a statistically significant negative coefficient (~ -0.0025$), meaning higher crime is linked to lower safety scores. We computed the overall correlation between crime count and average student attendance (~ -0.426). We also computed a grouped correlation table (code available in notebooks/) to see how the crime/safety relationship varies by school type, finding that the negative correlation is generally strongest for High Schools.

Artifacts: 
* notebooks/data_cleaning_and_integration.ipynb (initial loading, summary statistics, cleaning, and integration of datasets.
* notebooks/data_visualizations_and_analysis
* data/chicago_schools.csv (raw dataset for Chicago schools from 2011-2012)

Analysis and Visualizations: To support reproducibility and avoid repeated manual notebook execution, we translated the cleaning and integration steps into Python scripts. These scripts allow any team member or reviewer to replicate the workflow programmatically without needing to run the Jupyter notebook which will be working with during our next steps of the project. 
* scripts/clean_data.py (reads raw datasets, cleans columns, handles missing values, and outputs schools_cleaned.csv and crime_cleaned.csv)
* scripts/integrate_data.py (reads the cleaned datasets, aggregates crime by Ward, merges with school data, and outputs merged_school_crime.csv)

## Timeline	
* **Week 3-4:** Data cleaning, profiling, initial exploration, check inconsistencies → Isha (completed)
  * artifacts/code to include: raw datasets, notebook with data loading, cleaning, missing value checks basic profiling, etc. (completed)
* **Week 5-6:** Integration (by location & year, handle mismatched schemas) → Isha (completed)
  * artifacts/code to include: Integrated dataset (save cleaned and then integrated dataset), notebook with mapping and joining schema
* **Week 7-8:** Former analysis, first visualizations (scatter plots, bar charts, maps) → Amritha (completed)
  * artifacts/code to include: notebook with anaylsis and visualization including summary statistics, bar charts, scatter plots, correlation tables, notes about trends in markdown, etc
* **Week 8-9:** Automate workflow (python scripts), test reproducibility → Isha 
  * artifacts/code to include: add python scripts (.py) underneath script folder
  * our very next step is to take our python scripts and automate the workflow and test reproducibility
* **Week 9-10:** final touches, polish write ups/docs, checking for reproducibility → both
* **Week 11-12:** Submit (Github release, status report updates, and final README) → both

Next steps include furthering analysis if it seems necessary, automating the workflow using the Python scripts, verifying that the scripts reproduce the exact cleaned and merged datasets, and expanding the analysis with additional visualizations and statistical tests.

## Changes
Originally, we planned to integrate datasets using location coordinates (latitude/longitude) or year. During implementation, we discovered that both datasets contained a common Ward column, which provided a more reliable and consistent method for merging for the datasets. Feedback from Milestone 2 also requested that we review dataset licensing. Upon review of the Chicago Data Portal, we confirmed that both the Chicago Schools dataset and the Chicago Crime dataset are subject to the Chicago Data Portal Terms of Use, which allow use of the datasets for research, education, and non commercial purposes. By following these terms, we ensured that our work complies with licensing requirements. Additionally, the original crime dataset was too large to include entirely so we created a subset for 2011–2012 for processing and reproducibility.

## Contributions
Isha:
Contributions for this milestone focused on data cleaning, integration, and automation. I examined both the Chicago Schools and Crime datasets, performing missing value analysis, renaming columns for consistency, and focusing on relevant subsets of columns. I then aggregated crime data by Ward and merged it with the cleaned school dataset to create an integrated dataset for analysis. To support reproducibility for future steps, I converted these steps into Python scripts (clean_data.py and integrate_data.py), which reads the raw datasets, cleans and processes them, and generates the merged dataset automatically. I also verified dataset integrity and documented the cleaning and integration workflow in the repository.

Amritha:
Contributions for this checkpoint was to start the analysis and create visualizations to understand our dataset better. This included creating visualizations to show the distribution of safety scores and academic performance by school type (ES, MS, HS) and the relationship between average student attendance and ward crime count. Creating this relationship was important to directly address the attendance portion of our first research question. Additionally, I started the statistical analysis, including the OLS regression to predict safety from crime to quantify the strength of the relationships and analyzing the grouped correlation table to see if the crime/safety correlation is significantly different across school types. In the next weeks, I plan to create more visualizations and conduct deeper analysis to find underlying patterns/relationships within both datasets.
