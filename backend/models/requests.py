from pydantic import BaseModel
from typing import List


class ThemeRequest(BaseModel):
    theme: str


class KeywordsResponse(BaseModel):
    keywords: List[str]


class SuggestionsResponse(BaseModel):
    suggestions: list[str]
