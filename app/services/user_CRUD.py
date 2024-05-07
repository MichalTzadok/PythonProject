from app.models.user import User
from app.services.db import users

async def login(user: User):
    existing_user = users.find_one({"name": user.name, "password": user.password})
    if existing_user:
        return User(**existing_user)
    return "Error: Please sign up."

async def sign_up(new_user:User):
    users.insert_one({"id":new_user.id,"name": new_user.name, "password": new_user.password})
    return "Sign-up successful."

async def update_user(updated_user:User):
    filter = {"id": updated_user.id}
    new_values = {"$set": {"name": updated_user.name, "password": updated_user.password}}
    users.update_one(filter,new_values)
    return "Update successful."
