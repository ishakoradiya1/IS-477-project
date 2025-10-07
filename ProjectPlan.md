# Project Plan

## Overview
The overall goal of this project is to explore the relationship between public school performance, student attendance, and crime in surrounding neighborhoods in Chicago. We aim to investigate how educational outcomes and perceived school safety relate to local crime patterns, and whether school type, such as elementary, middle school, high school, influences these relationships. Understanding the link between school performance and neighborhood crime can be useful, as it can help inform policymakers, educators, and community planners about potential areas to intervene in and improve. Overall, the project also provides a real-world application for demonstrating the full data lifecycle, from data acquisition and integration to visualization and reproducibility.

## Research Questions
The research questions we aim to explore investigate the relationship between the crime variables and school academic performance-related variables. Specifically, we are trying to address:
1. How do school attendance and academic performance relate to crime patterns in surrounding neighborhoods?
2. Does perceived school safety correlate with local crime rates?

## Team
Our team consists of two members, and we will together contribute to project planning, status reporting, and final report preparation. One of the members (Isha) will work on data acquisition, which will include the process of collecting datasets through APIs or CSV downloads based on what is appropriate. Additionally, this member will establish file organization and storage systems such as CSVs and/or SQLite databases. The other team member (Amritha) will then do data cleaning & integrations. So they will handle data quality, handle missing/inconsistent values, and integrate school and crime datasets by location and year, creating a consistent subset. The first member (Isha) will then switch off and work on analysis/visualization and create visualizations, such as scatter plots, bar charts, interactive maps, and implement interactivity features as necessary. Both members will maintain clear documentation of our data sources, code, and analysis to ensure reproducibility. Finally, both of the members will also work on any final issues, make edits, and complete the final project report together.

## Datasets
The datasets we plan to use are both from the ‘City of Chicago Data Portal.’ The first dataset we found is called Chicago Public Schools - Progress Report Cards (2011 - 2012). The download for this dataset is available in both CSV or API. There are 566 rows (each row is a school) and 79 columns in total. The key fields included in this dataset are School Name, School Type, Street Address, Attendance Rate, Reading/Math Performance Scores, Average Student Attendance. Accessibility to this data sent requires no consent as it is from a public open data portal. The original data is provided by Chicago Public Schools and was last updated September 12, 2018. Possible challenges that might be encountered using this dataset is that there is missing data, requires cleaning, and consistent formatting. 
The second dataset we are exploring is ‘Crimes - 2001 to Present’ and the dataset is available in formats of CSV or API. The dataset has 352K rows, with each row representing a crime record and 19 columns in total. The key fields included in this dataset are ID, Date, Block, Primary Type, Arrest, X and Y Coordinates. This dataset is accessible through a public open data portal. The original data is provided by the Chicago Police Department and is updated daily. Potential challenges that may be encountered when working with this dataset include its size, its a large dataset and will require filtering by year or neighborhood for a subset of the original dataset. 
1. Chicago Public Schools - Progress Report Cards (2011 - 2012): https://data.cityofchicago.org/Education/Chicago-Public-Schools-Progress-Report-Cards-2011-/9xs2-f89t/about_data
2. Crimes - 2001 to Present: https://data.cityofchicago.org/Public-Safety/Crimes-2011/qnrb-dui6/about_data

## Timeline	
Our current plan for the timeline for implementing our project starts with collecting the datasets, setting up the repo, verifying data integrity, and organizing folders during week 1-2, which was completed by Isha. Our future timeline will be:
- **Week 3-4:** Data cleaning, profiling, initial exploration, check inconsistencies → Amritha
- **Week 5-6:** Integration (by location & year, handle mismatched schemas) → Isha
- **Week 7-8:** Former analysis, first visualizations (scatter plots, bar charts, maps) → Amritha
- **Week 8-9:** Automate workflow (python scripts), test reproducibility → Isha
- **Week 9-10:** final touches, polish write ups/docs, checking for reproducibility → both
- **Week 11-12:** Submit (github release, status report updates, and final README) → both

## Constraints
Current constraints and challenges we plan to encounter are dataset size. Our first dataset has data within the time frame 2011-2012 while our second dataset is extremely large with updates daily. To solve this problem we are planning on filtering and using a consistent range for years for our subset of the second larger dataset. We will also have to look into handling missing values properly and fixing formatting consistencies especially for variables like addresses, coordinates, etc. Additionally, we have to think about how the data is public, as both datasets are publicly available under open data licenses provided by the City of Chicago, and no personally identifiable information is present. However, each row represents an individual school (not individual students) so we might need to discuss privacy/confidentiality for school level data and ensure overall ethical handling by documenting data sources. 

## Gaps
Some current gaps we have found include our uncertainty in how to efficiently integrate the two datasets, especially when matching schools to the surrounding crime data by location. We are still considering whether to use coordinates, zip code, or community areas to accurately match the two datasets together. Another gap is creating documentation for data acquisition and integration to ensure others can reproduce our steps and results, as well as considering how much detail to include in the documentation. Additionally, we need additional input on how to implement workflow automation for our project, including how to best combine a Snakemake workflow with a “Run All” script. As we carry out this project, we expect to receive additional input and address these gaps. 
