from pydantic import BaseModel, Field


class SearchResult(BaseModel):
    snippets: list[str] = Field(
        description="List of text snippets retrieved from search results."
    )


class ThemeResult(BaseModel):
    story: str = Field(description="Generated story based on the theme and activity.")


class TranslationResult(BaseModel):
    translated_text: str = Field(
        description=(
            "The text translated into the target language, maintaining the original meaning, tone, and cultural context."
        )
    )
    notes: list[str] = Field(
        default=[],
        description=(
            "Optional notes explaining translation choices, especially for ambiguous or culturally specific phrases."
        ),
    )
