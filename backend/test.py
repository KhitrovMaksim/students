import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from fastapi import FastAPI, Depends

TEST_SERVER_DB_PASSWORD = os.environ.get('TEST_SERVER_DB_PASSWORD')
TEST_SERVER_HOST = os.environ.get('TEST_SERVER_HOST')

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://teacher:{TEST_SERVER_DB_PASSWORD}@host.docker.internal:3306/students"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Students(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(String)
    email = Column(String)
    phone = Column(String)
    favorite_sports = Column(String)

print("------------Base------------")
Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:

        db.close()


@app.get("/")
async def get_all_students():
    return {"Test"}


# @app.get("/students")
# async def get_all_students(db: Session = Depends(get_db)):
#     return db.query(Students).all()
