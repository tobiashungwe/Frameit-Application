import asyncio
import sys
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.models.dependencies import ThemeDependencies
from backend.ai.agents.curator_agent import curator_agent
from backend.ai.agents.researcher_agent import researcher_agent
from backend.ai.agents.adapter_agent import adapter_agent
from backend.ai.agents.generator_agent import generator_agent
from backend.ai.agents.search_agent import search_agent
from backend.ai.agents.curator_agent import curator_router

import logfire

# Dynamically add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))


# Configure Logfire
logfire.configure()

# Todo: Make sure to update the logger with something that is more flexible so that i do not break the principle of DRY


app = FastAPI()
logfire.instrument_fastapi(app)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include agent router
app.include_router(curator_router, prefix="/curator", tags=["Curator Agent"])


# Define API routes for agents
@app.post("/curator")
async def run_curator_agent(deps: ThemeDependencies):
    return await curator_agent.run(deps)


@app.post("/researcher")
async def run_researcher_agent(deps: ThemeDependencies):
    return await researcher_agent.run(deps)


@app.post("/search")
async def run_search_agent(deps: ThemeDependencies):
    return await search_agent.run(deps)


@app.post("/adapter")
async def run_adapter_agent(deps: ThemeDependencies):
    return await adapter_agent.run(deps)


@app.post("/generator")
async def run_generator_agent(deps: ThemeDependencies):
    return await generator_agent.run(deps)


# CLI-based workflow
async def cli_workflow():
    logfire.info("Starting the multi-agent workflow.")

    deps = ThemeDependencies(
        theme="Mario",
        activity_description="running through tunnels and throwing balls",
        user_keywords=["Luigi", "Mushroom", "Santa"],
    )

    # Curator Agent
    curator_result = await curator_agent.run(deps=deps)
    logfire.info(f"Curator Result: {curator_result.data.snippets}")

    # Researcher Agent
    researcher_result = await researcher_agent.run(deps=deps)
    logfire.info(f"Researcher Result: {researcher_result.data.snippets}")

    # Search Agent (if needed)
    if not researcher_result.data.snippets:
        search_result = await search_agent.run(deps=deps)
        logfire.info(f"Search Result: {search_result.data.snippets}")
        deps.theme_info = (
            search_result.data.snippets
        )  # Pass search results to next agents

    # Adapter Agent
    adapter_result = await adapter_agent.run(deps=deps)
    logfire.info(f"Adapter Result: {adapter_result.data.snippets}")

    # Generator Agent
    generator_result = await generator_agent.run(deps=deps)
    logfire.info(f"Generated Story: {generator_result.data.story}")

    print("Generated Story:\n", generator_result.data.story)


# Entry point
if __name__ == "__main__":
    if "uvicorn" in sys.argv[0]:
        pass  # Allow uvicorn to start the FastAPI app
    else:
        asyncio.run(cli_workflow())
