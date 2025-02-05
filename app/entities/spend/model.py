from sqlmodel import SQLModel, Field, Relationship
from entities.budget.model import Budget
from entities.category.model import CategoryPublic
from datetime import date
import uuid

class BaseSpend(SQLModel):
  amount: int
  comment: str | None = Field(default=None, max_length=300)
  spend_date: date = Field(default_factory=date.today)
  

class Spend(BaseSpend, table=True):
  id: int = Field(default=None, primary_key=True)
  budget_id: uuid.UUID | None = Field(default=None, foreign_key='budget.id')
  budget: Budget | None = Relationship(back_populates='spends')
  category_id: int | None = Field(default=None, foreign_key='category.id')

class SpendCreate(BaseSpend):
  amount: int
  date: date
  category_id: int

class SpendUpdate(BaseSpend):
  amount: int | None = None
  spend_date: date | None = None
  category_id: int | None = None

class SpendPublic(BaseSpend):
  id: int
  amount: int
  comment: str
  spend_date: date
  category: CategoryPublic