import sqlite3
import pandas as pd
import plotly.express as px

# Load from SQLite
conn = sqlite3.connect("db/ohio_health_data.db")

df_income_life = pd.read_sql("""
SELECT County, [Median Household Income], [Life Expectancy]
FROM county_health
WHERE [Median Household Income] IS NOT NULL AND [Life Expectancy] IS NOT NULL
""", conn)

df_housing_diabetes = pd.read_sql("""
SELECT County, [Severe Housing Cost Burden], [Diabetes Prevalence]
FROM county_health
WHERE [Severe Housing Cost Burden] IS NOT NULL AND [Diabetes Prevalence] IS NOT NULL
""", conn)

df_income_housing = pd.read_sql("""
SELECT County, [Median Household Income], [Severe Housing Cost Burden]
FROM county_health
WHERE [Median Household Income] IS NOT NULL AND [Severe Housing Cost Burden] IS NOT NULL
""", conn)

# Plot 1
fig1 = px.scatter(df_income_life, x="Median Household Income", y="Life Expectancy",
                  text="County", trendline="ols", title="Life Expectancy vs Income")
fig1.show()

# Plot 2
fig2 = px.scatter(df_housing_diabetes, x="Severe Housing Cost Burden", y="Diabetes Prevalence",
                  text="County", trendline="ols", title="Diabetes vs Housing Burden")
fig2.show()

# Plot 3
fig3 = px.scatter(df_income_housing, x="Median Household Income", y="Severe Housing Cost Burden",
                  text="County", trendline="ols", title="Income vs Housing Burden")
fig3.show()
