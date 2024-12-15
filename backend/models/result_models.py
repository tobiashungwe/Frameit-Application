from pydantic import BaseModel, Field
from typing import List


class SearchResult(BaseModel):
    snippets: List[str] = Field(
        description="List of text snippets retrieved from search results."
    )


class ThemeResult(BaseModel):
    story: str = Field(description="Generated story based on the theme and activity.")
