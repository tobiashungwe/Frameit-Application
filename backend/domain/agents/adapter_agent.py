from pydantic_ai import Agent, RunContext
from backend.core.model_config import ModelConfig
from backend.infrastructure.models import AdapterDependencies, AdapterResponse
from typing import Dict
import logfire


logfire.configure()

adapter_agent = Agent(
    model=ModelConfig.DEFAULT_MODEL,
    deps_type=AdapterDependencies,
    result_type=AdapterResponse,
    system_prompt="Map generic activity objects to equivalents in the given theme.",
)


# Todo: Make sure to add a tool to extract the materials out of the document and other information!
@adapter_agent.system_prompt
async def map_objects(ctx: RunContext[AdapterDependencies]) -> Dict[str, str]:
    with logfire.span("adapter_agent:map_objects"):
        logfire.info(
            f"Mapping objects for activity '{ctx.deps.exercise}' in theme '{ctx.deps.theme}, make sure to also include these materials: {ctx.deps.materials}'"
        )
        response = f"Map the following activity description '{ctx.deps.exercise} to equivalents based on theme '{ctx.deps.theme}' and these keywords: {', '.join(ctx.deps.user_keywords)}."

        return response
