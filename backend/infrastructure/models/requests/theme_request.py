from pydantic import BaseModel


class ThemeRequest(BaseModel):
    theme: str
