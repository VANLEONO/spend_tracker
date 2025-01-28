from sqlmodel import SQLModel, Field
from entities.category import Category
from datetime import date
import uuid

class BaseSpend(SQLModel):
  category: Category
  amount: int
  comment: str | None = Field(default=None, max_length=300)
  date: date

class Spend(BaseSpend, table=True):
  id: int = Field(default=None, primary_key=True)
  budget_id: uuid.UUID = Field(foreign_key='budget.id')
