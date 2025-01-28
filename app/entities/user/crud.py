import uuid
from typing import Any

from sqlmodel import Session, select

from core.security import get_password_hash, verify_password
from entities.user.model import User, UserCreate, UserUpdate

def create_db_user(*, session: Session, user_create: UserCreate) -> User:
    db_obj = User.model_validate(
        user_create, update={"hashed_password": get_password_hash(user_create.password)}
    )
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj

def update_db_user(*, session: Session, db_user: User, user_updates: UserUpdate) -> User:
    plain_user = user_updates.model_dump(exclude_unset=True)
    if 'password' in plain_user:
        hashed = get_password_hash(plain_user['password'])
        plain_user['hashed_password'] = hashed
    db_user.sqlmodel_update(plain_user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def authenticate(*, session: Session, email, password) -> User:
    user = session.exec(select(User).where(User.email == email)).first()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

def get_user_by_email(*, session: Session, email: str) -> User:
    user = session.exec(select(User).where(User.email == email)).first()
    return user