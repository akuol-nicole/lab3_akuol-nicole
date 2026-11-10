import csv
import sys
import os

def load_raw_data(filename):
    if not os.path.exists(filename):
        print(f"File {filename} not found.")
        sys.exit(1)
        
    raw_tweets = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            raw_tweets.append(row)
            
    return raw_tweets

def clean_data(tweets):
    # Quest 1: Remove tweets missing text, fill blank likes/retweets with 0
    clean_list = []
    bad_rows = 0

    for tweet in tweets:
        text = tweet.get('Text', '')
        # Skip if text is empty or missing
        if not text or text.strip() == "":
            bad_rows += 1
            continue

        fixed = False

        # Check likes
        likes = tweet.get('Likes', '')
        if not likes or likes.strip() == "":
            tweet['Likes'] = 0
            fixed = True
        else:
            tweet['Likes'] = int(float(likes))

        # Check retweets
        retweets = tweet.get('Retweets', '')
        if not retweets or retweets.strip() == "":
            tweet['Retweets'] = 0
            fixed = True
        else:
            tweet['Retweets'] = int(float(retweets))

        if fixed:
            bad_rows += 1

        clean_list.append(tweet)

    print("--- Quest 1: Clean Data ---")
    print(f"Bad rows removed or fixed: {bad_rows}")
    print(f"Remaining valid tweets: {len(clean_list)}\n")
    return clean_list

def find_viral_tweet(tweets):
    # Quest 2: Find max likes without using max()
    top_tweet = tweets[0]
    for tweet in tweets:
        if tweet['Likes'] > top_tweet['Likes']:
            top_tweet = tweet

    print("--- Quest 2: Most Liked Tweet ---")
    print(f"User: @{top_tweet.get('Username')}")
    print(f"Likes: {top_tweet.get('Likes')}")
    print(f"Tweet: {top_tweet.get('Text')}\n")
    return top_tweet

def custom_sort_by_likes(tweets):
    # Quest 3: Bubble sort descending without .sort()
    sorted_tweets = list(tweets)
    n = len(sorted_tweets)

    # Bubble sort
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_tweets[j]['Likes'] < sorted_tweets[j + 1]['Likes']:
                # Swap positions
                temp = sorted_tweets[j]
                sorted_tweets[j] = sorted_tweets[j + 1]
                sorted_tweets[j + 1] = temp

    top_10 = sorted_tweets[:10]

    print("--- Quest 3: Top 10 Tweets ---")
    rank = 1
    for tweet in top_10:
        print(f"{rank}. [{tweet['Likes']} likes] @{tweet.get('Username')}: {tweet.get('Text')}")
        rank += 1
    print()
    return top_10

def search_tweets(tweets, keyword):
    # Quest 4: Search keyword and add matches to a new list
    matching_tweets = []
    search_term = keyword.lower()

    for tweet in tweets:
        if search_term in tweet.get('Text', '').lower():
            matching_tweets.append(tweet)

    print(f"--- Quest 4: Keyword Search for '{keyword}' ---")
    print(f"Found {len(matching_tweets)} matching tweets.\n")
    for t in matching_tweets:
        print(f"@{t.get('Username')}: {t.get('Text')}")
    print()
    return matching_tweets

if __name__ == "__main__":
    tweets = load_raw_data("twitter_dataset.csv")
    print(f"Loaded {len(tweets)} tweets.\n")

    cleaned = clean_data(tweets)
    find_viral_tweet(cleaned)
    custom_sort_by_likes(cleaned)

    word = input("Enter a word to search for: ")
    search_tweets(cleaned, word)