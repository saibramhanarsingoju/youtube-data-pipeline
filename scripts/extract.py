import os
import pandas as pd

RAW_DATA_PATH = "data/raw/"
os.makedirs(RAW_DATA_PATH, exist_ok=True)

# Simulate extract: load a sample YouTube dataset (replace with Kaggle download)
data = {
    "video_id": ["a1", "b2", "c3"],
    "title": ["Video A", "Video B", "Video C"],
    "views": [1000, 5000, 3000],
    "likes": [100, 400, 250],
    "category": ["Music", "Education", "Music"]
}

df = pd.DataFrame(data)
df.to_csv(os.path.join(RAW_DATA_PATH, "youtube_trending.csv"), index=False)

print("✅ Data extracted to", RAW_DATA_PATH)
