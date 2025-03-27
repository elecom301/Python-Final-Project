#Programming Final Project: Analyzing the Relationship between Health Expenditure and Malnutrition Death Rate
#By: Elena Comellas

#This script analyzes the impact of healthcare expenditure on malnutrition death rates by GDP level using 2021 data. Regression results and heteroscedasticity tests are included.

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.iolib.summary2 import summary_col

# Load datasets
death_rate = pd.read_csv("death-rate-from-malnutrition-ghe.csv")
healthcare_expenditure = pd.read_csv("total-healthcare-expenditure-gdp.csv")
gdp_data = pd.read_csv("gdp-per-capita-worldbank.csv")

# Select and rename relevant columns
death_rate = death_rate[['Entity', 'Year', 'Death rate from protein-energy malnutrition among both sexes']]
death_rate.columns = ['Country', 'Year', 'Malnutrition_Death_Rate']

healthcare_expenditure = healthcare_expenditure[['Entity', 'Year', 'Current health expenditure (CHE) as percentage of gross domestic product (GDP) (%)']]
healthcare_expenditure.columns = ['Country', 'Year', 'Health_Expenditure_GDP']

gdp_data = gdp_data[['Entity', 'Year', 'GDP per capita, PPP (constant 2021 international $)']]
gdp_data.columns = ['Country', 'Year', 'GDP_per_capita']

# Merge datasets
data = pd.merge(death_rate, healthcare_expenditure, on=['Country', 'Year'])
data = pd.merge(data, gdp_data, on=['Country', 'Year'])

# Filter for 2021 and drop missing values
data_2021 = data[data['Year'] == 2021].dropna()

# Group countries by GDP tertiles
data_2021['GDP_Group'] = pd.qcut(data_2021['GDP_per_capita'], 3, labels=['Low-GDP', 'Medium-GDP', 'High-GDP'])

# Summary statistics
print("Overall Summary Statistics:")
print(data_2021[['Malnutrition_Death_Rate', 'Health_Expenditure_GDP', 'GDP_per_capita']].describe())

# Group-wise summaries
for group in ['Low-GDP', 'Medium-GDP', 'High-GDP']:
    print(f"\nSummary for {group}:")
    print(data_2021[data_2021['GDP_Group'] == group][['Malnutrition_Death_Rate', 'Health_Expenditure_GDP']].describe())

# Histograms
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.histplot(data_2021['Malnutrition_Death_Rate'], bins=20, color='skyblue')
plt.title("Histogram: Malnutrition Death Rate")

plt.subplot(1, 2, 2)
sns.histplot(data_2021['Health_Expenditure_GDP'], bins=20, color='lightgreen')
plt.title("Histogram: Health Expenditure (% of GDP)")
plt.tight_layout()
plt.show()

# Boxplots
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.boxplot(y=data_2021['Malnutrition_Death_Rate'], color='skyblue')
plt.title("Boxplot: Malnutrition Death Rate")

plt.subplot(1, 2, 2)
sns.boxplot(y=data_2021['Health_Expenditure_GDP'], color='lightgreen')
plt.title("Boxplot: Health Expenditure (% of GDP)")
plt.tight_layout()
plt.show()

# Scatter plot by GDP Group
sns.lmplot(data=data_2021, x='Health_Expenditure_GDP', y='Malnutrition_Death_Rate', hue='GDP_Group', height=5, aspect=1.5)
plt.title('Scatter: Health Expenditure vs Malnutrition Death Rate (2021)')
plt.show()

# Run OLS regressions for each group
results = {}
for group in ['Low-GDP', 'Medium-GDP', 'High-GDP']:
    subset = data_2021[data_2021['GDP_Group'] == group]
    model = smf.ols('Malnutrition_Death_Rate ~ Health_Expenditure_GDP', data=subset).fit(cov_type='HC0')
    results[group] = model

# Display regression results
summary = summary_col([results['Low-GDP'], results['Medium-GDP'], results['High-GDP']],
                      stars=True,
                      model_names=['Low-GDP', 'Medium-GDP', 'High-GDP'],
                      info_dict={'N':lambda x: f"{int(x.nobs)}",
                                 'R2':lambda x: f"{x.rsquared:.2f}"})
print(summary)

# Breusch-Pagan test
print("\nBreusch-Pagan Test Results:")
for group in ['Low-GDP', 'Medium-GDP', 'High-GDP']:
    model = results[group]
    bp_test = het_breuschpagan(model.resid, model.model.exog)
    labels = ['LM Statistic', 'LM-Test p-value', 'F-Statistic', 'F-Test p-value']
    print(f"\n{group} Group:")
    for label, stat in zip(labels, bp_test):
        print(f"{label}: {stat:.4f}")
