import pandas as pd
df = pd.read_csv("titanic.csv")
print("First 5 Rows of the Dataset:")
print(df.head())
import pandas as pd

# Load dataset
df = pd.read_csv("titanic.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())
import pandas as pd

# Load dataset
df = pd.read_csv("titanic.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Missing values before cleaning
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Fill missing Age values with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Embarked values with mode
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Drop Cabin column because most values are missing
df = df.drop(columns=["Cabin"])

# Remove duplicate rows (there are none, but this is good practice)
df = df.drop_duplicates()

# Missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("cleaned_titanic.csv", index=False)

print("\n✅ Data Cleaning Completed Successfully!")