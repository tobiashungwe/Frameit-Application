from pydantic import BaseModel


class FileUpload(BaseModel):
    filename: str
    content: bytes
    sanitize: bool
