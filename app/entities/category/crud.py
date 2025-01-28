import uuid
from typing import Any

from sqlmodel import Session, select

from core.security import get_password_hash, verify_password
from entities.category.model import Category

def create_db_category(session: Session, category: Category):
  pass