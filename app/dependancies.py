from fastapi import Depends,HTTPException
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session,select
from app.database import get_session
from app.auth2 import verify_token
from app.models.user_models import User


session_depends=Annotated[Session,Depends(get_session)]
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")
def get_cuurent_user(token:Annotated[str,Depends(oauth2_scheme)],session:session_depends):
   payload=verify_token(token)
   if not payload:
      raise HTTPException(status_code=401,detail="invalid token")
   user=session.exec(select(User).where(User.email==payload.get("sub"))).first()
   if not user:
      raise HTTPException(status_code=401,detail="user not found")
   return user