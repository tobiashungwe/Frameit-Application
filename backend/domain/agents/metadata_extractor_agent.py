import json
import logfire
from pydantic_ai import Agent, RunContext
from backend.application.services.prompt_service import PromptService
from backend.core.model_config import ModelConfig
from backend.infrastructure.models.dependencies import DocumentMetaDependencies

logfire.configure()


class MetaDataExtractorAgent:
    def __init__(self, db):
        self.prompt_service = PromptService(db)

        static_prompt = self.prompt_service.get_prompt_template(
            "metadata_extractor_static"
        )

        self.agent = Agent(
            model=ModelConfig.DEFAULT_MODEL,
            deps_type=DocumentMetaDependencies,
            system_prompt=static_prompt,
        )

        @self.agent.system_prompt
        def extract_metadata(
            ctx: RunContext[DocumentMetaDependencies],
        ) -> DocumentMetaDependencies:
            """
            Extract the materials, terrains, and group sizes/types from the document.
            Return them in a structured JSON format with keys: 'materials', 'terrains', 'groups'.
            """
            with logfire.span("metadata_extractor_agent:extract_metadata"):
                logfire.info("Generating metadata from provided content.")

                text_to_parse = getattr(ctx.deps, "text", "")

                # Generate the dynamic portion of the prompt based on the content.
                # The name is the dynamic prompt stored in your prompt_service
                # (e.g. "metadata_extractor_dynamic").
                response = self.prompt_service.generate_dynamic_prompt(
                    name="metadata_extractor_dynamic",
                    text=text_to_parse,
                )

                # We expect the LLM response to be valid JSON.
                # If your system returns raw text, parse or sanitize as needed.
                try:
                    parsed_response = json.loads(response.data)
                except json.JSONDecodeError:
                    # Handle or log error; return empty structure
                    logfire.error("Failed to decode JSON from response.")
                    parsed_response = {"materials": [], "terrains": [], "groups": []}

                # Return the structured data as a DocumentMeta object
                return DocumentMetaDependencies(**parsed_response)
