
from schemas import  UserCreate
from models.User import User
from sqlalchemy.orm import Session
from fastapi import HTTPException

def store_user(user:UserCreate, db:Session):
  
        db_user = User(email=user.email, first_name=user.first_name)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        
        return db_user
       
   
