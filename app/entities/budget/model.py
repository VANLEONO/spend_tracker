from sqlmodel import SQLModel, Field, Relationship
from entities.links import UserBudgetLink
from datetime import datetime
import uuid
from typing import List

class BaseBudget(SQLModel):
  title: str = Field(max_length=255)
  created_at: datetime = Field(default_factory=datetime.now)
  description: str | None = Field(default=None, max_length=500)


class Budget(BaseBudget, table=True):
  id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
  categories: List["Category"] = Relationship(back_populates='budget')
  participants: List["User"] = Relationship(back_populates='budgets', link_model=UserBudgetLink)
  spends: List["Spend"] = Relationship(back_populates='budget')
  user_id: uuid.UUID

class BudgetCreate(BaseBudget):
  title: str

class BudgetPublic(BaseBudget):
  id: uuid.UUID
  title: str
  description: str | None
  created_at: datetime
  user_id: uuid.UUID