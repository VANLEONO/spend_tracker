from sqlmodel import SQLModel, Field
import uuid

class UserBudgetLink(SQLModel, table=True):
  user_id: uuid.UUID | None = Field(default=None, foreign_key='user.id', primary_key=True)
  budget_id: uuid.UUID | None = Field(default=None, foreign_key='budget.id', primary_key=True)