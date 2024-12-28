from pydantic import BaseModel


class KeywordsResponse(BaseModel):
    keywords: list[str]
