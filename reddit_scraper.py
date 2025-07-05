import praw, json, re
from datetime import datetime, timezone, timedelta

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

# Search in related subreddits
subreddits = ["travel", "solotravel", "digitalnomad", "backpacking", "technology", "europeTravel", "Shoestring", "JapanTravel", "WorkOnline", "RemoteWork", "TravelHacks"]

results = []
one_week_ago = datetime.now(timezone.utc) - timedelta(days=7)

for sub in subreddits:
    for post in reddit.subreddit(sub).new(limit=100):
        # keep only last 7 days posts
        created_dt = datetime.fromtimestamp(post.created_utc, tz=timezone.utc)
        if created_dt < one_week_ago:
            continue

        text_blob = f"{post.title} {post.selftext or ''}".lower()
        if kw_regex.search(text_blob):
            results.append(
                {
                    "title": post.title,
                    "url": post.url,
                    "score": post.score,
                    "comments": post.num_comments,
                    "created": created_dt.strftime("%Y-%m-%d %H:%M:%S"),
                    "subreddit": post.subreddit.display_name,
                    "context": "question" if "?" in post.title else "general"
                }
            )

# save to JSON
with open("reddit_posts.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"Saved {len(results)} matching posts to reddit_posts.json")