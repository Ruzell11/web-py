import sqlalchemy
import databases

SERVER_NAME = "localhost";
USER_NAME = "root";
PASSWORD = "";
DB_NAME = "python_database";
DATABASE_URL = f"mysql://{USER_NAME}:{PASSWORD}@{SERVER_NAME}/{DB_NAME}"


def startDatabase():
    
    database = databases.Database(DATABASE_URL)
    metadata = sqlalchemy.MetaData()
    
    engine = sqlalchemy.create_engine(DATABASE_URL)
    
    metadata.create_all(engine)
    
    return database


