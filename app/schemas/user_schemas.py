from sqlmodel import SQLModel
from pydantic import EmailStr
#after creating a user to validation
class create_user(SQLModel):
    name:str
    email:EmailStr
    password:str
#user login validation
class login_user(SQLModel):
    email:EmailStr
    password:str
class Token(SQLModel):
    access_token:str
    token_type:str