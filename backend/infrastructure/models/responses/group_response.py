from pydantic import BaseModel
from typing import Optional


class GroupResponse(BaseModel):
    id: int
    name: str
    is_active: Optional[bool] = True
