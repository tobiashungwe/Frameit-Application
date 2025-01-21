from pydantic import BaseModel
from typing import Optional


class TerrainResponse(BaseModel):
    id: int
    name: str
    is_active: Optional[bool] = True
    user_id: Optional[int] = None
