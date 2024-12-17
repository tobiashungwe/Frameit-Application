from pydantic_ai import Agent, RunContext
from backend.models import ThemeDependencies
from typing import List
import logfire

logfire.configure()

curator_agent = Agent(
    "groq:llama-3.3-70b-versatile",
    deps_type=ThemeDependencies,
    system_prompt="Suggest standalone themes suitable for children’s activities. "
    "Each theme should be a single word or a short compound noun.",
)


@curator_agent.tool
async def suggest_themes(ctx: RunContext[ThemeDependencies]) -> List[str]:
    with logfire.span("curator_agent:suggest_themes"):
        logfire.info(f"Generating themes for query: '{ctx.deps.theme}'")
        response = await ctx.agent.run(f"Suggest themes related to '{ctx.deps.theme}'")
        return [theme.strip() for theme in response.data.split("\n") if theme.strip()]
