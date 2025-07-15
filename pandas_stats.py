import pandas as pd

# Change the path of the file for analysis of different dataset
filename = "data/fb_ads.csv"
df = pd.read_csv(filename)

# 1. Full dataset summary
print("\n=== DataFrame.describe() ===")
print(df.describe(include='all'))

# 2. Most frequent values for categorical columns
print("\n=== Top 5 Frequent Values for Categorical Columns ===")
for col in df.select_dtypes(include='object').columns:
    print(f"\nColumn: {col}")
    print(df[col].value_counts(dropna=False).head(5))

# 3. Number of unique values per column
print("\n=== Number of Unique Values per Column ===")
print(df.nunique(dropna=False))

# 4. Grouped by page_id
print("\n=== Grouped Descriptive Stats by page_id ===")
try:
    grouped_page = df.groupby("page_id").describe()
    print(grouped_page.head(10))  # Displaying only first 10 groups for readability
except KeyError:
    print("Column 'page_id' not found.")

# 5. Grouped by (page_id, ad_id)
print("\n=== Grouped Descriptive Stats by (page_id, ad_id) ===")
if "ad_id" in df.columns:
    grouped_page_ad = df.groupby(["page_id", "ad_id"]).describe()
    print(grouped_page_ad.head(10))  # Displaying only first 10 groups
else:
    print("Column 'ad_id' not found.")
