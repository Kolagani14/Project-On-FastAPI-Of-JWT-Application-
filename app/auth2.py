from passlib.context import CryptContext
from jose import jwt,JWTError
from datetime import timedelta,datetime,timezone
key="mysecretkey"
algorithm="HS256"
token_expire_minutes=30

def create_access_token(data:dict,expire_delta:timedelta|None=None):
   to_encode = data.copy()
   expire = datetime.now(timezone.utc)+(expire_delta or timedelta(15))
   to_encode.update({"exp":expire})
   return jwt.encode(to_encode,key,algorithm=algorithm)


def verify_token(token:str):
   try:
       payload=jwt.decode(token,key,algorithms=algorithm)
       return payload
   except JWTError:
      return None
   

#authentication
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
def hash_password(password:str):
   return pwd_context.hash(password)
def verify_password(plain:str,hashed:str):
   return pwd_context.verify(plain,hashed)