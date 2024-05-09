from datetime import datetime

from pydantic import BaseModel
class User_budget(BaseModel):
     id:int
     user_id:str
     expenses:int
     revenues:int
     date_time:datetime
