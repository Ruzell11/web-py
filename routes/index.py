from fastapi import APIRouter
from schemas import UserCreate , UserUpdate
from controller.userController import store_user , index_user , index_user_by_email , update_user_by_email
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from dependecies.db_session import get_db_session

router = APIRouter()

@router.post('/register' , response_model=UserCreate)
async def register_user(user:UserCreate , db:Session = Depends(get_db_session)):
   user_exist = index_user_by_email(user.email , db)
   if user_exist:
      raise HTTPException(status_code=400, detail="Email already registered")
   return store_user(user,  db)

@router.get('/users' )
async def user_list(db:Session = Depends(get_db_session)):
   return index_user(db)

@router.get('/user')
async def get_single_user(email:str, db:Session = Depends(get_db_session)):
   return index_user_by_email(email , db)

@router.patch('/user-update')
async def update_user( field:UserUpdate , db:Session = Depends(get_db_session)):
     return update_user_by_email(field , db)