from pydantic import BaseModel
class User_budget(BaseModel):
     user_id:int
     expenses:int
     revenues:int
