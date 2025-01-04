from pydantic_ai import Agent
from backend.infrastructure.models import ThemeDependencies, SuggestionsResponse
from backend.core.model_config import ModelConfig
import logfire
from backend.application.services.prompt_service import PromptService

logfire.configure()

# TODO: Add research agent in phase 1 to make sure that user has sufficient keywords


class KeywordAgent:
    def __init__(self, db):
        self.prompt_service = PromptService(db)

        static_prompt = self.prompt_service.get_prompt_template("keyword_agent_static")

        self.agent = Agent(
            model=ModelConfig.DEFAULT_MODEL,
            deps_type=ThemeDependencies,
            result_type=SuggestionsResponse,
            system_prompt=static_prompt,
        )


# TODO: Fix this validator and make sure it works with compound words!
# @keyword_agent.result_validator
# async def validate_result(
#    ctx: RunContext[ThemeDependencies], result: SuggestionsResponse
# ) -> SuggestionsResponse:
#    """
#    Validates the result to ensure it meets the specified criteria.
#    """
#    valid_keywords = SuggestionsResponse.validate_keywords(result.suggestions)
#    if not valid_keywords:
#        raise ModelRetry("No valid keywords found; retrying with adjusted parameters.")
#    return SuggestionsResponse(suggestions=valid_keywords)
