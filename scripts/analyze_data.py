import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import os

FIG_DIR = "../figures"
os.makedirs(FIG_DIR, exist_ok=True)

def main():
    schools_cleaned = pd.read_csv("../data/processed/schools_cleaned.csv")
    crime_cleaned = pd.read_csv("../data/processed/crime_cleaned.csv")
    merged = pd.read_csv("../data/processed/merged_school_crime.csv")

    # 1. Top 10 Crime Types
    top_crime = crime_cleaned['Crime_Type'].value_counts().nlargest(10).index
    crime_top_10 = crime_cleaned[crime_cleaned['Crime_Type'].isin(top_crime)]

    plt.figure(figsize=(6, 4))
    sns.countplot(data=crime_top_10, y='Crime_Type', order=top_crime)
    plt.title('Top 10 Crime Types in Chicago (2011)')
    plt.xlabel('Number of Incidents')
    plt.ylabel('Crime Type')
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/top_10_crime_types.png")
    plt.close()


    # 2. Boxplots by School Type
    merged = merged.rename(columns={'Elementary,_Middle,_or_High_School': 'School_Type'})

    # Safety Score Boxplot
    plt.figure(figsize=(6, 4))
    sns.boxplot(data=merged, x='School_Type', y='Safety_Score', palette='Set2')
    plt.title('Safety Score Distribution by School Type')
    plt.xlabel('School Type')
    plt.ylabel('Safety Score')
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/safety_score_by_school_type.png")
    plt.close()

    # Reading Performance Boxplot
    plt.figure(figsize=(6, 4))
    sns.boxplot(data=merged, x='School_Type', y='ISAT_Exceeding_Reading_Percent', palette='Set2')
    plt.title('Reading Performance Distribution by School Type')
    plt.xlabel('School Type')
    plt.ylabel('ISAT Exceeding Reading Percent')
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/reading_performance_by_school_type.png")
    plt.close()

    # 3. Regression — Safety Score vs Crime Count
    X = merged[['Crime_Count']]
    X = sm.add_constant(X)
    y = merged['Safety_Score']

    model = sm.OLS(y, X).fit()

    # Save regression summary
    with open(f"{FIG_DIR}/regression_safety_score.txt", "w") as f:
        f.write(model.summary().as_text())

    print("Regression model saved to regression_safety_score.txt")

    # 4. Attendance vs Crime Count
    # Convert attendance to numeric
    merged['Average_Student_Attendance'] = (
        merged['Average_Student_Attendance']
        .astype(str)
        .str.replace('%', '', regex=False)
        .astype(float)
    )

    plt.figure(figsize=(6, 4))
    sns.scatterplot(
        data=merged,
        x='Crime_Count',
        y='Average_Student_Attendance',
        hue='School_Type'
    )
    plt.title("Attendance vs. Ward Crime Count (2011)")
    plt.xlabel("Ward Crime Count (2011)")
    plt.ylabel("Average Student Attendance (%)")
    plt.legend(title="School Type")
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/attendance_vs_crime.png")
    plt.close()

    attendance_corr = merged['Average_Student_Attendance'].corr(merged['Crime_Count'])

    with open(f"{FIG_DIR}/attendance_correlation.txt", "w") as f:
        f.write(f"Correlation between attendance and crime count: {attendance_corr:.3f}")

    print("Attendance correlation saved to attendance_correlation.txt")

    # 5. Grouped Correlations
    grouped_corr = merged.groupby('School_Type')[
        ['Safety_Score', 'ISAT_Exceeding_Reading_Percent', 'Crime_Count']
    ].corr()

    with open(f"{FIG_DIR}/grouped_correlations.txt", "w") as f:
        f.write(str(grouped_corr))

    print("Grouped correlations saved to grouped_correlations.txt")

if __name__ == "__main__":
    main()
