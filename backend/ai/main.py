import asyncio
from models.dependencies import ThemeDependencies
from agents.curator_agent import curator_agent
from agents.researcher_agent import researcher_agent
from agents.adapter_agent import adapter_agent
from agents.generator_agent import generator_agent
from agents.search_agent import search_agent
from logger_config import logger


async def main():
    logger.info("Starting the multi-agent workflow.")

    deps = ThemeDependencies(
        theme="Mario",
        activity_description="running through tunnels and throwing balls",
        user_keywords=["Luigi", "Mushroom", "Santa"],
    )

    # Curator Agent
    curator_result = await curator_agent.run(deps=deps)
    logger.info(f"Curator Result: {curator_result.data.snippets}")

    # Researcher Agent
    researcher_result = await researcher_agent.run(deps=deps)
    logger.info(f"Researcher Result: {researcher_result.data.snippets}")

    # Search Agent (if needed)
    if not researcher_result.data.snippets:
        search_result = await search_agent.run(deps=deps)
        logger.info(f"Search Result: {search_result.data.snippets}")
        deps.theme_info = (
            search_result.data.snippets
        )  # Pass search results to next agents

    # Adapter Agent
    adapter_result = await adapter_agent.run(deps=deps)
    logger.info(f"Adapter Result: {adapter_result.data.snippets}")

    # Generator Agent
    generator_result = await generator_agent.run(deps=deps)
    logger.info(f"Generated Story: {generator_result.data.story}")

    print("Generated Story:\n", generator_result.data.story)


if __name__ == "__main__":
    asyncio.run(main())
