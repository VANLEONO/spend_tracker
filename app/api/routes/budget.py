from typing import Annotated
from api.deps import SessionDep, CurrentUser, is_user_participant
from fastapi import APIRouter, Depends, HTTPException
from entities.category.model import CategoryPublic, Category
from entities.budget.model import BudgetPublic, BudgetCreate, Budget
from entities.budget.crud import create_db_budget, update_db_budget_spends, update_db_spend
from entities.user.model import UserPublic, User
from entities.spend.model import SpendCreate, Spend, SpendPublic, SpendUpdate
from sqlmodel import select
import uuid

router = APIRouter(prefix='/budgets', tags=['budget'])

@router.post('/', response_model=UserPublic)
def create_budget(*, session: SessionDep, budget: BudgetCreate, current_user: CurrentUser):
  create_db_budget(session, budget, current_user)
  user = session.get(User, current_user.id)
  return current_user

@router.get('/', response_model=list[BudgetPublic])
def get_budget(*, session: SessionDep, current_user: CurrentUser):
  print(current_user)
  user = session.get(User, current_user.id)
  return user.budgets

@router.get('/{budget_id}/categories/', dependencies=[Depends(is_user_participant)], response_model=list[CategoryPublic])
def get_budget_categories(*, budget_id: uuid.UUID,  session: SessionDep, current_user: CurrentUser):
  db_budget = session.exec(select(Budget).where(Budget.id == budget_id)).first()
  
  return db_budget.categories

@router.get('/{budget_id}/spends/', dependencies=[Depends(is_user_participant)], response_model=list[SpendPublic])
def get_budget_spends(*, budget_id: uuid.UUID,  session: SessionDep, current_user: CurrentUser):

  spends  = session.exec(select(Spend, Category).where(Spend.budget_id == budget_id).join(Category))
  results = []
  for spend, category in spends:
    results.append(SpendPublic(**dict(spend), category=CategoryPublic(color=category.color, id=category.id, title=category.title)))
  return results

@router.post('/{budget_id}/spends/', dependencies=[Depends(is_user_participant)], response_model=list[SpendPublic])
def create_spend(*, budget_id: uuid.UUID,  session: SessionDep, current_user: CurrentUser, spend: SpendCreate):
  db_budget = session.get(Budget, budget_id)
  update_db_budget_spends(session, db_budget, spend)
  spends  = session.exec(select(Spend, Category).where(Spend.budget_id == budget_id).join(Category))
  results = []
  for spend, category in spends:
    results.append(SpendPublic(**dict(spend), category=CategoryPublic(color=category.color, id=category.id, title=category.title)))
  return results

@router.patch('/{budget_id}/spends/{spend_id}/', dependencies=[Depends(is_user_participant)], response_model=Spend)
def update_spend(*, budget_id: uuid.UUID, spend_id: int, session: SessionDep, spend: SpendUpdate, current_user: CurrentUser):

  target_spend = session.get(Spend, spend_id)

  updated_spend = update_db_spend(session, target_spend, spend)
  return updated_spend

@router.delete('/{budget_id}/spends/{spend_id}', dependencies=[Depends(is_user_participant)], response_model=list[SpendPublic])
def delete_spend(*, budget_id: uuid.UUID, spend_id: int, session: SessionDep, current_user: CurrentUser):
  target_spend = session.get(Spend, spend_id)
  session.delete(target_spend)
  session.commit()
  spends = session.exec(select(Spend, Category).where(Spend.budget_id == budget_id).join(Category))
  results = []
  for spend, category in spends:
    results.append(SpendPublic(**dict(spend), category=CategoryPublic(color=category.color, id=category.id, title=category.title)))
  return results