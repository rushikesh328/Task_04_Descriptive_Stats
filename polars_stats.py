import polars as pl

filename = "data/fb_ads.csv"  # Change to your dataset file
df = pl.read_csv(filename)

# Overall Descriptive Statistics
print("\n=== Polars: DataFrame.describe() ===")
print(df.describe())

# Unique values per column
print("\n=== Number of Unique Values per Column ===")
for col in df.columns:
    unique_count = df.select(pl.col(col).n_unique()).item()
    print(f"{col}: {unique_count}")

print("\n=== Top 5 Frequent Values for Categorical Columns ===")
for col in df.columns:
    if df[col].dtype == pl.Utf8:
        top_values = (
            df.select(pl.col(col).value_counts())
              .select([
                  pl.col(col).struct.field(col).alias("value"),
                  pl.col(col).struct.field("count").alias("count")
              ])
              .sort("count", descending=True)
              .head(5)
        )
        print(f"\nColumn: {col}")
        print(top_values)


# Grouped by page_id
if "page_id" in df.columns:
    print("\n=== Grouped Stats by page_id ===")
    try:
        grouped_page = (
            df.group_by("page_id")
              .agg([
                  *[pl.col(c).mean().alias(f"{c}_mean") for c in df.columns if c != "page_id"],
                  *[pl.col(c).std().alias(f"{c}_std") for c in df.columns if c != "page_id"],
                  *[pl.col(c).min().alias(f"{c}_min") for c in df.columns if c != "page_id"],
                  *[pl.col(c).max().alias(f"{c}_max") for c in df.columns if c != "page_id"]
              ])
        )
        print(grouped_page.head(5))
    except Exception as e:
        print(f"Grouping by page_id failed: {e}")

# Grouped by (page_id, ad_id)
if "page_id" in df.columns and "ad_id" in df.columns:
    print("\n=== Grouped Stats by (page_id, ad_id) ===")
    try:
        grouped_page_ad = (
            df.group_by(["page_id", "ad_id"])
              .agg([
                  *[pl.col(c).mean().alias(f"{c}_mean") for c in df.columns if c not in ["page_id", "ad_id"]],
                  *[pl.col(c).std().alias(f"{c}_std") for c in df.columns if c not in ["page_id", "ad_id"]],
                  *[pl.col(c).min().alias(f"{c}_min") for c in df.columns if c not in ["page_id", "ad_id"]],
                  *[pl.col(c).max().alias(f"{c}_max") for c in df.columns if c not in ["page_id", "ad_id"]]
              ])
        )
        print(grouped_page_ad.head(5))
    except Exception as e:
        print(f"Grouping by (page_id, ad_id) failed: {e}")

