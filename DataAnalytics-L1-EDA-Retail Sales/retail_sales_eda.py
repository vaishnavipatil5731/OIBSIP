
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the retail sales dataset
df = pd.read_csv("retail_sales_dataset.csv")

# Display basic information
print("FIRST FIVE ROWS")
print(df.head())

print("\nDATASET SHAPE")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns.tolist())

print("\nDATA TYPES AND NON-NULL VALUES")
df.info()

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

print("\nNUMERICAL SUMMARY")
print(df.describe())

# Sales by product category
category_sales = df.groupby("Product Category")["Total Amount"].sum()
print("\nTOTAL SALES BY PRODUCT CATEGORY")
print(category_sales)

# Bar chart
plt.figure(figsize=(9, 5))
category_sales.sort_values(ascending=False).plot(
    kind="bar", color="steelblue"
)
plt.title("Total Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.show()

# 2. Sales by Gender
gender_sales = df.groupby("Gender")["Total Amount"].sum()

plt.figure(figsize=(7, 5))
gender_sales.plot(kind="bar", color="coral")
plt.title("Total Sales by Gender")
plt.xlabel("Gender")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("sales_by_gender.png")
plt.show()

# 3. Sales by Age
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Age", bins=15, kde=True)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("customer_age_distribution.png")
plt.show()

# 4. Quantity Sold by Product Category
category_quantity = df.groupby("Product Category")["Quantity"].sum()

plt.figure(figsize=(9, 5))
category_quantity.sort_values(ascending=False).plot(
    kind="bar", color="seagreen"
)
plt.title("Quantity Sold by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Quantity Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("quantity_by_category.png")
plt.show()

print("\nEDA ANALYSIS COMPLETED SUCCESSFULLY!")

# 2. Sales by Gender
gender_sales = df.groupby("Gender")["Total Amount"].sum()

plt.figure(figsize=(7, 5))
gender_sales.plot(kind="bar", color="coral")
plt.title("Total Sales by Gender")
plt.xlabel("Gender")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("sales_by_gender.png")
plt.show()

# 3. Sales by Age
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Age", bins=15, kde=True)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("customer_age_distribution.png")
plt.show()

# 4. Quantity Sold by Product Category
category_quantity = df.groupby("Product Category")["Quantity"].sum()

plt.figure(figsize=(9, 5))
category_quantity.sort_values(ascending=False).plot(
    kind="bar", color="seagreen"
)
plt.title("Quantity Sold by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Quantity Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("quantity_by_category.png")
plt.show()

print("\nEDA ANALYSIS COMPLETED SUCCESSFULLY!")
