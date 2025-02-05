from sqlmodel import SQLModel, Field, Relationship
from entities.budget.model import Budget
import uuid
from typing import Optional
import random

def color():
  color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
  return color

class CategoryBase(SQLModel):
  title: str
  color: str = Field(default_factory=color)

class Category(CategoryBase, table=True):
  id: int = Field(default=None, primary_key=True)
  budget_id: Optional[uuid.UUID] = Field(default=None, foreign_key='budget.id')
  budget: Budget | None = Relationship(back_populates='categories')

class CategoryPublic(CategoryBase):
  title: str
  id: int