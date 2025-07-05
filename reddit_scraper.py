import praw, json, re, logging
from datetime import datetime, timezone, timedelta
from textblob import TextBlob

MIN_UPVOTES = 5
MIN_COMMENTS = 5

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

reddit = praw.Reddit(
    client_id='I8ieylAr3UeRYE5hiXKOTA',
    client_secret='Djnd8NJ1i6zuKVh5SYJLuWJEHbxVhQ',
    user_agent='BNESIM_Assessment by u/Ok_Training9618'
)

keywords = [
    "travel esim", "international roaming", "BNESIM", "travel connectivity", 
    "roaming charges", "sim for travel", "eSIM recommendation", "travel SIM", 
    "holafly", "data roaming", "airalo", "Nomad eSIM", "global esim", 
    "best esim", "instabridge", "esim vs sim", "sim card for travel", 
    "cheap roaming", "esim dubai", "europe esim"
]

kw_regex = re.compile("|".join(re.escape(k.lower()) for k in keywords))

# Function to count keyword matches
def keyword_hits(text: str) -> int:
    return sum(1 for kw in keywords if kw.lower() in text)

# Search in related subreddits
subreddits = ["travel", "solotravel", "digitalnomad", "backpacking", "technology", "europeTravel", "Shoestring", "JapanTravel", "WorkOnline", "RemoteWork", "TravelHacks"]

results = []
one_week_ago = datetime.now(timezone.utc) - timedelta(days=7)

for sub in subreddits:
    try:
        logging.info(f"Processing subreddit: {sub}")
        for post in reddit.subreddit(sub).new(limit=100):
            try:
                # keep only last 7 days posts
                created_dt = datetime.fromtimestamp(post.created_utc, tz=timezone.utc)
                if created_dt < one_week_ago:
                    continue

                # skip low-engagement posts
                if post.score < MIN_UPVOTES and post.num_comments < MIN_COMMENTS:
                    continue

                text_blob = f"{post.title} {post.selftext or ''}".lower()
                hits = keyword_hits(text_blob)

                if hits:
                    sentiment_score = TextBlob(text_blob).sentiment.polarity
                    if sentiment_score > 0.1:
                        sentiment = "positive"
                    elif sentiment_score < -0.1:
                        sentiment = "negative"
                    else:
                        sentiment = "neutral"

                    engagement_score = post.score + (2 * post.num_comments)

                    results.append(
                        {
                            "title": post.title,
                            "url": post.url,
                            "up-votes": post.score,
                            "comments": post.num_comments,
                            "created": created_dt.strftime("%Y-%m-%d %H:%M:%S"),
                            "subreddit": post.subreddit.display_name,
                            "context": "question" if "?" in post.title else "general",
                            "relevance_score": hits,
                            "sentiment": sentiment,
                            "engagement_score": engagement_score
                        }
                    )
            except Exception as post_err:
                logging.warning(f"Error processing a post in r/{sub}: {post_err}")
    except Exception as sub_err:
        logging.error(f"Failed to fetch posts from r/{sub}: {sub_err}")

# save to JSON
with open("reddit_posts.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"Saved {len(results)} matching posts to reddit_posts.json")