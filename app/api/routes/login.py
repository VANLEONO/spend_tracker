from typing import Annotated
from api.deps import SessionDep, CurrentUser, Token
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException
from entities.user.model import UserPublic
from entities.user.crud import authenticate
from core.config import settings
from datetime import timedelta
from core.security import create_access_token


router = APIRouter(tags=['login'])

@router.post('/login')
def login(*, session: SessionDep, ):
  pass


@router.post("/login/access-token")
def login_access_token(
    session: SessionDep, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    user = authenticate(
        session=session, email=form_data.username, password=form_data.password
    )
    print(session)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return Token(
        access_token=create_access_token(
            user.id, expires_delta=access_token_expires
        )
    )


@router.post("/login/test-token", response_model=UserPublic)
def test_token(current_user: CurrentUser):
    """
    Test access token
    """
    return current_user
