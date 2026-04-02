from fastapi import Depends,HTTPException,APIRouter
from sqlmodel import select
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from app.dependancies import session_depends,get_cuurent_user
from app.models.user_models import User
from app.schemas.user_schemas import create_user,Token
from app.auth2 import hash_password,verify_password,create_access_token
#instead of app we are using router
router=APIRouter()
@router.post("/registration")
def register(session:session_depends,user_data:create_user):
   if session.exec(select(User).where(User.email==user_data.email)).first():
      raise HTTPException(status_code=404,detail="already used")
   hash_pwd=hash_password(user_data.password)
   user=User(
                email=user_data.email,
                name=user_data.name,
                hashed_password=hash_pwd
            )
   session.add(user)
   session.commit()
   session.refresh(user)
   return user

@router.post("/login",response_model=Token)
def login(session:session_depends,form_data:Annotated[OAuth2PasswordRequestForm,Depends()]):
   user=session.exec(select(User).where(User.email==form_data.username)).first()
   if not user:
        raise HTTPException(status_code=401, detail="invalid credentials")     
   if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="invalid credentials")
   token=create_access_token(data={"sub":user.email})
   return {"access_token":token,"token_type":"bearer"}

@router.get("/profile")
def profile(current_user:Annotated[User,Depends(get_cuurent_user)]):
   return {"name":current_user,"email":current_user.email}
   
