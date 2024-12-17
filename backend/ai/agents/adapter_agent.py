from pydantic_ai import Agent, RunContext
from backend.models import AdapterDependencies
from typing import Dict
import logfire

logfire.configure()

adapter_agent = Agent(
    "groq:llama-3.3-70b-versatile",
    deps_type=AdapterDependencies,
    system_prompt="Map generic activity objects to equivalents in the given theme.",
)


@adapter_agent.tool
async def map_objects(ctx: RunContext[AdapterDependencies]) -> Dict[str, str]:
    with logfire.span("adapter_agent:map_objects"):
        logfire.info(
            f"Mapping objects for activity '{ctx.deps.activity_description}' in theme '{ctx.deps.theme}'"
        )
        response = await ctx.agent.run(
            f"Map the following activity description '{ctx.deps.activity_description}' "
            f"to equivalents based on theme '{ctx.deps.theme}' and these keywords: {', '.join(ctx.deps.user_keywords)}."
        )
        return {
            line.split(":")[0].strip(): line.split(":")[1].strip()
            for line in response.data.split("\n")
            if ":" in line
        }
