from pydantic_ai import Agent, RunContext
from backend.models import ThemeDependencies
import logfire

logfire.configure()

adapter_agent = Agent(
    "groq:llama-3.3-70b-versatile",
    deps_type=ThemeDependencies,
    system_prompt="Map generic objects in '{activity_description}' to equivalents in the '{theme}' theme.",
)


@adapter_agent.tool
async def map_objects_to_theme(ctx: RunContext[ThemeDependencies]) -> dict:
    logfire.info(f"Adapter Agent: Mapping objects for theme '{ctx.deps.theme}'")
    if ctx.deps.theme.lower() == "mario":
        mapping = {"tunnel": "Warp Pipe", "ball": "Koopa Shell"}
    elif ctx.deps.theme.lower() == "christmas":
        mapping = {"tunnel": "Candy Cane Tunnel", "ball": "Snowball"}
    else:
        mapping = {}

    logfire.info(
        f"Adapter Agent: Generated object mapping for theme '{ctx.deps.theme}': {mapping}"
    )
    return mapping
