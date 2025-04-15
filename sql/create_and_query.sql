-- This file is optional for documentation, not run by Python
-- Shows schema and queries used

-- Create Table (auto-created by pandas)
-- Query 1
SELECT County, [Median Household Income], [Life Expectancy]
FROM county_health
WHERE [Median Household Income] IS NOT NULL AND [Life Expectancy] IS NOT NULL;

-- Query 2
SELECT County, [Severe Housing Cost Burden], [Diabetes Prevalence]
FROM county_health
WHERE [Severe Housing Cost Burden] IS NOT NULL AND [Diabetes Prevalence] IS NOT NULL;

-- Query 3
SELECT County, [Median Household Income], [Severe Housing Cost Burden]
FROM county_health
WHERE [Median Household Income] IS NOT NULL AND [Severe Housing Cost Burden] IS NOT NULL;
