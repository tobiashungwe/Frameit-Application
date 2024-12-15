from pydantic_ai import Agent, RunContext
from backend.models.dependencies import ThemeDependencies
from backend.ai.agents import search_agent
import logfire

logfire.configure()

researcher_agent = Agent(
    "groq:llama-3.3-70b-versatile",
    deps_type=ThemeDependencies,
    system_prompt="Provide detailed information about the theme '{theme}'.",
)


@researcher_agent.tool
async def retrieve_theme_details(ctx: RunContext[ThemeDependencies]) -> dict:
    logfire.info(f"Researcher Agent: Retrieving details for theme '{ctx.deps.theme}'")
    if ctx.deps.theme.lower() == "mario":
        details = {
            "characters": ["Mario", "Luigi", "Princess Peach"],
            "items": ["Mushrooms", "Warp Pipes", "Fire Flowers"],
            "enemies": ["Goombas", "Koopas"],
            "settings": ["Mushroom Kingdom"],
        }
        logfire.info(
            f"Researcher Agent: Static details for '{ctx.deps.theme}' found: {details}"
        )
        return details

    # If no static details, fallback to SearchAgent
    search_result = await search_agent.run(deps=ctx.deps)
    logfire.info(
        f"Researcher Agent: Retrieved details via SearchAgent for '{ctx.deps.theme}': {search_result.data.snippets}"
    )
    return search_result.data.snippets
