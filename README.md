# IS-477-project
## Exploring the Relationship Between School Performance and Neighborhood Crime in Chicago

## Contributors 
* Isha Koradiya
* Amritha Barani 

* Title: Title of your project
* Contributors: Bulleted list of contributors (with optional ORCIDs).

# Summary: [500-1000 words] Description of your project, motivation, research question(s), and any findings.
This project investigates the relationship between Chicago public school performance indicators, such as safety score, reading performance, attendance, and neighborhood crime patterns. Our motivation stems from the idea that school environments are heavily impacted by surrounding neighborhood conditions, particularly crime levels, which could influence perceived safety, educational outcomes, and student engagement. Understanding this relationship is valuable for policymakers, educators, and city planners aiming to improve community well-being. We analyze two publicly available datasets from the Chicago Open Data Portal:
1. Chicago Public Schools – Progress Report Cards (2011–2012)
2. Crimes – 2001 to Present (filtered to 2011)

These datasets contains supporting information such as school characteristics and performance data, and incident level crime records. To answer our central research questions, we narrowed the crime dataset to 2011, the year overlapping with the school dataset, and then aggregated crime counts by Ward. We then merged school performance data with crime totals to explore correlations and trends.

We conducted data cleaning, profiling, integration, visualization, and statistical modeling. Missing data, inconsistent column names, and the size of the crime dataset were key challenges. We resolved these through systematic filtering, renaming, and automation scripts for full reproducibility.

Our analyses reveal meaningful relationships. Safety Score shows a moderately negative correlation with neighborhood crime count (about –0.43). OLS regression confirms crime count as a statistically significant predictor of Safety Score, though with a modest effect size (coefficient ~ –0.0025). Reading performance also tends to decrease as crime increases, though the relationship is weaker. Average student attendance shows a negative correlation with crime as well (about –0.31), suggesting neighborhood conditions may influence school engagement. We also observe that these relationships vary by school type (ES/MS/HS).

All data processing and analysis steps are fully automated through a single script (run_workflow.py) to support reproducibility. This project demonstrates the complete data lifecycle and highlights the importance of transparent and well documented data practices.

# Data profile: [500-1000 words] Description of each dataset used including all ethical/legal constraints.
# Data quality: [500-1000 words] Summary of the quality assessment and findings.
# Findings: [~500 words] Description of any findings including numeric results and/or visualizations.
# Future work: [~500-1000 words] Brief discussion of any lessons learned and potential future work.
# Reproducing: Sequence of steps required for someone else to reproduce your results.
# References: Formatted citations for any papers, datasets, or software used in your project.

Box link to output data: https://uofi.box.com/s/56t7ofh4sb2nhkaifiojl3k1q9zkqd39

Last things to add:
Licenses for data and software created as part of your project

Final artifact to add:
Metadata and data documentation 
Data dictionary or codebook as text file, PDF, or self-describing data formats.
Descriptive metadata describing your project in conformance with a standard such as DataCite, Schema.org.

