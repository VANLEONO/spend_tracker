from fastapi import FastAPI
from core.db import init_db, engine
from sqlmodel import Session
from api.main import app_router

app = FastAPI()


def init() -> None:
    with Session(engine) as session:
        init_db(session)

init()

app.include_router(app_router)