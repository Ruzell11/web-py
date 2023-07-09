from sqlalchemy.orm import Session
from database.db import SessionLocal

def get_db_session() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
