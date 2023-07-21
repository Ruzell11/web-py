
from schemas import  UserCreate , UserUpdate
from models.User import User
from sqlalchemy.orm import Session
from fastapi import HTTPException
from dependecies.redis_session import REDIS_HOST , REDIS_PORT
import redis

pool = redis.ConnectionPool(host=REDIS_HOST , port=REDIS_PORT)
redisSetter = redis.Redis(connection_pool=pool)


def store_user(user:UserCreate, db:Session):
  
        db_user = User(email=user.email, first_name=user.first_name)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        redisSetter.lpush("register1" , user.email)
        
        return {
                "message":"User created successfully",
                "user" : db_user
        }

def index_user(db:Session , skip: int = 0 , limit: int=100):
        return {
                "message" : "User lists",
                "user_list" : db.query(User).offset(skip).limit(limit).all()        
                }
        
def index_user_by_email(user_email:str , db:Session ):
      return db.query(User).filter(User.email == user_email).first()
        
   

def update_user_by_email(fieldForUpdate: UserUpdate, db: Session):
    user_exist = index_user_by_email(fieldForUpdate.email, db)
    if not user_exist:
        raise HTTPException(status_code=404, detail="User not found")

    for field, value in fieldForUpdate.model_dump(exclude_unset=True).items():
        setattr(user_exist, field, value)

    db.commit()
    db.refresh(user_exist)

    return {
            "message" : "Successfully edited",
            "user" : user_exist
    }
        
