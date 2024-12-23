from pydantic import BaseModel, Field
import re


class SuggestionsResponse(BaseModel):
    suggestions: list[str] = Field(
        description="List of suggested keywords and compounds keywords."
    )

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


class ResearchResponse(BaseModel):
    details: list[str] = Field(
        description=(
            "A list of detailed explanations or analyses about a given theme, including information about its characters, "
            "items, and settings. Each item in the list corresponds to a line of structured content. Empty lines and "
            "whitespace are automatically removed during processing."
        )
    )


class AdapterResponse(BaseModel):
    object_mapping: list[str] = Field(
        description=(
            "A list of object mappings for a given activity in a theme. Each item in the list corresponds to a line of "
            "structured content. Empty lines and whitespace are automatically removed during processing."
        )
    )


class StoryResponse(BaseModel):
    story: str = Field(
        description=(
            "A story generated for a given theme and activity. The story should be a single string of text, "
            "formatted as a block of structured content. Empty lines and whitespace are automatically removed during "
            "processing."
        )
    )


class KeywordsResponse(BaseModel):
    keywords: list[str]
