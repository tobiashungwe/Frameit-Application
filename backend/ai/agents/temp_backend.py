from fastapi import FastAPI
from pydantic import BaseModel
from pydantic_ai import Agent, RunContext
from fastapi.middleware.cors import CORSMiddleware
from models import ThemeDependencies
from typing import List


import logfire

# Configure Logfire
logfire.configure()

# Initialize FastAPI app
app = FastAPI()
logfire.instrument_fastapi(app)


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],  # Update this to match your React app's URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Curator Agent (Theme Suggestions)
curator_agent = Agent(
    "groq:llama-3.3-70b-versatile",
    system_prompt=(
        "Suggest standalone themes suitable for children’s activities. "
        "Each theme should be a single word or a compound noun, such as 'Mario', 'Minions', or 'Christmas'."
    ),
)

# Keyword Agent (Keyword Suggestions)
keyword_agent = Agent(
    "groq:llama-3.3-70b-versatile",
    system_prompt=(
        "For the given theme, suggest the most relevant standalone keywords. "
        "Keywords should be concise and directly related to the theme, such as 'Mushroom', 'Pipe', 'Princess Peach'."
    ),
)


# Pydantic Models
class ThemeRequest(BaseModel):
    theme: str


class SuggestionsResponse(BaseModel):
    suggestions: list[str]


@curator_agent.tool
async def suggest_keywords(ctx: RunContext[ThemeDependencies]) -> List[str]:
    logfire.info(f"Curator Agent: Received theme '{ctx.deps.theme}'")
    response = await ctx.agent.run(
        f"Provide a list of standalone keywords for the theme '{ctx.deps.theme}' without explanations or extra text."
    )
    raw_keywords = response.data
    logfire.info(f"Raw Keywords for theme '{ctx.deps.theme}': {raw_keywords}")

    # Post-process response to extract clean keywords
    keywords = [
        kw.strip()
        for kw in raw_keywords.split("\n")
        if kw.strip() and kw.strip().isdigit() is False
    ]
    logfire.info(f"Clean Keywords for theme '{ctx.deps.theme}': {keywords}")
    return keywords


@app.post("/suggest_themes", response_model=SuggestionsResponse)
async def suggest_themes():
    """Fetch standalone theme suggestions from the Curator Agent."""
    async with curator_agent.run_stream("") as result:
        themes = []
        async for text in result.stream():
            themes.extend([theme.strip() for theme in text.split(",")])

    logfire.info(f"Suggested themes: {themes}")
    return SuggestionsResponse(suggestions=themes)


@app.post("/suggest_keywords", response_model=SuggestionsResponse)
async def request_keywords(request: ThemeRequest):
    """Fetch standalone keywords for the given theme from the Keyword Agent."""
    async with keyword_agent.run_stream(request.theme) as result:
        keywords = []
        async for text in result.stream():
            keywords.extend([keyword.strip() for keyword in text.split(",")])

    logfire.info(f"Keywords for theme '{request.theme}': {keywords}")
    return SuggestionsResponse(suggestions=keywords)
