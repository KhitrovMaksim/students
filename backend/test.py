import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from fastapi import FastAPI

TEST_SERVER_DB_PASSWORD = os.environ.get('TEST_SERVER_DB_PASSWORD')
TEST_SERVER_HOST = os.environ.get('TEST_SERVER_HOST')

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://teacher:{TEST_SERVER_DB_PASSWORD}@{TEST_SERVER_HOST}:3306/students"

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


app = FastAPI()


@app.get("/")
async def get_all_students():
    return SQLALCHEMY_DATABASE_URL
