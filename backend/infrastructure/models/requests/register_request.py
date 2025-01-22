from pydantic import BaseModel


# providing the possibility to extend the register
class RegisterRequest(BaseModel):
    username: str
    password: str
