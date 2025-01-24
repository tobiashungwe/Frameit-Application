from pydantic_ai import Agent, RunContext
from backend.infrastructure.models import ThemeResult
import logfire
from backend.infrastructure.models import GeneratorDependencies
from backend.core.model_config import ModelConfig
from backend.application.services.prompt_service import PromptService

logfire.configure()


class GeneratorAgent:
    def __init__(self, db):
        self.prompt_service = PromptService(db)

        static_prompt = self.prompt_service.get_prompt_template(
            "generator_agent_static"
        )

        self.agent = Agent(
            model=ModelConfig.DEFAULT_MODEL,
            deps_type=GeneratorDependencies,
            result_type=ThemeResult,
            retries=5,
            system_prompt=static_prompt,
        )

        @self.agent.system_prompt
        def create_story(ctx: RunContext[GeneratorDependencies]) -> str:
            """Generate a story based on the given theme and activity."""
            with logfire.span("generator_agent:create_story"):
                logfire.info(
                    f"Generating story for theme: '{ctx.deps.theme}' and activity: '{ctx.deps.exercise}'"
                )
                logfire.info(
                    f"theme_details type: {type(ctx.deps.theme_details)}, "
                    f"exercise type: {type(ctx.deps.exercise)}, "
                    f"object_mapping type: {type(ctx.deps.object_mapping)}"
                )

                return generate_multimove_story_prompt(
                    ctx.deps.theme,
                    ctx.deps.theme_details,
                    ctx.deps.exercise,
                    ctx.deps.object_mapping,
                )


def generate_multimove_story_prompt(
    theme: str,
    theme_details: list[str],
    activity_data: str,
    materials_mapping: list[str],
) -> str:
    """
    Generates a Multimove-themed story overlay prompt for a given theme, activity, and materials.

    Parameters:
    - theme (str): The desired theme for the story (e.g., "Mario", "Space Adventure").
    - theme_details (dict): Additional details or lore about the theme.
    - activity_data (dict): Parsed data of the activity, documenting its structure and elements.
    - materials_mapping (dict): A mapping of materials to their usage in the activity.

    Returns:
    - str: A dynamically generated prompt tailored to Multimove principles, the provided theme, activity, and materials.
    """

    # Format theme details as a bulleted list
    theme_context = "\n".join([f"- {detail}" for detail in theme_details])

    # Format activity documentation as a bulleted list
    activity_context = "\n".join([f"- {data}" for data in activity_data.split("\n")])

    # Format materials mapping as a bulleted list
    materials_context = "\n".join([f"- {material}" for material in materials_mapping])

    # Multimove-specific prompt
    prompt = f"""
    Create a {theme}-themed story overlay for the following Multimove activity. The story must adhere to the core principles of Multimove:

    - Multimove is designed for children aged 3 to 8 and focuses on broad motor skill development.
    - The goal is to foster a lifelong enjoyment of sports and physical activities, with fun and engagement as central pillars.
    - The activity must include challenges based on the 12 fundamental movement skills crucial for a child’s motor development:
        - Dribbling, hitting, kicking, catching/throwing
        - Sliding, lifting/carrying
        - Climbing
        - Rotating and swinging
        - Jumping/landing
        - Pulling/pushing
        - Walking/running

    The story should:

    - Be inspired by the {theme} universe, incorporating iconic characters, settings, and elements.
    - This will give you more information about the theme:
      {theme_context}
    - Be based on the documented Multimove activity structure:
      {activity_context}
    - Utilize the provided materials as follows:
      {materials_context}
    - Have a clear beginning, middle, and end, where participants complete Multimove skill challenges within the story's framework.
    - Turn each step or station in the activity into a {theme}-style challenge that aligns with Multimove principles. For example:
        - Crawling could become navigating tunnels or warp pipes (for Mario).
        - Throwing and catching could involve tossing objects to complete a quest (e.g., catching "star fragments").
    - Encourage cooperation, positive reinforcement, and enjoyment, reflecting the Multimove spirit.
    - Avoid repetitive or nonsensical sequences. Ensure logical progression, culminating in overcoming a final obstacle or achieving a key objective.
    - Maintain a child-friendly, engaging, and motivational tone.

    Based on this, generate the {theme}-themed Multimove story overlay following the above guidelines.
    """
    return prompt.strip()
