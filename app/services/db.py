from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client['Finance_Focus']
users = db['Users']
users_budgets = db['Users_Budgets']
