from sqlmodel import SQLModel, Field, Relationship
from entities.user.model import User
from entities.category.model import Category
from entities.spend.model import Spend
from datetime import datetime
import uuid

class BaseBudget(SQLModel):
  title: str = Field(max_length=255)
  created_at: datetime = Field(default_factory=datetime.now)
  description: str | None = Field(default=None, max_length=500)
  user_id: uuid.UUID


class Budget(BaseBudget, table=True):
  id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
  categories: list[Category] = Relationship(back_populates='budget')
  participants: list[User] = Relationship(back_populates='buget')
  spends: list[Spend] = Relationship(back_populates='bugget')
