from typing import Union, Annotated

from fastapi import FastAPI, Depends
from core.db import init_db, engine
from sqlmodel import Session, select
from entities.user.model import User

app = FastAPI()

def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

def init() -> None:
    with Session(engine) as session:
        init_db(session)

init()

@app.get("/")
def read_root(session: SessionDep):
    user = session.exec(select(User).where(User.email == "admin@example.com"))
    return list(user)


@app.get("/items/{item_id}")
def read_item(item_id: int, c: Union[str, None] = None):
    return {"item_id": item_id, "g": c}