# BNESIM Reddit Automation

This project automatically discovers Reddit posts mentioning **travel eSIMs**, **connectivity issues**, or **BNESIM**, and generates intelligent AI-powered response suggestions for the marketing team.

---

## 🚀 Features

### 🔍 Discovery Engine
- Searches across travel-related subreddits for relevant posts within the **last 7 days**
- Uses **keyword matching**, **regex filtering**, and **engagement thresholds**
- Extracts post metadata: title, content, URL, subreddit, creation time, upvotes, and comment count

### 📊 Content Scoring
- Assigns a **relevance score** based on keyword matches
- Filters out posts with **low engagement** (less than 5 upvotes and 5 comments)

### 🧠 AI Response Generation
- Uses **Together.ai's open-source GPT-4 model** to generate replies
- Responses are:
  - Helpful and natural
  - Aligned with Reddit tone
  - Casually mention BNESIM (without sounding like an ad)

### 🧪 Sentiment Analysis
- Labels each post as `positive`, `negative`, or `neutral` using TextBlob

---

## 📂 Files

| File | Description |
|------|-------------|
| `reddit_scraper.py` | Scrapes Reddit posts, filters, scores, and saves to `reddit_posts.json` |
| `generate_responses.py` | Loads posts and generates AI replies, saves to `responses.json` |
| `reddit_posts.json` | Extracted Reddit post data |
| `responses.json` | Generated AI responses |
| `requirements.txt` | All required Python packages |

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/Ilham7x/BNESIM-Reddit-Automation.git
cd BNESIM-Reddit-Automation

# Create virtual environment (optional)
python -m venv venv
source venv/Scripts/activate  # Windows

# Install requirements
pip install -r requirements.txt
```

---

## 🔑 API Keys

You'll need:

- A Reddit developer account for `client_id` and `client_secret`
- A Together.ai account: https://platform.together.xyz
- An API key from Together.ai

Set your Together API key before running:

```bash
set TOGETHER_API_KEY=your_together_api_key_here
```

---

## 📤 Sample Output

### Sample from `reddit_posts.json`:

```json
{
  "title": "Local SMS not arriving while using travel eSIM",
  "url": "https://www.reddit.com/r/TravelHacks/comments/1lrpvnp/local_sms_not_arriving_while_using_travel_esim/",
  "up-votes": 0,
  "comments": 8,
  "created": "2025-07-04 18:29:25",
  "subreddit": "TravelHacks",
  "context": "general",
  "relevance_score": 1,
  "sentiment": "negative"
}
```

### Sample from `responses.json`:

```json
{
  "title": "Local SMS not arriving while using travel eSIM",
  "response": "Hey there! Sorry to hear that your local SMS isn't arriving while using your travel eSIM. That can be super frustrating! Have you tried reaching out to your carrier's customer support to troubleshoot? Some providers like BNESIM have great support for SMS delivery issues."
}
```

---

## ✍️ Author

**Ilham Ghori** — 2025 BNESIM Assessment Submission

---

## ✅ Status

✔️ Core and Advanced Features Implemented  
✔️ Clean output, modular code, and zero dependency on premium services  
✔️ Designed with extensibility and marketing impact in mind

