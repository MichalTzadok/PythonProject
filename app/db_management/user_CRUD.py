from app.models.user import User
from app.db_management.config_db import users


async def get_all_users():
    users.find()
    return [User(**user) for user in users.find()]
