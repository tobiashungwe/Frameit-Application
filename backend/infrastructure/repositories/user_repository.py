from typing import Type
from sqlalchemy.orm import Session
from backend.domain.models.user_model import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, username: str, hashed_password: str) -> User:
        new_user = User(username=username, password=hashed_password)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def get_user_by_username(self, username: str) -> Type[User] | None:
        return self.db.query(User).filter(User.username == username).first()
