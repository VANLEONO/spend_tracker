import uuid
from typing import Any

from sqlmodel import Session, select

from core.security import get_password_hash, verify_password
from entities.user.model import User, UserCreate, UserUpdate

def create_user(*, session: Session, user_create: UserCreate) -> User:
    db_obj = User.model_validate(
        user_create, update={"hashed_password": get_password_hash(user_create.password)}
    )
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj