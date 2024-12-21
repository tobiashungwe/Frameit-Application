from pydantic import BaseModel


class ThemeRequest(BaseModel):
    theme: str


class FileUpload(BaseModel):
    filename: str
    content: bytes


class ActivityRequest(BaseModel):
    theme: str
    excerise: FileUpload
    materials: list[str]
    terrain: str
    selected_keywords: list[str]
    language: str = "en"
