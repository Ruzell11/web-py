import sqlalchemy
import databases
from sqlalchemy.ext.declarative import declarative_base
from constants.index import DATABASE_URL
from sqlalchemy.orm import sessionmaker

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(DATABASE_URL)    
metadata.create_all(engine)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



