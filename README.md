# YouTube Trending Data Pipeline

## Overview
This project demonstrates an ETL (Extract-Transform-Load) pipeline using Python for YouTube trending videos data. 
It simulates AWS architecture by processing data locally, but can be extended to AWS services (S3, Glue, Athena, QuickSight).

## Features
- Extract YouTube trending dataset from Kaggle
- Transform: clean data, calculate metrics
- Load: save processed data for analytics

## Tech Stack
- Python (pandas, boto3)
- AWS S3 (for future extension)
- Jupyter Notebook (optional for exploration)

## How to Run
1. Clone the repo:
   ```
   git clone <your-repo-url>
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run ETL scripts:
   ```
   python scripts/extract.py
   python scripts/transform.py
   python scripts/load.py
   ```
