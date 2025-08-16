import os
import pandas as pd

RAW_FILE = "data/raw/youtube_trending.csv"
PROCESSED_PATH = "data/processed/"
os.makedirs(PROCESSED_PATH, exist_ok=True)

# Load raw data
df = pd.read_csv(RAW_FILE)

# Transform: add engagement rate column
df["engagement_rate"] = (df["likes"] / df["views"]) * 100

# Sort by views
df_sorted = df.sort_values(by="views", ascending=False)

df_sorted.to_csv(os.path.join(PROCESSED_PATH, "youtube_trending_clean.csv"), index=False)

print("✅ Data transformed and saved to", PROCESSED_PATH)
