from pydantic import BaseModel
from typing import Optional


class MaterialResponse(BaseModel):
    id: int
    name: str
    category: Optional[str] = None
    is_active: Optional[bool] = True
    user_id: Optional[int] = None
