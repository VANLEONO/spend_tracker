from fastapi import APIRouter, Depends, HTTPException
from api.deps import get_current_active_superuser, SessionDep, CurrentUser
from entities.user.model import UserPublic, UserUpdate, User, UserCreate
from entities.user.crud import get_user_by_email, update_db_user, create_db_user
from sqlmodel import select

router = APIRouter(prefix='/user', tags=['user'])

@router.patch('/{user_id}', dependencies=[Depends(get_current_active_superuser)], response_model=UserPublic)
def update_user(*, session: SessionDep, user_id: str, user_updates: UserUpdate):
    db_user = session.get(User, user_id)
    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="The user with this id does not exist in the system",
        )
    if user_updates.email:
        existing_user = get_user_by_email(session=session, email=user_updates.email)
        if existing_user and existing_user.id != user_id:
            raise HTTPException(
                status_code=409, detail="User with this email already exists"
            )

    db_user = update_db_user(session=session, db_user=db_user, user_updates=user_updates)
    return db_user

@router.post('/', dependencies=[Depends(get_current_active_superuser)], response_model=UserPublic)
def create_user(*, session: SessionDep, user_create: UserCreate):
    print(user_create)
    user = get_user_by_email(session=session, email=user_create.email)
    if user:
        raise HTTPException(
                status_code=409, detail="User with this email already exists"
            )
    db_user = create_db_user(session=session, user_create=user_create)
    return db_user

@router.get('/all/', dependencies=[Depends(get_current_active_superuser)])
def get_all_users(*, session: SessionDep):
    users = session.exec(select(User)).all()
    return users   

@router.get('/me/', response_model=UserPublic)
def get_current_user(*, current_user: CurrentUser):
    return current_user

