import asyncio
import sys
from pathlib import Path

from fastapi import FastAPI  # , HTTPException
from fastapi.middleware.cors import CORSMiddleware

from backend.models.dependencies import ThemeDependencies
from backend.ai.agents import (
    curator_agent,
    researcher_agent,
    search_agent,
    adapter_agent,
    generator_agent,
    # keyword_agent,
    # ,  translator_agent, editor_agent
)
from backend.ai.agents.curator_agent import curator_router

# from backend.models import (
#     ActivityRequest,
#     SuggestionsResponse,
#     StoryResponse,
#     ThemeRequest,
# )

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


# # Generate Keywords Workflow
# @app.post("/generate_keywords", response_model=SuggestionsResponse)
# async def generate_keywords(request: ThemeRequest):
#     logfire.info(f"Generating keywords for theme: {request.theme}")
#     keywords = await keyword_agent.tools.fetch_keywords(request)
#     if not keywords:
#         logfire.info("No keywords found. Fetching via Search Agent.")
#         keywords = await search_keywords({"query": f"{request.theme} keywords"})
#     return SuggestionsResponse(suggestions=keywords)


# # PHASE 2: STORY GENERATION
# @app.post("/generate_story", response_model=StoryResponse)
# async def generate_story(request: ActivityRequest):
#     try:
#         theme = request.theme
#         selected_keywords = request.selected_keywords
#         activity_description = request.activity_description

#         logfire.info("Step 2.1: Fetching detailed theme data...")
#         theme_details = await researcher_agent.fetch_theme_details(theme, selected_keywords)

#         logfire.info("Step 2.2: Mapping activity objects...")
#         object_mapping = await adapter_agent.map_objects(activity_description, theme_details)

#         logfire.info("Step 2.3: Generating story...")
#         story = await generator_agent.generate_story(
#             activity_description, theme_details, object_mapping, selected_keywords
#         )

#         #ToDo: Add traslation agent
#         logfire.info("Step 2.4: Translating story...")
#         # translated_story = await translator_agent.translate_story(story, request.language)

#         return StoryResponse(story=translated_story)

#     except Exception as e:
#         logfire.error(f"Error generating story: {e}")
#         raise HTTPException(status_code=500, detail="Failed to generate story.")


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
