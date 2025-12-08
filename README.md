# IS-477-project
## Exploring the Relationship Between School Performance and Neighborhood Crime in Chicago


## Contributors
* Isha Koradiya
* Amritha Barani 

## Summary
This project investigates the relationship between Chicago public school performance indicators, such as safety score, reading performance, attendance, and neighborhood crime patterns. Specifically we are looking at how school attendance and academic performance relate to crime patterns in surrounding neighborhoods, and how perceived school safety correlate with local crime rates? Our motivation stems from the idea that school environments are heavily impacted by surrounding neighborhood conditions, particularly crime levels, which could influence perceived safety, educational outcomes, and student engagement. Understanding this relationship is valuable for policymakers, educators, and city planners aiming to improve community well-being. We analyze two publicly available datasets from the Chicago Open Data Portal:
1. Chicago Public Schools – Progress Report Cards (2011–2012)
2. Crimes – 2001 to Present (filtered to 2011)

These datasets contains supporting information such as school characteristics and performance data, and incident level crime records. To answer our central research questions, we narrowed the crime dataset to 2011, the year overlapping with the school dataset, and then aggregated crime counts by Ward. We then merged school performance data with crime totals to explore correlations and trends.

We conducted data cleaning, profiling, integration, visualization, and statistical modeling. Missing data, inconsistent column names, and the size of the crime dataset were key challenges. We resolved these through systematic filtering, renaming, and automation scripts for full reproducibility.

Our analyses reveal meaningful relationships. Safety Score shows a moderately negative correlation with neighborhood crime count (about –0.43). OLS regression confirms crime count as a statistically significant predictor of Safety Score, though with a modest effect size (coefficient ~ –0.0025). Reading performance also tends to decrease as crime increases, though the relationship is weaker. Average student attendance shows a negative correlation with crime as well (about –0.31), suggesting neighborhood conditions may influence school engagement. We also observe that these relationships vary by school type (ES/MS/HS).

All data processing and analysis steps are fully automated through a single script (run_workflow.py) to support reproducibility. This project demonstrates the complete data lifecycle and highlights the importance of transparent and well documented data practices.

## Data profile: [500-1000 words] Description of each dataset used including all ethical/legal constraints.
also add --> Documentation describing steps someone else would use to acquire data, including checksums. This is particularly important if your data cannot be redistributed. (Where each dataset comes from, the URLs (you already have them), any licensing/ethical info, the fact your workflow uses programmatic acquisition, explanation of SHA-256 checksums and why they matter, how someone would normally download the data manually if needed)

Licensing:
The datasets used in this project are provided by the City of Chicago Data Portal and are subject to the Chicago Data Portal Terms of Use, which allow reuse for research and educational purposes. All software written for this project ... ADD TO THIS 

## Data quality

**Filesystem Organization**
Our project required a structured approach to storing, cleaning, and assessing the quality of the datasets. To support future reproducibility, we used a consistent filesystem organization that seperates raw, processed, and merged data. The raw dataset was downloaded directly from a Chicago Data Portal and chose a simple folder based CSV structure rather than a relational database because our cleaning and integration steps were straightfroward enought to be performed using pandas. This filesystem layout also supports automated workflows using our run_workflow script, which relies on predictable file paths. 

**Quality assessment and Findings**
Assessing the quality of the Chicago schools and 2011 crime datasets was an essential part of preparing the data for integration and later analysis. Both datasets come from the Chicago Open Data Portal so they were relatively well structured but still contained general inconsistencies regarding missing values, redundant information, and formatting issues that required cleaning. Before cleaning the 2011 crime dataset contained over 350,000 records. The initial profiling process involved generating summary statistics, inspecting column types, checking for missingness, and evaluating internal consistency and several quality issues were revealed. The dataset has some missing spatial data as well and specifically, 741 records lacked Latitude, Longitude, X Coordinate, and Y Coordinate values. The geographic information is foundational for understanding the distribution of crime, and because the Ward level aggregation depended on these fields, keeping records without coordinates would risk skewing the spatial summaries. Similarly, 14 records were missing the Ward attribute, making them unusable for the project's integration goals. In total, these rows were removed. We also identified 322 missing values in the "Location Description" field. Though this attribute was not required for integration or analysis, so we excluded this column from the subset. The crime dataset also contained duplicate rows, which were removed using a full duplicate drop. After these cleaning steps, the dataset contained no missing values in any of the columns used for aggregation or merging. The final cleaned dataset consisted of four variables essential to our aims: Crime_Type, Ward, Latitude, and Longitude.

The schools dataset originally contained 566 rows and 79 columns. The initial quality assessment revealed both structural and completeness issues. Many column names contained spaces, punctuation, inconsistent symbols (such as %), and trailing whitespace. To fix this we cleaned up the columns to ensure proper formatting. In terms of completeness, the dataset exhibited substantial missing values in several educational performance indicators. Because these fields were important to the research question examining our research questions, the rows lacking values for any of these variables were removed.  After cleaning, we checked the compatibility between the two datasets for the merging process. The integration relied on Ward as the common key. Originally we thought to integrate using latitude and longitude, but this method raised concerns about misalignment. Using Ward as the key provided better interpretible results and reduced possible error. Before merging, we verified that Ward values were consistently formatted in both datasets and fell within expected numerical ranges. The left join ensured that every school remained represented, even if a Ward had unusually low or missing crime counts. After merging we made checked the quality by verifying row counts and examining basic summary statistics to confirm that no values were unintentionally changed or duplicated during integration. 

In the end the quality assessment process showed that both of the datasets required straightforward cleaning. The majority of issues were related to missing values, inconsistent column naming, and structural formatting rather than real inaccuracies or problematic records. After cleaning both of the datasets had consistency and completeness for all key variable. It also ensured that the final analysis for the relationship between crime levels and school performance were based on reliable and interpretable data. 

## Data Integration
The data integration process required choosing the best way to join datasets representing  different the entities of individual crime incidents and individual schools. Originally, we considered joining datasets by geographic proximity (latitude/longitude), but this approach introduced unnecessary complexity and uncertainty. Instead, we chose Ward as the integration key because both datasets contained it, and Ward level crime aggregation aligned with our goal to examine neighborhood level safety trends. We grouped the crime dataset by Ward to compute total crime counts and then merged this aggregated dataset with the cleaned schools dataset using a left join. The left join ensured that every school remained represented, even if a Ward had unusually low or missing crime counts. After integration, we validated the dataset by checking row counts, summary statistics, and null values to verify that no rows were unintentionally dropped and that crime totals aligned with expectations.


## Findings: [~500 words] Description of any findings including numeric results and/or visualizations.
also add --> data viz and analysis documentation
plots generated, methods used (count plot, scatter plot, boxplot, OLS regression, correlations, grouped correlations), why we chose these methods, patterns or statistical results were observed and what this all means

## Future work
A​‍​‌‍​‍‌​‍​‌‍​‍‌n important lesson learn during this project was the importance of selecting an appropriate spatial unit for data integration. At first, we wanted to use the geographic coordinates (latitude and longitude) for a proximity join between the schools and crimes datasets. However, it also faced a problem that was computationally complex and could result in errors in the coordinates of the raw datasets. Instead, we used a Ward-level integration to get a reliable and consistent primary key for merging datasets. However, we found that Wards are administrative boundaries, which may not necessarily be the immediate neighborhood environment a student navigates daily.

Additionally, working with the "Crimes - 2001 to Present" dataset was an important lesson in understanding how to handle large-scale data. Since the size of the raw data was very large, we needed to focus on filtering and profiling at early stages of the data lifecycle to avoid memory-related issues during the integration process. It also emphasized the need for defensive cleaning scripting as seen in the situation where the Average_Student_Attendance column, originally an object due to the percentage signs, was standardized.

In the future, there are many ways to broaden this study to offer better and more detailed insights. Future versions of this work may consider not using the Wards-level aggregation and instead look into buffer-based geospatial analysis. By creating a 1-mile or 500-meter radius "safety buffer" specifically around each school’s exact coordinates, we could quantify the specific incidents of crime affecting a student's commute and immediate school grounds. This change would allow for a local view of neighborhood safety as opposed to district-wide Ward data currently allows. Furthermore, using control variables such as local unemployment rates can be a baseline for economic conditions for a complex OLS regression analysis that can be done to establish if crime is the primary predictor of school safety scores or if both variables are driven by systemic socioeconomic factors.

Another future step to consider is to incorporate data spanning a longer time period to conduct a longitudinal study. This research focuses on the 2011-2012 school year due to the availability of the progress reports. Tracking school performance and attendance alongside changing crime patterns over the course of a decade would enable researchers to analyze whether educational improvements correlate with improved neighborhood safety outcomes. By examining these trends over several years, the analysis could be used to create a predictive model. This model can be useful for policymakers to identify schools that may need additional safety resources or support based on real-time neighborhood data. In addition, expanding the scope of the study to include qualitative perspectives such as parent, teacher, or stakeholder interviews could provide a more human-centered understanding of how neighborhood crime influences school culture and student well-being. Collecting this qualitative information would help by offering more context that would not be understood solely by the numerical datasets and analysis. This would help ensure that student safety and academic performance are addressed through data analysis.

## Reproducing
**Workflow Overview**

This project uses a scripted end-to-end workflow to ensure full reproducibility. The workflow consists of four stages, each handled by a specific Python script:

1. Data Acquisition/Collection (acquire_data.py)
Downloads the raw Chicago Schools and Crime datasets automatically using stable public URLs, verifies integrity with SHA-256 checksums, and stores the files in data/raw/.
2. Data Cleaning/Profiling (clean_data.py)
Loads the raw datasets, selects relevant variables, handles missing values, standardizes column names, and outputs cleaned datasets into data/processed/.
3. Data Integration (integrate_data.py)
Aggregates crime counts by ward and merges them with the cleaned school dataset, producing a unified dataset (merged_school_crime.csv).
4. Analysis + Visualization (analyze_data.py)
Generates all figures, statistical summaries, and text outputs, saving them into the figures/ directory.

**Reproducibility and Transparency**

To reproduce these results you have to clone the GitHub repository: git clone https://github.com/ishakoradiya1/IS-477-project

1. Install dependencies using requirements.txt
    * pip install -r requirements.txt
2. Run the full workflow using:
    * python3 scripts/run_workflow.py
3. Running the full workflow will:
    * Download the raw Chicago Schools and Chicago Crime datasets automatically using the URLs in acquire_data.py
        * Schools: https://data.cityofchicago.org/api/views/9xs2-f89t/rows.csv
        * Crimes: https://data.cityofchicago.org/api/views/ijzp-q8t2/rows.csv?where=year=2011
    * Clean the datasets (clean_data.py)
    * Integrate the datasets (integrate_data.py)
    * Generate all final processed data and visualizations (analyze_data.py)

All generated outputs will appear in:
* data/processed/
* figures/
* checksums.txt (project root)

Optional: accessing output data archive - download all processed datasets and figures from: (https://uofi.box.com/s/56t7ofh4sb2nhkaifiojl3k1q9zkqd39) and place them in the project directory exactly as:
* data/processed/ (place all processed CSVs here)
* figures/ (place all PNG's + textoutputs here)
* checksums.txt (place in project root directory) 
These files match what the workflow will generate.

## References: Formatted citations for any papers, datasets, or software used in your project.

Box link to output data: https://uofi.box.com/s/56t7ofh4sb2nhkaifiojl3k1q9zkqd39

Last things to add:
Licenses for data and software created as part of your project

Final artifact to add:
Metadata and data documentation 
Data dictionary or codebook as text file, PDF, or self-describing data formats.
Descriptive metadata describing your project in conformance with a standard such as DataCite, Schema.org.

