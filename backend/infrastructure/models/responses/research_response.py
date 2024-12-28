from pydantic import BaseModel, Field


class ResearchResponse(BaseModel):
    details: list[str] = Field(
        description=(
            "A list of detailed explanations or analyses about a given theme, including information about its characters, "
            "items, and settings. Each item in the list corresponds to a line of structured content. Empty lines and "
            "whitespace are automatically removed during processing."
        )
    )
