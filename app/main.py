from typing import Union, Annotated

from fastapi import FastAPI, Depends
from core.db import init_db, engine
from sqlmodel import Session, select
from entities.user.model import User
from api.deps import CurrentUser
from api.main import app_router

app = FastAPI()

def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

def init() -> None:
    with Session(engine) as session:
        init_db(session)

init()

app.include_router(app_router)