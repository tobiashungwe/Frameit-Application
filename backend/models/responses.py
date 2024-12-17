from pydantic import BaseModel


class SuggestionsResponse(BaseModel):
    suggestions: list[str]


class StoryResponse(BaseModel):
    story: str


class KeywordsResponse(BaseModel):
    keywords: list[str]
