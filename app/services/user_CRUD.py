from app.models.user import User
from app.services.db import users

async def login(user: User):
    found_user = users.find_one({"name": user.name, "password": user.password})
    if found_user:
        return User(**found_user)
    return "Error:please signUp"

async def sign_up(user:User):
    users.insert_one({"id":user.id,"name": user.name, "password": user.password})
    return "Sign-up successful."

async def update_user(user:User):
    filter = {"id": user.id}
    new_values = {"$set": {"name": user.name, "password": user.password}}
    users.update_one(filter,new_values)
    return "Update successful."
