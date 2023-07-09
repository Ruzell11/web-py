import sqlalchemy
import databases
from sqlalchemy.ext.declarative import declarative_base
from constants.index import DATABASE_URL



def startDatabase():
    
    database = databases.Database(DATABASE_URL)
    metadata = sqlalchemy.MetaData()
    
    engine = sqlalchemy.create_engine(DATABASE_URL)
    
    metadata.create_all(engine)
    
    return database

Base = declarative_base()

