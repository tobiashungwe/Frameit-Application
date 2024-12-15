import requests
from pydantic_ai import Agent, RunContext
from backend.models import ThemeDependencies, SearchResult
from backend.ai.model_config import ModelConfig
import logfire

logfire.configure()


class BraveSearch:
    def __init__(self):
        self.api_key = ModelConfig.BRAVE_API_KEY
        self.search_url = "https://api.search.brave.com/v1/search"

    def search(self, query: str) -> list:
        logfire.info(f"BraveSearch: Performing search for query '{query}'")
        headers = {"Accept": "application/json", "X-Subscription-Token": self.api_key}
        params = {"q": query, "count": 5}
        response = requests.get(self.search_url, headers=headers, params=params)
        if response.status_code == 200:
            snippets = [
                result["snippet"]
                for result in response.json().get("webPages", {}).get("value", [])
            ]
            logfire.info(
                f"BraveSearch: Retrieved {len(snippets)} snippets for query '{query}'"
            )
            return snippets
        logfire.error(
            f"BraveSearch: Failed search for query '{query}' with status code {response.status_code}"
        )
        response.raise_for_status()


search_agent = Agent(
    "groq:llama-3.3-70b-versatile",
    deps_type=ThemeDependencies,
    result_type=SearchResult,
    system_prompt="Fetch and summarize relevant information about '{theme}'.",
)


@search_agent.tool
async def fetch_theme_info(ctx: RunContext[ThemeDependencies]) -> list:
    logfire.info(f"Search Agent: Fetching theme info for '{ctx.deps.theme}'")
    brave = BraveSearch()
    results = brave.search(ctx.deps.theme)
    logfire.info(
        f"Search Agent: Retrieved {len(results)} results for theme '{ctx.deps.theme}'"
    )
    return results
