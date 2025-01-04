from pydantic import BaseModel
from typing import Optional, Union, List
from .file_upload import FileUpload


class ActivityRequest(BaseModel):
    theme: str
    exercise: FileUpload
    materials: Union[str, List[str]]
    terrain: str
    group_size: Optional[Union[int, str]] = None
    selected_keywords: list[str]
    language: str = "en"
