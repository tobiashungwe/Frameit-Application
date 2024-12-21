from pydantic_ai import Agent, RunContext, ModelRetry
from backend.models import ThemeDependencies, SuggestionsResponse
import logfire

logfire.configure()

# Define the Keyword Agent
keyword_agent = Agent(
    "groq:llama-3.3-70b-versatile",
    deps_type=ThemeDependencies,
    result_type=SuggestionsResponse,
    system_prompt="provide a diverse assortment of the most iconic, widely recognized character names, significant locations and objects strongly associated with that theme. Your answer should be a concise list of single-word or compound-noun keywords, each instantly familiar to fans. Do not include episode titles, game names, merchandise items, explanations, or numeric references. Randomize both your selection and their order, offering a fresh and varied set each time. Give me a list of 24 keywords",
)


# @keyword_agent.result_validator
async def validate_result(
    ctx: RunContext[ThemeDependencies], result: SuggestionsResponse
) -> SuggestionsResponse:
    """
    Validates the result to ensure it meets the specified criteria.
    """
    valid_keywords = SuggestionsResponse.validate_keywords(result.suggestions)
    if not valid_keywords:
        raise ModelRetry("No valid keywords found; retrying with adjusted parameters.")
    return SuggestionsResponse(suggestions=valid_keywords)
