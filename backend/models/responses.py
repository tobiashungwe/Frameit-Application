from pydantic import BaseModel, Field
import re


class SuggestionsResponse(BaseModel):
    suggestions: list[str] = Field(description="List of suggested keywords.")

    @classmethod
    def validate_keywords(cls, keywords: list[str]) -> list[str]:
        """
        Validates that each keyword is a single word or short compound noun
        and does not contain explanations or numbers.
        """
        valid_keywords = []
        for keyword in keywords:
            if re.match(r"^[A-Za-z-]+$", keyword):
                if len(keyword.split("-")) <= 3:
                    valid_keywords.append(keyword)
        return valid_keywords


class StoryResponse(BaseModel):
    story: str


class KeywordsResponse(BaseModel):
    keywords: list[str]
