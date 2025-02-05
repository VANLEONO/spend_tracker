from fastapi import APIRouter
from api.routes import login, user, budget

app_router = APIRouter(prefix='/api/v1')

app_router.include_router(login.router)
app_router.include_router(user.router)
app_router.include_router(budget.router)
