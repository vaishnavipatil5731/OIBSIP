# Oasis Infobyte Internship — Task 3: Data Cleaning

## Project Overview
This project focuses on cleaning the Titanic passenger dataset using Python and Pandas. The objective is to identify and handle missing values, remove duplicate records, standardize text data, correct data types, and document potential outliers.

## Tools and Technologies
- Python
- Pandas
- NumPy
- VS Code

## Dataset
The project uses the Titanic passenger dataset containing 891 rows and 12 original columns.

## Data Cleaning Steps
1. Inspected the dataset and checked data quality.
2. Checked and removed duplicate rows.
3. Filled missing Age values using the median.
4. Filled missing Embarked values using the mode.
5. Created a `CabinKnown` indicator and removed the original Cabin column due to extensive missing data.
6. Standardized Sex and Embarked text values.
7. Converted columns to their intended data types.
8. Identified potential outliers using the Interquartile Range (IQR) method.
9. Retained potential outliers because they may represent legitimate passenger records.
10. Generated a before-and-after quality summary.

## Results

| Metric | Before Cleaning | After Cleaning |
|---|---:|---:|
| Rows | 891 | 891 |
| Columns | 12 | 12 |
| Missing values | 866 | 0 |
| Duplicate rows | 0 | 0 |
| Correct data types | 9/12 | 12/12 |

## Output Files
- `output/titanic_cleaned.csv` — cleaned dataset
- `output/before_after_summary.csv` — quality comparison
- `output/outlier_report.csv` — potential outlier report
- `output/cleaning_decisions.txt` — documentation of cleaning decisions

## How to Run
1. Install Python.
2. Install the required library:

   `pip install pandas`

3. Ensure the original dataset is located at `data/titanic.csv`.
4. Run:

   `python clean_titanic.py`

## Conclusion
The dataset was cleaned by handling missing values, checking duplicates, standardizing text, correcting data types, and documenting potential outliers. The cleaned dataset and quality reports were saved in the output folder.

**Internship Track:** Data Analytics  
**Organization:** Oasis Infobyte
