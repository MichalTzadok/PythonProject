from fastapi import APIRouter
from app.services import user_service
from app.models.user import User
from utils.decorators import logger

user_router = APIRouter()

@user_router.post('/login')
@logger
async def login(user: User):
    user_found = await user_service.login(user)
    print(f"Message: user id: {user_found.id} login successful")
    return user_found


@user_router.post('/signup')
@logger
async def sign_up(user: User):
   new_user = await user_service.sign_up(user)
   print(f"message: user id: {user.id} Sign-up successful")
   return new_user


@user_router.put('/update')
@logger
async def update_user_detail(user: User):
        user = await user_service.update_user_detail(user)
        print(f"message: user id:  {user.id} Update successful")
        return user


@user_router.get('/get')
async def get_users():
    try:
       users_list= await user_service.get_users();
       print(f"message: get all users successfully")
       return users_list
    except Exception as e:
       print(f"An error occurred during get  users: {e}")
       raise e
@user_router.get('/get/{user_id}')
async def get_user_by_id(user_id: int):
    try:
        user_found = await user_service.get_user_by_id(user_id)
        print(f" message: get user id: {user_found.id}  successfully")
        return user_found
    except Exception as e:
        print(f"An error occurred during get user by id: {e}")
        raise e