from pydantic import BaseModel


class ThemeRequest(BaseModel):
    theme: str


class ActivityRequest(BaseModel):
    theme: str
    activity_description: str
    selected_keywords: list[str]
    language: str = "en"
