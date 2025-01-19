from pydantic import BaseModel


class FileUpload(BaseModel):
    filename: str
    content: str
    sanitize: bool
