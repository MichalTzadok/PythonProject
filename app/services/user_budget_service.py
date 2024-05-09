from datetime import datetime

from pymongo import DESCENDING

from app.models.user_budget import User_budget
from app.services.db import users_budgets
async def Create(new_user_budget:User_budget):
    user_budget_id = await set_id()
    time_now=datetime.now()
    users_budgets.insert_one({
        "id": user_budget_id,
        "user_id":new_user_budget.user_id,
        "expenses":new_user_budget.expenses,
        "revenues":new_user_budget.revenues,
        "date_time":time_now
    })
    print("Create new user budget successful.")
    new_user_budget=users_budgets.find_one({"id":user_budget_id})
    return new_user_budget



async def set_id():
   max_id_document = users_budgets.find_one({}, sort=[("id", DESCENDING)])
   if max_id_document:
    return(max_id_document["id"]+1)
   else:
    return 0