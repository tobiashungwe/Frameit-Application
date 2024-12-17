from pydantic_ai import Agent, RunContext
from backend.models import ResearchDependencies
from typing import Dict, List
import logfire

logfire.configure()

researcher_agent = Agent(
    "groq:llama-3.3-70b-versatile",
    deps_type=ResearchDependencies,
    system_prompt="Provide detailed and structured information about a given theme, including its characters, items, and settings.",
)


@researcher_agent.tool
async def fetch_theme_details(
    ctx: RunContext[ResearchDependencies],
) -> Dict[str, List[str]]:
    with logfire.span("researcher_agent:fetch_theme_details"):
        logfire.info(
            f"Researching theme '{ctx.deps.theme}' with keywords: {ctx.deps.user_keywords}"
        )
        response = await ctx.agent.run(
            f"Provide a detailed summary for the theme '{ctx.deps.theme}' including these keywords: "
            f"{', '.join(ctx.deps.user_keywords)}."
        )
        details = [line.strip() for line in response.data.split("\n") if line.strip()]
        return {"details": details}
