from fastapi import APIRouter
from app.db_management import user_CRUD

user_router = APIRouter()

@user_router.get('/all')
async def get_all_users():
    return await user_CRUD.get_all_users()
