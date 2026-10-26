# OTT Content Strategy & Trend Analysis Using Python

## Project Overview
This project analyzes a Netflix movies and TV shows catalogue dataset using Python. It explores content-type distribution, genre representation, country associations, release-year patterns, and data quality.

## Objectives
- Clean and prepare catalogue data using Pandas.
- Analyze movies versus TV shows.
- Identify frequently listed genres and countries.
- Explore release-year patterns.
- Visualize findings and develop evidence-based recommendations.

## Tools and Technologies
- Python
- Pandas
- Matplotlib
- Collections (`Counter`)
- CSV data processing

## Dataset
The dataset contains 8,807 titles and 12 columns, including title, content type, director, cast, country, date added, release year, rating, duration, genre labels, and description.

## Key Findings
- Total titles analyzed: 8,807.
- Movies: 6,131 (69.62%).
- TV shows: 2,676 (30.38%).
- Most frequent genre label: International Movies (2,752 titles).
- United States had the highest country association count (3,690), followed by India (1,046).
- 2018 was the most represented release year among the years in the dataset (1,147 titles).
- No duplicate rows were found.
- Ten `date_added` values remained missing.

## Visualizations
Charts are saved in the `charts/` directory:
- `content_type_distribution.png`
- `release_year_trend.png`
- `top_10_genres.png`

## Project Structure
```text
OTT-Content-Strategy-and-Trend-Analysis/
├── analysis.py
├── data/
│   └── netflix_titles.csv
├── output/
│   └── cleaned_netflix_titles.csv
├── charts/
│   ├── content_type_distribution.png
│   ├── release_year_trend.png
│   └── top_10_genres.png
└── README.md
```

## Business Insights
The catalogue contains more movies than TV shows. International content and drama-related labels are prominent. These findings can guide further catalogue research, but do not measure audience popularity or profitability.

## Limitations
This analysis uses catalogue metadata. It does not include actual viewership, revenue, customer preferences, or subscriber engagement. Country and genre counts can overlap because a title may have multiple associated countries or genre labels.

## How to Run
1. Install dependencies:
   `python -m pip install pandas matplotlib`
2. Place `netflix_titles.csv` in the `data/` directory.
3. Run:
   `python analysis.py`

## Learning Outcomes
Data cleaning, missing-value handling, date conversion, exploratory data analysis, data visualization, and communicating findings.

## Disclaimer
This is an educational portfolio project using a public dataset. It is not affiliated with or endorsed by Netflix.
