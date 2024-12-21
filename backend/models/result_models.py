from pydantic import BaseModel, Field


class SearchResult(BaseModel):
    snippets: list[str] = Field(
        description="List of text snippets retrieved from search results."
    )


class ThemeResult(BaseModel):
    story: str = Field(description="Generated story based on the theme and activity.")
