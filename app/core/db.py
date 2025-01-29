from sqlmodel import Session, create_engine, select, SQLModel

from entities.user.crud import create_db_user
from core.config import settings
from entities.user.model import User, UserCreate
from entities.budget.model import Budget
from entities.category.model import Category
from entities.spend.model import Spend
from entities.links import UserBudgetLink

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))

def init_db(session: Session) -> None:
  
    SQLModel.metadata.create_all(engine)

    user = session.exec(
        select(User).where(User.email == settings.FIRST_SUPERUSER)
    ).first()
    if not user:
        user_in = UserCreate(
            email=settings.FIRST_SUPERUSER,
            login='superuser',
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
            first_name='Ivan',
            second_name='Leonov'
        )
        user = create_db_user(session=session, user_create=user_in)