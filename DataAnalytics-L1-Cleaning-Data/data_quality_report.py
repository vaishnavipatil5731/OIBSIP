
import pandas as pd
from pathlib import Path

# Define the dataset path
DATA_PATH = Path("data/titanic.csv")

# Check whether the dataset exists
if not DATA_PATH.exists():
    print("ERROR: titanic.csv was not found!")
    print("Please save the dataset inside the data folder.")
    raise SystemExit

# Load the dataset
df = pd.read_csv(DATA_PATH)

print("=" * 60)
print("OASIS INFOBYTE - DATA CLEANING PROJECT")
print("INITIAL DATA QUALITY REPORT")
print("=" * 60)

# 1. Dataset size
print("\n1. DATASET SHAPE")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

# 2. Column names and data types
print("\n2. COLUMN DATA TYPES")
print(df.dtypes)

# 3. Missing values
print("\n3. MISSING VALUES PER COLUMN")
print(df.isnull().sum())

# 4. Duplicate rows
print("\n4. DUPLICATE ROWS")
print(f"Duplicate rows: {df.duplicated().sum()}")

# 5. Numerical summary
print("\n5. NUMERICAL SUMMARY")
print(df.describe().round(2))

# 6. Categorical summary
print("\n6. CATEGORICAL SUMMARY")
print(df.describe(include="object"))

# 7. Unique values in each column
print("\n7. UNIQUE VALUES")
print(df.nunique())

# 8. Save the quality report
Path("output").mkdir(exist_ok=True)

with open("output/data_quality_report.txt", "w", encoding="utf-8") as file:
    file.write("OASIS INFOBYTE - INITIAL DATA QUALITY REPORT\n")
    file.write("=" * 50 + "\n\n")
    file.write(f"Rows: {df.shape[0]}\n")
    file.write(f"Columns: {df.shape[1]}\n\n")
    file.write("DATA TYPES\n")
    file.write(df.dtypes.to_string() + "\n\n")
    file.write("MISSING VALUES\n")
    file.write(df.isnull().sum().to_string() + "\n\n")
    file.write(f"Duplicate rows: {df.duplicated().sum()}\n\n")
    file.write("NUMERICAL SUMMARY\n")
    file.write(df.describe().round(2).to_string() + "\n\n")
    file.write("UNIQUE VALUES\n")
    file.write(df.nunique().to_string() + "\n")

print("\nReport saved to output/data_quality_report.txt")
print("\nInitial data-quality inspection completed!")
