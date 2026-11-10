#!/bin/bash

CSV_FILE="${1:-twitter_dataset.csv}"

if [ ! -f "$CSV_FILE" ]; then
    echo "Error: The dataset file '$CSV_FILE' does not exist."
    echo "Usage: ./feed-analyzer.sh [filename.csv]"
    exit 1
fi

echo "========================================"
echo "       TOP 5 MOST ACTIVE USERS          "
echo "========================================"

# Extract column 2, keep valid usernames (start with letter/underscore), count and rank
tail -n +2 "$CSV_FILE" | cut -d',' -f2 | grep -E '^[a-zA-Z_]' | sort | uniq -c | sort -nr | head -n 5
