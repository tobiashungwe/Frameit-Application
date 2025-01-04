from fastapi import APIRouter, HTTPException, File, UploadFile, Depends

# from backend.application.services.agent_service import AgentService
# TODO: Integerate with the database and the agent service make sure database is running and working with the agent service
# TODO: Change the agents to be more generic by creating a generic agent class and then creating specific agents that inherit from the generic agent class

from backend.core.database import get_db_session
from sqlalchemy.orm import Session
from backend.infrastructure.models.dependencies import (
    ThemeDependencies,
    ResearchDependencies,
    AdapterDependencies,
    GeneratorDependencies,
    TranslationDependencies,
)
from backend.infrastructure.models import (
    ThemeRequest,
    ActivityRequest,
    StoryResponse,
    SuggestionsResponse,
)
from backend.domain.agents import (
    KeywordAgent,
    SearchAgent,
    ResearchAgent,
    AdapterAgent,
    GeneratorAgent,
    ThemeRemoverAgent,
    TranslatorAgent,
)
import logfire
from pathlib import Path
import os
from unstract.llmwhisperer import LLMWhispererClientV2
from dotenv import load_dotenv


load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))


# Retrieve API key from environment variable
api_key = os.getenv("LLMWHISPERER_API_KEY")
if not api_key:
    raise ValueError(
        "API key for LLMWhispererClientV2 is not set in environment variables."
    )

# Initialize the LLMWhispererClientV2 with the retrieved API key
llm_client = LLMWhispererClientV2(
    base_url="https://llmwhisperer-api.us-central.unstract.com/api/v2",
    api_key=api_key,
)


router = APIRouter()

# ------------------- PHASE 1: KEYWORD GENERATION AND SEARCH ------------------- #


@router.post("/generate_keywords", response_model=SuggestionsResponse)
async def generate_keywords(
    request: ThemeRequest, db: Session = Depends(get_db_session)
):
    """
    Generate standalone keywords for a theme using Keyword Agent.
    If no valid keywords are found, use Search Agent (Brave API) for fallback.
    """
    themeDepends = ThemeDependencies(theme=request.theme)
    try:
        # Initialize agents
        keyword_agent = KeywordAgent(db)
        search_agent = SearchAgent(db)
        result = await keyword_agent.agent.run(
            f'You are an expert in popular culture references. Given the theme: "{request.theme}"',
            deps=themeDepends,
        )
        keywords = result.data

        if not keywords:
            # TODO: Complete the search agent, atm agent is not complete yet and misses api key
            logfire.warning(
                "No valid keywords found. Invoking Search Agent as fallback."
            )
            results = await search_agent.agent.run(
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


@router.post("/generate_story", response_model=StoryResponse)
async def generate_story(
    request: ActivityRequest, db: Session = Depends(get_db_session)
):
    """
    Generate a story using selected keywords and theme details.
    """
    with logfire.span("main:generate_story"):
        try:
            # Initialize agents
            researcher_agent = ResearchAgent(db)
            adapter_agent = AdapterAgent(db)
            generator_agent = GeneratorAgent(db)
            translator_agent = TranslatorAgent(db)

            try:
                logfire.info(
                    f"Generating story for theme '{request.theme}' with file '{request.exercise.filename}"
                )

                # Fetch theme details
                # TODO: add settings to configure if the agent should be used or not, this can be usefull for users if they want to save tokens
                with logfire.span("researcher_agent:research_theme"):
                    logfire.info("Research agent started job!")
                    theme_details_result = await researcher_agent.agent.run(
                        "Research this!",
                        deps=ResearchDependencies(
                            theme=request.theme, user_keywords=request.selected_keywords
                        ),
                    )
                    logfire.info(f"Theme details: {theme_details_result.data}")
            except Exception as e:
                logfire.error(f"Error fetching theme details: {e}")
                raise HTTPException(
                    status_code=500, detail="Failed to fetch theme details."
                )
            finally:
                logfire.info("Theme details fetched successfully.")

            theme_details = theme_details_result.data

            try:
                # Map objects in the activity
                with logfire.span("adapter_agent:map_objects"):
                    logfire.info("Adapter agent started job!")
                    object_mapping_result = await adapter_agent.agent.run(
                        "Map objects",
                        deps=AdapterDependencies(
                            theme=request.theme,
                            exercise=request.exercise.content,
                            user_keywords=request.selected_keywords,
                            materials=request.materials,
                        ),
                    )
                    logfire.info(f"Object mapping: {object_mapping_result.data}")
            except Exception as e:
                logfire.error(f"Error mapping objects: {e}")
                raise HTTPException(status_code=500, detail="Failed to map objects.")
            finally:
                logfire.info("Objects mapped successfully.")

            object_mapping = object_mapping_result.data

            try:
                # Generate story
                with logfire.span("generator_agent:create_story"):
                    logfire.info("Generator agent started job!")
                    story_result = await generator_agent.agent.run(
                        f"Create an engaging story for children that uses the theme: '{request.theme}' and incorporates the activity: '{request.exercise.content}', using the following keywords: {request.selected_keywords} in the story.",
                        deps=GeneratorDependencies(
                            theme=request.theme,
                            exercise=request.exercise.content,
                            theme_details=theme_details.details,
                            object_mapping=object_mapping.object_mapping,
                        ),
                    )
                    logfire.info(f"Generated story: {story_result.data}")
            except Exception as e:
                logfire.error(f"Error generating story: {e}")
                raise HTTPException(status_code=500, detail="Failed to generate story.")
            finally:
                logfire.info("Story generated successfully.")

            story = story_result.data

            try:
                # Translate story to user-selected language
                with logfire.span("translator_agent:translate_story"):
                    logfire.info("Translator agent started job!")
                    translation_result = await translator_agent.agent.run(
                        "Translate the text accurately and naturally, preserving its meaning, tone, and cultural context.",
                        deps=TranslationDependencies(
                            story=story, target_language=request.language
                        ),
                    )
                    logfire.info(f"Translated story: {translation_result.data}")
            except Exception as e:
                logfire.error(f"Error translating story: {e}")
                raise HTTPException(
                    status_code=500, detail="Failed to translate story."
                )
            finally:
                logfire.info("Story translated successfully.")

            translated_story = translation_result.data

            logfire.info("Story generation completed successfully.")
            return StoryResponse(story=translated_story.translated_text)

        except Exception as e:
            logfire.error(f"Error generating story: {e}")
            raise HTTPException(status_code=500, detail="Failed to generate story.")


# Directory where files will be stored
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/upload_activity/")
async def upload_activity(
    file: UploadFile = File(...), db: Session = Depends(get_db_session)
):
    try:
        # Initialize agents
        theme_remover_agent = ThemeRemoverAgent(db)

        file_location = UPLOAD_DIR / file.filename
        with open(file_location, "wb") as f:
            f.write(await file.read())
        logfire.info(f"File uploaded successfully: {file_location}")

        result = llm_client.whisper(file_path=file_location, wait_for_completion=True)
        logfire.info("LLMWhisperer processing completed.")

        extracted_text = result.get("extraction", {}).get("result_text", "")
        if not extracted_text:
            raise HTTPException(
                status_code=500, detail="Failed to extract text from the document."
            )

        sanitized_content = await theme_remover_agent.agent.run(
            f"Remove any themes from the following content. Content:{extracted_text}"
        )
        logfire.info("Content sanitized successfully.")

        return {"sanitized_content": sanitized_content}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process file: {e}")
