from sqlmodel import SQLModel,create_engine,Session
url="sqlite:///./users1.db"
engine=create_engine(url,echo=True)
SQLModel.metadata.create_all(engine)
def get_session():
   with Session(engine) as session:
      yield session