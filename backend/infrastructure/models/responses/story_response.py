from pydantic import BaseModel, Field


class StoryResponse(BaseModel):
    story: str = Field(
        description=(
            "A story generated for a given theme and activity. The story should be a single string of text, "
            "formatted as a block of structured content. Empty lines and whitespace are automatically removed during "
            "processing."
        )
    )
