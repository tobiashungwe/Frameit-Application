from pydantic_ai import Agent, RunContext
from backend.models import ResearchDependencies, ResearchResponse
import logfire


logfire.configure()

RESEARCHER_SYSTEM_PROMPT = """
Provide detailed and structured information about a given theme, including its characters, items, and settings.
Make sure to include information that is relevant to the theme and its context. """

researcher_agent = Agent(
    "groq:llama-3.3-70b-versatile",
    deps_type=ResearchDependencies,
    result_type=ResearchResponse,
    system_prompt=RESEARCHER_SYSTEM_PROMPT,
)


@researcher_agent.system_prompt
def research_theme(ctx: RunContext[ResearchDependencies]) -> str:
    logfire.info(
        f"Researching theme '{ctx.deps.theme}' with keywords: {ctx.deps.user_keywords}"
    )
    return f"Provide a detailed summary for the theme '{ctx.deps.theme}' including these keywords: {', '.join(ctx.deps.user_keywords)}."
