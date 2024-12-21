# # Todo: Make sure to update the logger with something that is more flexible so that i do not break the principle of DRY

import asyncio
import sys
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware
from unstract.llmwhisperer import LLMWhispererClientV2
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic_ai import Agent
import os
from backend.models import (
    ActivityRequest,
    SuggestionsResponse,
    StoryResponse,
    ThemeRequest,
)
from backend.ai.agents import (
    curator_agent,
    researcher_agent,
    search_agent,
    adapter_agent,
    generator_agent,
    keyword_agent,
    translator_agent,
)
import logfire

from backend.models.dependencies import ThemeDependencies

# Configure Logfire before other imports
logfire.configure()
logfire.install_auto_tracing(
    modules=["backend"], min_duration=0.01, check_imported_modules="warn"
)

# Dynamically add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))


# Retrieve API key from environment variable
api_key = os.getenv("LLMWHISPERER_API_KEY")
if not api_key:
    raise ValueError(
        "API key for LLMWhispererClientV2 is not set in environment variables."
    )

# Initialize the LLMWhispererClientV2 with the retrieved API key
llm_client = LLMWhispererClientV2(
    base_url="https://llmwhisperer-api.us-central.unstract.com/api/v2",
    api_key="sequ6Qlik-Y17Gn7rgn9i2jvzXxQISg9E7NHC79OZoA",
)

# Initialize FastAPI app
app = FastAPI()
logfire.instrument_fastapi(app)
logfire.info("Starting FastAPI application...")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------- PHASE 1: KEYWORD GENERATION AND SEARCH ------------------- #
# Todo: Add research agent in phase 1 to make sure that user has sufficient keywords


@app.post("/generate_keywords", response_model=SuggestionsResponse)
async def generate_keywords(request: ThemeRequest):
    """
    Generate standalone keywords for a theme using Keyword Agent.
    If no valid keywords are found, use Search Agent (Brave API) for fallback.
    """
    themeDepends = ThemeDependencies(theme=request.theme)
    try:
        result = await keyword_agent.run(
            f'You are an expert in popular culture references. Given the theme: "{request.theme}"'
        )
        keywords = result.data

        if not keywords:
            # Fallback to Search Agent if no keywords are found
            # Todo: Complete the search agent, atm agent is not complete yet and misses api key
            logfire.warning(
                "No valid keywords found. Invoking Search Agent as fallback."
            )
            results = await search_agent.run(
                "Fetch theme information", deps=themeDepends
            )
            keywords = results[:10]  # Limit results from Brave Search API
            logfire.info(f"Search Agent provided fallback keywords: {keywords}")

        if not keywords:
            raise HTTPException(status_code=404, detail="No keywords found.")

        return keywords

    except Exception as e:
        logfire.error(f"Error in keyword generation: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate keywords.")


# ------------------- PHASE 2: STORY GENERATION ------------------- #


@app.post("/generate_story", response_model=StoryResponse)
async def generate_story(request: ActivityRequest):
    """
    Generate a story using selected keywords and theme details.
    """
    with logfire.span("main:generate_story"):
        try:
            logfire.info(f"Generating story for theme '{request.theme}'")

            # Research theme details
            theme_details_result = await researcher_agent.run(
                {"theme": request.theme, "user_keywords": request.selected_keywords}
            )
            theme_details = theme_details_result.data

            # Map objects in the activity
            object_mapping_result = await adapter_agent.run(
                {
                    "theme": request.theme,
                    "activity_description": request.activity_description,
                    "user_keywords": request.selected_keywords,
                }
            )
            object_mapping = object_mapping_result.data

            # Generate story
            story_result = await generator_agent.run(
                {
                    "activity_description": request.activity_description,
                    "theme_details": theme_details,
                    "object_mapping": object_mapping,
                }
            )
            story = story_result.data

            # Translate story to user-selected language
            translation_result = await translator_agent.run(
                {"story": story, "target_language": request.language}
            )
            translated_story = translation_result.data

            logfire.info("Story generation completed successfully.")
            return StoryResponse(story=translated_story)

        except Exception as e:
            logfire.error(f"Error generating story: {e}")
            raise HTTPException(status_code=500, detail="Failed to generate story.")


# ------------------- HEALTH CHECK ------------------- #


@app.get("/health")
def health_check():
    """Health check endpoint to ensure the API is running."""
    logfire.info("Health check endpoint was called.")
    return {"status": "OK", "message": "API is up and running!"}


# Directory where files will be stored
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@app.post("/upload_activity/")
async def upload_activity(file: UploadFile = File(...)):
    try:
        file_location = UPLOAD_DIR / file.filename
        with open(file_location, "wb") as f:
            f.write(await file.read())
        logfire.info(f"File uploaded successfully: {file_location}")

        # content = await file.read()
        # # Process with LLMWhisperer
        # print(content)
        result = llm_client.whisper(file_path=file_location, wait_for_completion=True)
        print(result)
        extracted_text = result.get("extraction", {}).get("result_text", "")
        if not extracted_text:
            raise HTTPException(
                status_code=500, detail="Failed to extract text from the document."
            )
        theme_remover_agent = Agent()
        sanitized_content = await theme_remover_agent.run(
            f"Remove any themes from the following content. Make sure to only provide the result! Content:{extracted_text}",
            model="groq:llama-3.3-70b-versatile",
        )
        print(sanitized_content)

        return {"sanitized_content": sanitized_content}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process file: {e}")


# ------------------- CLI WORKFLOW ------------------- #


async def cli_workflow():
    """
    CLI workflow for testing the agents in sequence.
    """
    logfire.info("Starting the CLI-based multi-agent workflow.")

    deps = {
        "theme": "Mario",
        "activity_description": "running through tunnels and throwing balls",
        "user_keywords": ["Luigi", "Mushroom", "Santa"],
    }

    # Step 1: Curator Agent
    curator_result = await curator_agent.run(deps)
    logfire.info(f"Curator Result: {curator_result.data}")

    # Step 2: Researcher Agent
    researcher_result = await researcher_agent.run(deps)
    logfire.info(f"Researcher Result: {researcher_result.data}")

    # Step 3: Search Agent (Fallback)
    if not researcher_result.data:
        search_result = await search_agent.run(deps)
        logfire.info(f"Search Result: {search_result.data}")
        deps["theme_info"] = search_result.data  # Pass search results to next agents

    # Step 4: Adapter Agent
    adapter_result = await adapter_agent.run(deps)
    logfire.info(f"Adapter Result: {adapter_result.data}")

    # Step 5: Generator Agent
    generator_result = await generator_agent.run(deps)
    logfire.info(f"Generated Story: {generator_result.data}")

    print("\nGenerated Story:\n", generator_result.data)


# Entry point for CLI execution
if __name__ == "__main__":
    if "uvicorn" in sys.argv[0]:
        pass  # Allow uvicorn to start FastAPI app
    else:
        asyncio.run(cli_workflow())
