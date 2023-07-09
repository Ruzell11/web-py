from pydantic import BaseModel , Field

class UserCreate(BaseModel):
    email: str
    first_name: str

class UserUpdate(BaseModel):
    email : str = Field(read_only=True)
    first_name: str = None
    
    class Config:
        keep_untouched = ("first_name")