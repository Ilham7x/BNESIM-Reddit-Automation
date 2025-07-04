import praw
from datetime import datetime, timedelta

# Replace the values below with your app credentials
reddit = praw.Reddit(
    client_id='I8ieylAr3UeRYE5hiXKOTA',
    client_secret='Djnd8NJ1i6zuKVh5SYJLuWJEHbxVhQ',
    user_agent='BNESIM_Assessment by u/Ok_Training9618'
)

# Define keywords to look for
keywords = ["travel esim", "international roaming", "bnasim", "travel connectivity", 
            "roaming charges", "sim for travel", "eSIM recommendation"]

# Search in r/travel and related subreddits
subreddits = ["travel", "solotravel", "digitalnomad", "backpacking", "technology"]

for subreddit in subreddits:
    print(f"\nSubreddit: {subreddit}")
    for post in reddit.subreddit(subreddit).search(" OR ".join(keywords), sort="new", time_filter="week", limit=5):
        print("Title:", post.title)
        print("URL:", post.url)
        print("Score:", post.score)
        print("Comments:", post.num_comments)
        print("Created:", post.created_utc)
        print("Subreddit:", post.subreddit.display_name)
        print("-" * 40)
