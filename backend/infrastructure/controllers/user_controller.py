from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.application.services.user_service import UserService
from backend.core.database import get_db_session
from backend.core.security import create_access_token
from backend.infrastructure.models.requests.login_request import LoginRequest
from backend.infrastructure.models.requests.register_request import RegisterRequest

router = APIRouter()


@router.post("/register")
def register(request: RegisterRequest, db: Session = Depends(get_db_session)):
    user_service = UserService(db)
    try:
        user = user_service.register_user(request.username, request.password)
        return {"message": "User registered successfully", "user_id": user.id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db_session)):
    user_service = UserService(db)
    user = user_service.authenticate_user(request.username, request.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )
    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
