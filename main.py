import uvicorn as uvicorn
from fastapi import FastAPI

from app.routes import visualization_router
from app.routes.user_action_router import user_action_router
from app.routes.user_router import user_router
app = FastAPI()
app.include_router(user_router, prefix='/user')
app.include_router(user_action_router, prefix='/user_action')
# app.include_router(visualization_router, prefix='/visualization_router')

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)