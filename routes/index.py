from fastapi import APIRouter
from schemas import UserCreate
from controller.userController import store_user
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from dependecies.db_session import get_db_session


router = APIRouter()


@router.post('/register' )
async def register_user(user:UserCreate , db:Session = Depends(get_db_session)):
  
   return store_user(user,  db)