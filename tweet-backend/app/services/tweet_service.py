import os, re, requests
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Groq client with API key
groq_client = Groq(api_key=os.environ["GROQ_API_KEY"])

def serper_search(query, num_results=20):
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": os.environ["SERPER_API_KEY"],
        "Content-Type": "application/json"
    }
    payload = {"q": query, "num": num_results}
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json().get("organic", [])

def filter_sources(results, max_sources=10):
    seen_domains, clean_results = set(), []
    for item in results:
        link, snippet, title = item.get("link", ""), item.get("snippet", ""), item.get("title", "")
        domain = link.split("/")[2] if "://" in link else None
        if not domain or domain in seen_domains:
            continue
        seen_domains.add(domain)
        if title and snippet:
            clean_results.append({"domain": domain, "content": f"{title}: {snippet}"})
        if len(clean_results) >= max_sources:
            break
    return clean_results

def build_context(articles):
    return "\n".join([f"SOURCE {i} ({a['domain']}): {a['content']}" for i, a in enumerate(articles, 1)])

def groq_generate(prompt_text):
    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You write natural, human-sounding tweets reacting to real news."},
            {"role": "user", "content": prompt_text}
        ],
        max_tokens=500, temperature=0.6, top_p=0.9
    )
    return response.choices[0].message.content.strip()

def clean_tweets(text):
    tweets, seen = [], set()
    for line in text.split("\n"):
        line = re.sub(r"^\d+[\.\)]\s*", "", line).strip('"').strip("'").strip()
        if not line or len(line) < 40 or len(line) > 280 or line in seen:
            continue
        seen.add(line)
        tweets.append(line)
    return tweets[:10]
