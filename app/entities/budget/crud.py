from sqlmodel import Session
from entities.budget.model import BudgetCreate, Budget
from entities.spend.model import SpendCreate, Spend, SpendUpdate
from entities.user.model import User
from entities.category.defaults import default_categories

def create_db_budget(session: Session, budget: BudgetCreate, db_user: User):
  db_obj = Budget.model_validate(budget, update={ 'user_id': db_user.id, 'categories': default_categories, 'participants': [db_user] })
  session.add(db_obj)
  session.commit()
  session.refresh(db_obj)
  return db_obj

def update_db_budget_spends(session: Session, db_budget: Budget, spend: SpendCreate):
  spend = Spend.model_validate(spend)
  db_budget.spends.append(spend)
  session.add(db_budget)
  session.commit()
  return db_budget

def update_db_spend(session: Session, db_spend: Spend, spend: SpendUpdate):
  spend_dump = spend.model_dump(exclude_unset=True)
  db_spend.sqlmodel_update(spend_dump)
  session.add(db_spend)
  session.commit()
  session.refresh(db_spend)
  return db_spend