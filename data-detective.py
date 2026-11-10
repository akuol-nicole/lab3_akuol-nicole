import csv
import sys
import os

def load_raw_data(filename):
    """
    Loads the CSV file into a list of dictionaries safely.
    Handles missing file edge cases.
    """
    if not os.path.exists(filename):
        print(f"Error: The dataset file '{filename}' was not found.")
        print("Please ensure the CSV file is placed in the project directory.")
        sys.exit(1)
        
    raw_tweets = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                raw_tweets.append(row)
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        sys.exit(1)
            
    return raw_tweets

def clean_data(tweets):
    """
    QUEST 1: The Data Auditor (Handle Missing Fields)
    - If 'Text' is missing/empty, removes/discards row.
    - If 'Likes' or 'Retweets' is missing or non-numeric, replaces with 0.
    - Validates data types by explicitly casting to int.
    - Prints total bad rows fixed or removed.
    """
    cleaned_tweets = []
    fixed_or_removed_count = 0

    for tweet in tweets:
        row_was_modified = False

        # Validate Text
        text_val = tweet.get('Text')
        if text_val is None or str(text_val).strip() == "":
            fixed_or_removed_count += 1
            continue  # Discard row missing text

        # Validate & Cast Likes
        likes_val = tweet.get('Likes')
        if likes_val is None or str(likes_val).strip() == "":
            tweet['Likes'] = 0
            row_was_modified = True
        else:
            try:
                tweet['Likes'] = int(float(str(likes_val).strip()))
                if tweet['Likes'] < 0:
                    tweet['Likes'] = 0
                    row_was_modified = True
            except (ValueError, TypeError):
                tweet['Likes'] = 0
                row_was_modified = True

        # Validate & Cast Retweets
        retweets_val = tweet.get('Retweets')
        if retweets_val is None or str(retweets_val).strip() == "":
            tweet['Retweets'] = 0
            row_was_modified = True
        else:
            try:
                tweet['Retweets'] = int(float(str(retweets_val).strip()))
                if tweet['Retweets'] < 0:
                    tweet['Retweets'] = 0
                    row_was_modified = True
            except (ValueError, TypeError):
                tweet['Retweets'] = 0
                row_was_modified = True

        # Ensure Username is clean
        username_val = tweet.get('Username')
        if username_val is None or str(username_val).strip() == "":
            tweet['Username'] = "Anonymous"
        else:
            tweet['Username'] = str(username_val).strip()

        if row_was_modified:
            fixed_or_removed_count += 1

        cleaned_tweets.append(tweet)

    print("========================================")
    print("      QUEST 1: THE DATA AUDITOR         ")
    print("========================================")
    print(f"Total 'bad' rows fixed or removed: {fixed_or_removed_count}")
    print(f"Total clean tweets ready for analysis: {len(cleaned_tweets)}\n")
    return cleaned_tweets

def find_viral_tweet(tweets):
    """
    QUEST 2: The Viral Post (Find the Maximum)
    Loops manually without using built-in max().
    """
    print("========================================")
    print("       QUEST 2: THE VIRAL POST          ")
    print("========================================")
    if not tweets:
        print("Error: No tweets available to analyze.")
        return None

    top_tweet = tweets[0]
    for tweet in tweets[1:]:
        if tweet['Likes'] > top_tweet['Likes']:
            top_tweet = tweet

    print(f"Username : @{top_tweet.get('Username')}")
    print(f"Likes    : {top_tweet['Likes']}")
    print(f"Text     : {top_tweet.get('Text')}\n")
    return top_tweet

def custom_sort_by_likes(tweets):
    """
    QUEST 3: The Algorithm Builder (Custom Sort)
    Uses Selection Sort to order tweets descending by Likes.
    Strictly prohibited from using .sort() or sorted().
    Slices the list to return and print only the top 10.
    """
    print("========================================")
    print("  QUEST 3: TOP 10 MOST LIKED TWEETS     ")
    print("========================================")
    if not tweets:
        print("Error: No tweets available to sort.")
        return []

    sorted_list = list(tweets)
    n = len(sorted_list)

    # Selection Sort (Descending)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if sorted_list[j]['Likes'] > sorted_list[max_idx]['Likes']:
                max_idx = j
        sorted_list[i], sorted_list[max_idx] = sorted_list[max_idx], sorted_list[i]

    top_10 = sorted_list[:10]

    for rank, tweet in enumerate(top_10, 1):
        print(f"{rank}. [{tweet['Likes']} Likes] @{tweet.get('Username')}: {tweet.get('Text')}")
    print()
    return top_10

def search_tweets(tweets, keyword):
    """
    QUEST 4: The Content Filter (Search & Extract)
    Extracts tweets matching the keyword into a new list.
    Reports len() of the extracted matches.
    """
    print("========================================")
    print("     QUEST 4: THE CONTENT FILTER        ")
    print("========================================")
    if not keyword or keyword.strip() == "":
        print("Error: Search keyword cannot be empty.\n")
        return []

    clean_keyword = keyword.strip().lower()
    matches = []

    for tweet in tweets:
        if clean_keyword in tweet.get('Text', '').lower():
            matches.append(tweet)

    print(f"Search term: '{keyword.strip()}'")
    print(f"Matching tweets found: {len(matches)}\n")

    if len(matches) == 0:
        print("No tweets matched your keyword query.\n")
    else:
        for idx, tweet in enumerate(matches, 1):
            print(f"{idx}. @{tweet.get('Username')}: {tweet.get('Text')}")
        print()

    return matches

if __name__ == "__main__":
    csv_filename = "twitter_dataset.csv"
    
    # Load dataset
    dataset = load_raw_data(csv_filename)
    print(f"Loaded {len(dataset)} raw tweets from '{csv_filename}'.\n")

    # Run Quests
    clean_dataset = clean_data(dataset)
    find_viral_tweet(clean_dataset)
    custom_sort_by_likes(clean_dataset)

    # Quest 4 interactive input
    try:
        user_keyword = input("Enter a keyword to filter tweets: ")
        search_tweets(clean_dataset, user_keyword)
    except (KeyboardInterrupt, EOFError):
        print("\nSearch cancelled by user.")