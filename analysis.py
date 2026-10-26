
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from collections import Counter

# 1. SET UP PROJECT PATHS
project_folder = Path(__file__).resolve().parent
file_path = project_folder / "data" / "netflix_titles.csv"
output_folder = project_folder / "output"
charts_folder = project_folder / "charts"

output_folder.mkdir(exist_ok=True)
charts_folder.mkdir(exist_ok=True)

# 2. LOAD DATASET
df = pd.read_csv(file_path)
print("Dataset loaded:", df.shape)

# 3. CLEAN DATA
text_columns = df.select_dtypes(include=["object", "str"]).columns

for column in text_columns:
    df[column] = df[column].apply(
        lambda value: value.strip() if isinstance(value, str) else value
    )

for column in ["director", "cast", "country", "rating", "duration"]:
    df[column] = df[column].fillna("Unknown")

df["date_added"] = pd.to_datetime(
    df["date_added"], errors="coerce", format="mixed"
)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# 4. SAVE CLEANED DATA
df.to_csv(output_folder / "cleaned_netflix_titles.csv", index=False)

# 5. CHART: MOVIES VS TV SHOWS
df["type"].value_counts().plot(kind="bar", figsize=(7, 5))
plt.title("Netflix: Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(charts_folder / "content_type_distribution.png")
plt.close()

# 6. CHART: RELEASE YEAR TREND
df["release_year"].value_counts().sort_index().plot(
    kind="line", figsize=(10, 5)
)
plt.title("Netflix Titles by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig(charts_folder / "release_year_trend.png")
plt.close()

# 7. COUNT GENRES
genre_counts = Counter()

for genres in df["listed_in"].dropna():
    for genre in genres.split(","):
        genre_counts[genre.strip()] += 1

pd.Series(genre_counts).sort_values(ascending=False).head(10).sort_values().plot(
    kind="barh", figsize=(10, 6)
)
plt.title("Top 10 Netflix Content Genres")
plt.xlabel("Number of Titles")
plt.tight_layout()
plt.savefig(charts_folder / "top_10_genres.png")
plt.close()

# 8. KEY FINDINGS
print("\n========== KEY FINDINGS ==========")

print("\n1. CONTENT TYPE DISTRIBUTION")
type_counts = df["type"].value_counts()
print(type_counts)
print("\nPercentages:")
print((df["type"].value_counts(normalize=True) * 100).round(2))

print("\n2. TOP 10 GENRES")
print(pd.Series(genre_counts).sort_values(ascending=False).head(10))

country_counts = Counter()
for countries in df["country"].dropna():
    if countries != "Unknown":
        for country in countries.split(","):
            country_counts[country.strip()] += 1

print("\n3. TOP 10 COUNTRIES")
print(pd.Series(country_counts).sort_values(ascending=False).head(10))

print("\n4. TOP 5 RELEASE YEARS")
print(df["release_year"].value_counts().head(5).sort_index())

print("\n5. DATA QUALITY")
print("Total titles:", len(df))
print("Duplicate rows:", df.duplicated().sum())
print("Missing date_added values:", df["date_added"].isna().sum())

print("\n========== FINDINGS COMPLETE ==========")
print("Charts folder:", charts_folder)
print("Cleaned dataset:", output_folder / "cleaned_netflix_titles.csv")
