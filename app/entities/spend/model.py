from sqlmodel import SQLModel, Field, Relationship
from entities.budget.model import Budget
from datetime import date
import uuid

class BaseSpend(SQLModel):
  category_id: str
  amount: int
  comment: str | None = Field(default=None, max_length=300)
  date: date

class Spend(BaseSpend, table=True):
  id: int = Field(default=None, primary_key=True)
  budget_id: uuid.UUID | None = Field(default=None, foreign_key='budget.id')
  budget: Budget | None = Relationship(back_populates='spends')
