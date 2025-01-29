from sqlmodel import SQLModel, Field, Relationship
from entities.budget.model import Budget
import uuid
from typing import Optional

class CategoryBase(SQLModel):
  title: str

class Category(CategoryBase, table=True):
  id: int = Field(default=None, primary_key=True)
  budget_id: Optional[uuid.UUID] = Field(default=None, foreign_key='budget.id')
  budget: Budget | None = Relationship(back_populates='categories')