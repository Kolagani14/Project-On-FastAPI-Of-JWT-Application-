from sqlmodel import SQLModel,Field
from typing import Optional
from pydantic import EmailStr
#create class
class User(SQLModel,table=True):
    id:Optional[int]=Field(default=None,primary_key=True)
    name:str
    email:EmailStr
    hashed_password:str