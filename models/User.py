from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True , autoincrement=True)
    first_name= Column(String , unique=False, nullable=False)
    email = Column(String, unique=True, index=True , nullable=False)
   