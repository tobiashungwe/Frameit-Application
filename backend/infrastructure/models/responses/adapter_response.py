from pydantic import BaseModel, Field


class AdapterResponse(BaseModel):
    object_mapping: list[str] = Field(
        description=(
            "A list of object mappings for a given activity in a theme. Each item in the list corresponds to a line of "
            "structured content. Empty lines and whitespace are automatically removed during processing."
        )
    )
