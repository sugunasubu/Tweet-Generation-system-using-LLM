from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, Field

from app.services.tweet_service import (
    serper_search,
    filter_sources,
    build_context,
    groq_generate,
    clean_tweets
)

app = FastAPI(
    title="Groq Tweet Generator API",
    description="Generate 10 human-like tweets using LLaMA 3.3 and live web data",
    version="1.0.0",
)

# CORS (optional for Swagger-only usage)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class TweetRequest(BaseModel):
    topic: str = Field(
        ...,
        example="OpenAI vs Google AI competition"
    )

class TweetResponse(BaseModel):
    tweets: list[str]

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

@app.post(
    "/generate_tweets",
    response_model=TweetResponse,
    tags=["Tweet Generator"]
)
async def generate_tweet_endpoint(request: TweetRequest):
    raw_results = serper_search(request.topic)
    articles = filter_sources(raw_results)
    web_context = build_context(articles)

    prompt = f"""
    You are writing tweets based ONLY on the sources below.

    CONTEXT:
    {web_context}

    TASK:
    Write EXACTLY 10 tweets.
    Each tweet must be inspired by a DIFFERENT source above.

    RULES:
    - Under 280 characters
    - One sentence only
    - No questions
    - No emojis
    - No URLs
    - No @mentions
    - No numbering or labels
    - Sound like a real human reacting to news
    - No hype or marketing tone

    OUTPUT:
    Return only the 10 tweets, each on a new line.
    """

    raw_output = groq_generate(prompt)
    tweets = clean_tweets(raw_output)

    return {"tweets": tweets}
