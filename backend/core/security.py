import jwt as pyjwt  # Explicitly alias PyJWT
from datetime import datetime, timedelta

# For demonstration only. Replace with your secure key handling.
SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: int = None):
    to_encode = data.copy()
    if expires_delta is None:
        expires_delta = ACCESS_TOKEN_EXPIRE_MINUTES
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    encoded_jwt = pyjwt.encode(
        to_encode, SECRET_KEY, algorithm=ALGORITHM
    )  # Use explicitly imported PyJWT
    return encoded_jwt
