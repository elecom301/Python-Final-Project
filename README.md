readme_text_updated = """
# Programming Final Project: Analyzing the Relationship between Health Expenditure and Malnutrition Death Rate

**By: Elena Comellas**

This project explores the relationship between healthcare expenditure and malnutrition death rates across countries in 2021. Countries are grouped by GDP per capita into low-, medium-, and high-income categories to identify how the relationship may vary by income level. The analysis includes summary statistics, visualizations, regression models, and heteroskedasticity testing.

---

## Files in This Repository
- `main.py`: Python script that performs the full analysis
- `death-rate-from-malnutrition-ghe.csv`: Malnutrition death rate data
- `total-healthcare-expenditure-gdp.csv`: Healthcare expenditure data
- `gdp-per-capita-worldbank.csv`: GDP per capita data

---

## Project Overview

- **Objective:** Assess how healthcare spending is associated with malnutrition death rates and whether this association differs by GDP level.
- **Dataset Year:** 2021
- **Tools used:** Python (matplotlib, seaborn, statsmodels, etc.)

---

## How to Run

1. Clone or download this repository.
2. Ensure the required CSV files are in the same directory as `main.py`.
3. Open `main.py` in an IDE or terminal and run the script.

---

## Analysis Breakdown

- **Data Preparation:**
  - Selection and renaming of relevant columns
  - Merging data from three datasets on country and year
  - Filtering for 2021 and handling missing values
  - Categorizing countries by GDP tertiles

- **Descriptive Statistics:**
  - Summary statistics overall and by GDP group

- **Visualizations:**
  - Histograms and boxplots for malnutrition death rate and health expenditure
  - Scatter plots with regression lines by GDP group

- **Regression Analysis:**
  - OLS regressions by GDP group to estimate relationship
  - Breusch-Pagan test to assess heteroskedasticity in residuals

---

## Outputs

- Summary statistics and GDP group-wise insights
- Visual representation of variable distributions and trends
- Regression models with robust standard errors
- Heteroskedasticity test results

---

## Author

Elena Comellas  
Python Final Project  
March 2025
"""

with open("README.md", "w") as f:
    f.write(readme_text_updated)

readme_text_updated.splitlines()[:10]  # Preview updated lines
