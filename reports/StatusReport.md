# Status Report (~1000-1500 words)

## Task Updates
An update on each of the tasks described on your project plan including references to specific artifacts in your repository (such as datasets, scripts, workflows, workflow diagrams, etc). → You should include anything you have been working on so far; it doesn't need to be polished, but you should have some code or similar artifacts in the repository, such as datasets, scripts, workflows, workflow diagrams, etc., to support your status updates and demonstrate tangible progress.

note to self: commit crimes dataset (subset - too large right now)

Data Collection and Repo Setup: We downloaded and collected the Chicago Schools and Chicago Crime datasets. Then we verfied formats, ensured overall data integrity, reviewed licensing. Following, we found that the Chicago Crime dataset included crimes from 2011-present which meant the dataset was too large. Our Chicago School dataset is from 2011-2012 so we chose to download a subset of the crime dataset from 2011-2012. Additionally we added folder structure to our Github repository including notebooks/, data/, scripts/, and reports/.

Data Cleaning and basic profiling: We examined the dataset to see what columns are available and the data type for each column. Then we performed missing value analysis, renamed columns for consistency, and focused on a subset of columns as the origina Chicago Schools dataset has 40+ columns. 

Data Integration: We aggregated the Chicago crime data by Ward to calculate total Crime_Count per Ward. We then merged the aggregated crime dataset with the cleaned school dataset using the Ward column. Finally, we verfied the merged dataset for integrity by looking at consistency with our original data and row counts. 

Data Visualization: We generated several plots and visualizations to explore initial relationships, saved within the reports/ folder. This includes a count plot of the Top 10 Primary Crime Types to characterize the local crime environment. We created box plots to compare the distribution of safety scores and reading performance across elementary, middle, and high Schools. Finally, we generated a scatterplot showing the relationship between ward crime count and average student attendance, categorized by school type.

Data Analysis: We completed the initial statistical analysis to quantify the relationships. We ran an OLS regression using crime countsto predict safety score, finding a statistically significant negative coefficient (~ -0.0025$), meaning higher crime is linked to lower safety scores. We computed the overall correlation between crime count and average student attendance (~ -0.426). We also computed a grouped correlation table (code available in notebooks/) to see how the crime/safety relationship varies by school type, finding that the negative correlation is generally strongest for High Schools.

Artifacts: 
* notebooks/data_cleaning_and_integration.ipynb (initial loading, summary statistics, cleaning, and integration of datasets.
* notebooks/
* data/chicago_schools.csv (raw dataset for Chicago schools from 2011-2012)
* NOTE TO SELF: commit crimes dataset (subset - too large right now, also add saving processing dataset in notebook)

Analysis and Visualizations: 

Automation & Python Scripts: Converted cleaning and integration steps into Python scripts for reproducibility. The scripts include reading the raw datasets in, cleaning, merging
Artifacts: scripts/
NOTE TO SELF: need to add this

## Timeline	
An updated timeline indicating the status of each task and when they will be completed (talk about next steps)

* **Week 3-4:** Data cleaning, profiling, initial exploration, check inconsistencies → Isha (completed)
  * artifacts/code to include: raw datasets, notebook with data loading, cleaning, missing value checks basic profiling, etc. (completed)
* **Week 5-6:** Integration (by location & year, handle mismatched schemas) → Isha (completed)
  * artifacts/code to include: Integrated dataset (save cleaned and then integrated dataset), notebook with mapping and joining schema
* **Week 7-8:** Former analysis, first visualizations (scatter plots, bar charts, maps) → Amritha
  * artifacts/code to include: notebook with anaylsis and visualization including summary statistics, bar charts, scatter plots, correlation tables, notes about trends in markdown, etc
* **Week 8-9:** Automate workflow (python scripts), test reproducibility → Isha 
  * artifacts/code to include: add python scripts (.py) underneath script folder
  * our very next step is to take our python scripts and automate the workflow and test reproducibility
* **Week 9-10:** final touches, polish write ups/docs, checking for reproducibility → both
* **Week 11-12:** Submit (Github release, status report updates, and final README) → both

## Changes
A description of any changes to your project plan itself, in particular about your progress so far. Also include changes you made to your plan based on feedback you may have received for Milestone 2.

Originally we planed on integrating on year or location using latitude and longitude. However, we noticed a common column of Ward in both datasets and merged using that to maintain consistency. Feedback we had gotten from our Milestone 2 was to review the licenses/terms of use and review that the dataset met the integration requirements. We found that it ____.
~feedback --> fix licensing explanation part for dataset explaination

## Contributions
Each team member has to write a short summary of their contributions to the current milestone. Each team member should add and commit their contribution summary themselves to the shared github repo.
My contribution (Amritha) for this checkpoint was to start the analysis and create visualizations to understand our dataset better. This included creating visualizations to show the distribution of safety scores and academic performance by school type (ES, MS, HS) and the relationship between average student attendance and ward crime count. Creating this relationship was important to directly address the attendance portion of our first research question. Additionally, I started the statistical analysis, including the OLS regression to predict safety from crime to quantify the strength of the relationships and analyzing the grouped correlation table to see if the crime/safety correlation is significantly different across school types. In the next weeks, I plan to create more visualizations and conduct deeper analysis to find underlying patterns/relationships within both datasets.

