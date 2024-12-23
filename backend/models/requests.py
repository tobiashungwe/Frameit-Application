from pydantic import BaseModel
from typing import Optional, Union, List


class ThemeRequest(BaseModel):
    theme: str


class FileUpload(BaseModel):
    filename: str
    content: bytes


class ActivityRequest(BaseModel):
    theme: str
    exercise: FileUpload
    materials: Union[str, List[str]]
    terrain: str
    # Todo: current use string and int, but later only use int and use the correct handling to process this once the ui is thought out better.
    group_size: Optional[Union[int, str]] = None
    selected_keywords: list[str]
    language: str = "en"
