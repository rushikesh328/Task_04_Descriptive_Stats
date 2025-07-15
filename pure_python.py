import csv
from collections import defaultdict, Counter
import math

def read_csv(filepath):
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        return list(csv.DictReader(csvfile))

#change the path of file for a different dataset analysis
if __name__ == "__main__":
    data = read_csv("data/fb_ads.csv") 

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def summarize_numeric(data):
    column_stats = defaultdict(list)

    for row in data:
        for key, value in row.items():
            if is_float(value):
                column_stats[key].append(float(value))

    for col, values in column_stats.items():
        if not values:
            continue
        count = len(values)
        mean = sum(values) / count
        min_val = min(values)
        max_val = max(values)
        std = math.sqrt(sum((x - mean) ** 2 for x in values) / count)

        print(f"\nColumn: {col}")
        print(f"  Count: {count}")
        print(f"  Mean: {mean:.2f}")
        print(f"  Min: {min_val}")
        print(f"  Max: {max_val}")
        print(f"  Std Dev: {std:.2f}")

summarize_numeric(data)
from collections import Counter

def summarize_categorical(data):
    column_values = defaultdict(list)

    for row in data:
        for key, value in row.items():
            if not is_float(value) and value != "":
                column_values[key].append(value)

    for col, values in column_values.items():
        counter = Counter(values)
        unique_count = len(counter)
        most_common_value, freq = counter.most_common(1)[0]

        print(f"\nColumn: {col}")
        print(f"  Unique values: {unique_count}")
        print(f"  Most frequent: {most_common_value} ({freq} times)")

summarize_categorical(data)

def grouped_summary_by_page_id_all_columns(data):
    from collections import defaultdict, Counter

    numeric_cols = set()
    non_numeric_cols = set()

    for row in data:
        for key, value in row.items():
            if is_float(value):
                numeric_cols.add(key)
            elif value != "":
                non_numeric_cols.add(key)

    numeric_cols = list(numeric_cols)
    non_numeric_cols = list(non_numeric_cols)

    grouped_data = defaultdict(lambda: {'numeric': defaultdict(list), 'categorical': defaultdict(list)})

    for row in data:
        page_id = row.get("page_id")
        if not page_id:
            continue

        for col in numeric_cols:
            val = row.get(col)
            if is_float(val):
                grouped_data[page_id]['numeric'][col].append(float(val))

        for col in non_numeric_cols:
            val = row.get(col)
            if val:
                grouped_data[page_id]['categorical'][col].append(val)

    for page_id, content in grouped_data.items():
        print(f"\n=== Stats for page_id: {page_id} ===")

        # Numeric columns
        for col, values in content['numeric'].items():
            if not values:
                continue
            count = len(values)
            mean = sum(values) / count
            min_val = min(values)
            max_val = max(values)
            std = math.sqrt(sum((x - mean) ** 2 for x in values) / count)

            print(f"\n[Numeric] Column: {col}")
            print(f"  Count: {count}")
            print(f"  Mean: {mean:.2f}")
            print(f"  Min: {min_val}")
            print(f"  Max: {max_val}")
            print(f"  Std Dev: {std:.2f}")

        # Categorical columns
        for col, values in content['categorical'].items():
            counter = Counter(values)
            unique_count = len(counter)
            most_common_value, freq = counter.most_common(1)[0]

            print(f"\n[Categorical] Column: {col}")
            print(f"  Unique values: {unique_count}")
            print(f"  Most frequent: {most_common_value} ({freq} times)")

grouped_summary_by_page_id_all_columns(data)

def grouped_summary_by_page_and_ad_id(data, max_rows=5000, max_groups=10):
    from collections import defaultdict, Counter

    data = data[:max_rows]  # Limit rows for testing

    numeric_cols = set()
    non_numeric_cols = set()

    for row in data:
        for key, value in row.items():
            if is_float(value):
                numeric_cols.add(key)
            elif value != "":
                non_numeric_cols.add(key)

    grouped_data = defaultdict(lambda: {'numeric': defaultdict(list), 'categorical': defaultdict(list)})

    for row in data:
        page_id = row.get("page_id")
        ad_id = row.get("ad_id")
        if not page_id or not ad_id:
            continue
        key = (page_id, ad_id)

        for col in numeric_cols:
            val = row.get(col)
            if is_float(val):
                grouped_data[key]['numeric'][col].append(float(val))

        for col in non_numeric_cols:
            val = row.get(col)
            if val:
                grouped_data[key]['categorical'][col].append(val)

    for i, ((page_id, ad_id), content) in enumerate(grouped_data.items()):
        if i >= max_groups:
            break
        print(f"\n=== Stats for (page_id, ad_id): ({page_id}, {ad_id}) ===")

        for col, values in content['numeric'].items():
            if not values:
                continue
            count = len(values)
            mean = sum(values) / count
            min_val = min(values)
            max_val = max(values)
            std = math.sqrt(sum((x - mean) ** 2 for x in values) / count)

            print(f"\n[Numeric] Column: {col}")
            print(f"  Count: {count}")
            print(f"  Mean: {mean:.2f}")
            print(f"  Min: {min_val}")
            print(f"  Max: {max_val}")
            print(f"  Std Dev: {std:.2f}")

        for col, values in content['categorical'].items():
            counter = Counter(values)
            unique_count = len(counter)
            most_common_value, freq = counter.most_common(1)[0]

            print(f"\n[Categorical] Column: {col}")
            print(f"  Unique values: {unique_count}")
            print(f"  Most frequent: {most_common_value} ({freq} times)")

grouped_summary_by_page_and_ad_id(data)

