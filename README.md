# Task_04_Descriptive_Stats

This project provides descriptive statistical summaries of three datasets related to the 2024 U.S. presidential election and social media activity. It includes implementations using:

- Pure Python (no third-party libraries)
- Pandas
- Polars

##  Datasets Used (Not Included in Repo)

To replicate this analysis, download the datasets and place them in a local folder named `data/`:
- `facebook_ads.csv`
- `facebook_posts.csv`
- `twitter_posts.csv`

Dataset source (as per assignment):
> https://drive.google.com/file/d/1Jq0fPb-tq76Ee_RtM58fT0_M3o-JDBwe/view?usp=sharing

---

##  What Each Script Does

### `pure_python_stats.py`
- Loads CSV using built-in libraries only
- Computes:
  - Count, mean, min, max, std (numeric)
  - Unique values, most frequent values (categorical)
- Performs grouped analysis by:
  - `page_id`
  - (`page_id`, `ad_id`) — where applicable

### `pandas_stats.py`
- Uses Pandas to:
  - Load and summarize datasets using `describe()`, `value_counts()`, `nunique()`
  - Performs grouped stats by `page_id` and (`page_id`, `ad_id`) where columns exist

### `polars_stats.py`
- Uses Polars for fast descriptive stats:
  - `describe()`
  - Unique values count
  - Top 5 most frequent values for categorical columns
- Grouped stats by `page_id` and (`page_id`, `ad_id`) implemented using `group_by().agg()`

---

## Summary of Insights

- Descriptive statistics revealed expected trends in ad/post volumes, spending, and message frequency.
- Grouped summaries exposed differences in average spend and message frequency across pages.
- Categorical summaries helped identify dominant advertiser names and platforms.

---

##  How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/Task_04_Descriptive_Stats.git
   cd Task_04_Descriptive_Stats
2. Place datasets inside a local data/ folder.
3. Run each script:
    python pure_python_stats.py
    python pandas_stats.py
    python polars_stats.py

## Summary of Findings
Facebook Ads showed higher variance in estimated spend and impressions across page_id groups.

Facebook Posts had a smaller number of unique post messages but high concentration around a few pages.

Twitter Posts data had fewer numeric metrics but more varied messaging and topics.

Pandas was fastest to use, Polars was fastest in performance, and Pure Python was the most manual but transparent.

## Reflections

### Was it a challenge to produce identical results?
Yes — especially between Pure Python and Polars, due to differences in:
- Data types
- Default behaviors (e.g., `describe()` in Pandas vs Polars)
- Grouping syntax

**Solution:** I standardized inputs, limited printed output, and used consistent column filters across scripts.

### Which tool was easier or more performant?
- **Easiest:** Pandas — intuitive and feature-rich
- **Most performant:** Polars — significantly faster on large datasets
- **Most manual:** Pure Python — verbose, but teaches fundamentals

For a junior data analyst, I’d recommend **starting with Pandas**, then exploring Polars once comfortable.

### Can AI tools like ChatGPT help?
Absolutely. ChatGPT provided:
- Template code to get started in each tool
- Help debugging tricky syntax (especially in Polars)
- Reliable defaults — like using `df.describe()` in Pandas — which I agree are the right recommendations for most users

Using AI responsibly helped save time while still ensuring I understood the logic behind the code.

---

### What default approach do AI tools recommend for descriptive statistics? Do you agree?

Most AI tools like ChatGPT recommend using **Pandas** and the `df.describe()` method as the default approach for descriptive statistics:

```python
df.describe()
```

#### Why it's recommended:
- It's **simple and intuitive** — perfect for beginners
- Provides key metrics (count, mean, std, min, quartiles, max) in one line
- Widely supported and used in industry, education, and interviews
- Easily extendable with `.value_counts()`, `.nunique()`, and `.groupby()`

#### Do I agree?
Yes — I agree that this is the best starting point for most analysts:
- It gives a quick overview of numeric distributions
- It's flexible enough to be adapted with `include='all'` for non-numeric data
- It's ideal for **exploratory analysis**

However, it does have limits:
- Doesn’t handle **categorical columns** well by default
- Doesn’t provide **mode** or **top categories**
- Can be slow with **large datasets**

####  Final thought:
> `df.describe()` is an excellent default, but should be paired with other tools like `value_counts()`, `groupby()`, or Polars for deeper, faster, and more specific analysis.
