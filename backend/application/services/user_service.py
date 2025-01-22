from passlib.context import CryptContext
from sqlalchemy.orm import Session
from backend.infrastructure.repositories.user_repository import UserRepository
from backend.domain.models.user_model import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = UserRepository(db)

    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    def register_user(self, username: str, password: str) -> User:
        # Check if user already exists
        existing_user = self.repository.get_user_by_username(username)
        if existing_user:
            raise ValueError("User already exists")

        hashed_password = self.hash_password(password)
        return self.repository.create_user(username, hashed_password)

    def authenticate_user(self, username: str, password: str) -> User:
        user = self.repository.get_user_by_username(username)
        if not user:
            return None
        if not self.verify_password(password, user.password):
            return None
        return user
