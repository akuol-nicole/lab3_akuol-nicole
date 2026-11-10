# Lab 3: The Social Media Data Detective

**Student Name:** Akuol Juach Agok  
**Repository:** `lab3_akuol-nicole`

## Project Overview
This project processes and analyzes a Twitter dataset using custom Python algorithms without relying on built-in sorting or max functions, accompanied by a Bash shell text processing pipeline.

## Repository Contents
- `data-detective.py`: Python script solving all 4 analytical quests with custom logic and robust validation.
- `feed-analyzer.sh`: Shell script pipeline calculating the top 5 most active users.
- `twitter_dataset.csv`: Dataset containing Twitter engagement metrics.
- `Readme.md`: Documentation and execution guidelines.

## Implementation Details
- **Quest 1 (Data Auditor):** Filters out tweets missing text, sets missing or invalid Likes/Retweets to 0, casts values to integers, and counts modified/removed rows.
- **Quest 2 (The Viral Post):** Determines the highest-liked tweet via a custom single-pass loop without using `max()`.
- **Quest 3 (Algorithm Builder):** Custom Selection Sort algorithm sorting tweets in descending order of Likes without `.sort()` or `sorted()`, displaying the top 10.
- **Quest 4 (Content Filter):** Interactive keyword search filtering matching posts into a new list, utilizing `append()` and outputting `len()`.
- **Bash Feed Analyzer:** Chained command pipeline (`tail | cut | sort | uniq -c | sort -nr | head -n 5`) identifying the top 5 active users.

## How to Run

### Run Python Analysis
```bash
python3 data-detective.py