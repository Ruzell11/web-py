from fastapi import FastAPI
from database.db import startDatabase
from routes.index import router as generalRoutes

app = FastAPI()
database = startDatabase()


@app.on_event("startup")
async def startup():
    await database.connect()
    if database.is_connected:
        print("Db connected")
    else:
        print("Db not connected")
    
    
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(generalRoutes)