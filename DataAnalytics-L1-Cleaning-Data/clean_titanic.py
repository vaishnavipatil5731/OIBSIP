
import pandas as pd
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "titanic.csv"
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("OASIS INFOBYTE - DATA CLEANING")
print("-" * 45)

# 1. Load dataset
df = pd.read_csv(DATA_FILE)
original = df.copy()

print("\nBEFORE CLEANING")
print({
    "Rows": len(original),
    "Columns": len(original.columns),
    "Missing values": int(original.isnull().sum().sum()),
    "Duplicate rows": int(original.duplicated().sum())
})

# 2. Define intended data types
before_expected_types = {
    "PassengerId": "string",
    "Survived": "int64",
    "Pclass": "int64",
    "Name": "str",
    "Sex": "string",
    "Age": "float64",
    "SibSp": "int64",
    "Parch": "int64",
    "Ticket": "str",
    "Fare": "float64",
    "Cabin": "str",
    "Embarked": "string"
}

# 3. Remove duplicate rows
df = df.drop_duplicates().copy()

# 4. Preserve cabin availability before dropping Cabin
df["CabinKnown"] = df["Cabin"].notna().astype("int64")

# 5. Handle missing values
# Fill Age with the median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill Embarked with the most frequent value
df["Embarked"] = df["Embarked"].fillna(
    df["Embarked"].mode()[0]
)

# Cabin has too many missing values, so retain its availability
# as CabinKnown and remove the original Cabin column
df = df.drop(columns=["Cabin"])

# 6. Standardize text columns
for column in ["Sex", "Embarked"]:
    df[column] = df[column].str.strip()

df["Sex"] = df["Sex"].str.lower()
df["Embarked"] = df["Embarked"].str.upper()

# 7. Correct data types
df["PassengerId"] = df["PassengerId"].astype("string")
df["Sex"] = df["Sex"].astype("string")
df["Embarked"] = df["Embarked"].astype("string")

for column in ["Survived", "Pclass", "SibSp", "Parch", "CabinKnown"]:
    df[column] = df[column].astype("int64")

df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Fare"] = pd.to_numeric(df["Fare"], errors="coerce")

# Handle any invalid numeric values if present
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Fare"] = df["Fare"].fillna(df["Fare"].median())

# 8. Check data types against the intended schema
after_expected_types = {
    "PassengerId": "string",
    "Survived": "int64",
    "Pclass": "int64",
    "Name": "str",
    "Sex": "string",
    "Age": "float64",
    "SibSp": "int64",
    "Parch": "int64",
    "Ticket": "str",
    "Fare": "float64",
    "Embarked": "string",
    "CabinKnown": "int64"
}

def dtype_accuracy(data, expected_types):
    matched = 0

    for column, expected_type in expected_types.items():
        if column not in data.columns:
            continue

        actual_type = str(data[column].dtype)

        # Treat pandas string and Python string representations
        # as equivalent only when the expected type is string.
        if actual_type == expected_type:
            matched += 1

    return matched

before_dtype_count = dtype_accuracy(
    original, before_expected_types
)

after_dtype_count = dtype_accuracy(
    df, after_expected_types
)

# 9. Build before-and-after summary
before = {
    "Rows": len(original),
    "Columns": len(original.columns),
    "Missing values": int(original.isnull().sum().sum()),
    "Duplicate rows": int(original.duplicated().sum()),
    "Correct data types": f"{before_dtype_count}/{len(before_expected_types)}"
}

after = {
    "Rows": len(df),
    "Columns": len(df.columns),
    "Missing values": int(df.isnull().sum().sum()),
    "Duplicate rows": int(df.duplicated().sum()),
    "Correct data types": f"{after_dtype_count}/{len(after_expected_types)}"
}

summary = pd.DataFrame(
    [before, after],
    index=["Before cleaning", "After cleaning"]
)

# 10. Identify potential outliers using IQR
outlier_rows = []

for column in ["Age", "Fare", "SibSp", "Parch"]:
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    count = int(
        ((df[column] < lower_bound) |
         (df[column] > upper_bound)).sum()
    )

    outlier_rows.append({
        "Column": column,
        "Lower bound": lower_bound,
        "Upper bound": upper_bound,
        "Potential outliers": count,
        "Decision": "Retained; values may be legitimate"
    })

outlier_report = pd.DataFrame(outlier_rows)

# 11. Save all output files
df.to_csv(OUTPUT_DIR / "titanic_cleaned.csv", index=False)
summary.to_csv(OUTPUT_DIR / "before_after_summary.csv")
outlier_report.to_csv(OUTPUT_DIR / "outlier_report.csv", index=False)

decisions = """
OASIS INFOBYTE - DATA CLEANING DECISIONS

Dataset: Titanic passenger dataset

1. Removed exact duplicate rows.
2. Filled missing Age values with the median.
3. Filled missing Embarked values with the mode.
4. Created CabinKnown to preserve cabin availability.
5. Dropped Cabin because it contained many missing values.
6. Standardized Sex to lowercase and Embarked to uppercase.
7. Converted PassengerId to string and checked numeric data types.
8. Used the IQR method to identify potential outliers.
9. Retained potential outliers because they may be legitimate
   passenger values; they were not automatically removed.
10. Saved a before-and-after data quality summary.

Missing-value handling and outlier decisions should be reviewed
before using this dataset for any statistical analysis.
"""

with open(
    OUTPUT_DIR / "cleaning_decisions.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(decisions.strip())

# 12. Display results
print("\nBEFORE-AND-AFTER SUMMARY")
print(summary.to_string())

print("\nMISSING VALUES AFTER CLEANING")
print(df.isnull().sum().to_string())

print("\nDATA TYPES AFTER CLEANING")
print(df.dtypes.to_string())

print("\nOUTLIER REPORT")
print(outlier_report.to_string(index=False))

print("\nFiles saved successfully:")
print("- output/titanic_cleaned.csv")
print("- output/before_after_summary.csv")
print("- output/outlier_report.csv")
print("- output/cleaning_decisions.txt")
