from pydantic_ai import Agent, RunContext
from backend.models import ThemeDependencies
from typing import List
import logfire

logfire.configure()

# Define the Keyword Agent
keyword_agent = Agent(
    "groq:llama-3.3-70b-versatile",
    deps_type=ThemeDependencies,
    system_prompt="For the given theme, suggest the most relevant standalone keywords. "
    "Keywords must be concise, single words or short compound nouns. Avoid explanations or numbers.",
)


@keyword_agent.tool
async def fetch_keywords(ctx: RunContext[ThemeDependencies]) -> List[str]:
    """
    Fetch standalone keywords for a theme using streamed responses and clean them.
    Args:
        theme: The name of the theme (e.g., 'Mario', 'Christmas').

    Returns:
        A list of relevant standalone keywords.
    """
    with logfire.span("keyword_agent:fetch_keywords"):
        logfire.info(
            f"Fetching keywords for theme '{ctx.deps.theme}' using streamed responses."
        )

        # Run the agent in streamed mode
        raw_keywords = []
        async with ctx.agent.run_stream(ctx.deps.theme) as result:
            async for text in result.stream():
                raw_keywords.extend(text.split("\n"))

        # Filter and clean the keywords
        keywords = []
        for keyword in raw_keywords:
            keyword = keyword.strip()
            if (
                keyword  # Non-empty
                and not keyword.startswith("Here are")  # Remove unnecessary phrases
                and not keyword.startswith("1.")  # Remove numbered lists
                and not any(
                    c.isdigit() for c in keyword
                )  # Remove items containing numbers
            ):
                keywords.append(keyword)

        # Remove duplicates and log results
        unique_keywords = list(set(keywords))
        logfire.info(
            f"Cleaned keywords for theme '{ctx.deps.theme}': {unique_keywords}"
        )
        return unique_keywords
