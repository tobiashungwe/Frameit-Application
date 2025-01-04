from pydantic import BaseModel


class ThemeResponse(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True
