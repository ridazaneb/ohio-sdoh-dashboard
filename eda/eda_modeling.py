import pandas as pd
import sqlite3
import os

# Load Excel data
excel_path = os.path.join("data", "2024_County_Health_Ohio_Data.xlsx")
data = pd.read_excel(excel_path, sheet_name="Additional Measure Data")

# Relevant columns
cols = [
    "Unnamed: 2", "Life Expectancy", "% Not Proficient in English", "% Female",
    "% Rural", "% Non-Hispanic White", "% Hispanic"
]
income_cols = [c for c in data.columns if 'income' in str(c).lower()]
housing_cols = [c for c in data.columns if 'housing' in str(c).lower()]
disease_cols = [c for c in data.columns if 'diabetes' in str(c).lower() or 'obesity' in str(c).lower()]
final_cols = list(set(cols + income_cols + housing_cols + disease_cols))

df = data[final_cols].rename(columns={"Unnamed: 2": "County"})
df = df.dropna(subset=["County"])
for col in df.columns:
    if col != "County":
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Save to SQLite
conn = sqlite3.connect("db/ohio_health_data.db")
df.to_sql("county_health", conn, if_exists="replace", index=False)
print("✅ Data saved to db/ohio_health_data.db")
