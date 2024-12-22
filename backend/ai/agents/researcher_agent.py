from pydantic_ai import Agent
from backend.models import ResearchDependencies, ResearchResponse
import logfire


logfire.configure()

RESEARCHER_SYSTEM_PROMPT = """
Provide detailed and structured information about a given theme, including its characters, items, and settings.
Make sure to include information that is relevant to the theme and its context.
"""

researcher_agent = Agent(
    "groq:llama-3.3-70b-versatile",
    deps_type=ResearchDependencies,
    result_type=ResearchResponse,
    system_prompt=RESEARCHER_SYSTEM_PROMPT,
)
