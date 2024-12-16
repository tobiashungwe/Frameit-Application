from pydantic_ai import Agent, RunContext
from typing import List
from fastapi import APIRouter
from backend.models import ThemeDependencies, SuggestionsResponse, ThemeRequest
import logfire

curator_router = APIRouter()

# Configure Logfire
logfire.configure()


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
        "Keywords should be concise and directly related to the theme, such as 'Mushroom', 'Pipe', 'Princess Peach'. "
        "Do not include explanatory text or numbers, only the keywords."
    ),
)


# Pydantic Models


@curator_agent.tool
async def suggest_keywords_tool(ctx: RunContext[ThemeDependencies]) -> List[str]:
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


@curator_router.post("/suggest_themes", response_model=SuggestionsResponse)
async def suggest_themes():
    """Fetch standalone theme suggestions from the Curator Agent."""
    async with curator_agent.run_stream("") as result:
        themes = []
        async for text in result.stream():
            themes.extend([theme.strip() for theme in text.split(",")])

    logfire.info(f"Suggested themes: {themes}")
    return SuggestionsResponse(suggestions=themes)


@curator_router.post("/suggest_keywords", response_model=SuggestionsResponse)
async def suggest_keywords(request: ThemeRequest):
    """Fetch standalone keywords for the given theme from the Keyword Agent."""
    async with keyword_agent.run_stream(request.theme) as result:
        raw_keywords = []
        async for text in result.stream():
            raw_keywords.extend(text.split("\n"))

    # Filter and clean the keywords
    keywords = []
    for keyword in raw_keywords:
        # Remove unnecessary phrases and ensure only valid keywords remain
        keyword = keyword.strip()
        if (
            keyword  # Non-empty
            and not keyword.startswith("Here are")  # Remove explanatory phrases
            and not keyword.startswith("1.")  # Remove numbered lists
            and not any(c.isdigit() for c in keyword)  # Ignore items with numbers
        ):
            keywords.append(keyword)

    keywords = list(set(keywords))

    logfire.info(f"Final cleaned keywords for '{request.theme}': {keywords}")
    return SuggestionsResponse(suggestions=keywords)
