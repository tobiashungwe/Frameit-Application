from pydantic_ai import Agent, RunContext
from backend.core.model_config import ModelConfig
from backend.infrastructure.models import TranslationDependencies, TranslationResult
import logfire

logfire.configure()

translator_agent = Agent(
    model=ModelConfig.DEFAULT_MODEL,
    deps_type=TranslationDependencies,
    result_type=TranslationResult,
    system_prompt="Translate the given story into the specified target language.",
)


@translator_agent.system_prompt
async def translate_story(ctx: RunContext[TranslationDependencies]) -> str:
    with logfire.span("translator_agent:translate_story"):
        logfire.info(f"Translating story to '{ctx.deps.target_language}'...")
        response = f"Translate the following story into {ctx.deps.target_language}:\n\n{ctx.deps.story}"

        return response
