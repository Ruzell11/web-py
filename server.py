from fastapi import FastAPI
from database.db import database
from routes.index import router as generalRoutes
from dependecies.redis_session import redis_session


app = FastAPI()

@app.on_event("startup")
async def startup():
    redis_session();
    await database.connect()
    if database.is_connected:
        print("Db connected")
    else:
        print("Db not connected")
    
    
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(generalRoutes , prefix="/api")