import requests, json, os

API_KEY = os.getenv("TOGETHER_API_KEY")  
API_URL = "https://api.together.xyz/v1/chat/completions"

MODEL = "meta-llama/Llama-3-8b-chat-hf"

with open("reddit_posts.json", "r", encoding="utf-8") as f:
    reddit_posts = json.load(f)

results = []

for post in reddit_posts:
    prompt = f"""
The following Reddit post is from r/{post['subreddit']}:
Title: "{post['title']}"
Context type: {post['context']}

Your task is to write a helpful, natural response that:
- Directly addresses the user’s concern
- Subtly mentions BNESIM as a solution (without sounding like a sales pitch)
- Follows Reddit community tone and style

Generate a short, friendly reply (2–4 lines):
"""
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "max_tokens": 200,
        "temperature": 0.7,
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
        post["ai_reply"] = reply.strip()
        print(f"Replied to: {post['title']}\n→ {reply}\n")
    else:
        print(f"Failed for: {post['title']}")
        post["ai_reply"] = "Error generating response."

    results.append(post)

with open("responses.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("All responses saved to responses.json")
