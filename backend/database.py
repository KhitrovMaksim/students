import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


TEST_SERVER_DB_PASSWORD = os.environ.get('TEST_SERVER_DB_PASSWORD')
TEST_SERVER_HOST = os.environ.get('TEST_SERVER_HOST')

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://teacher:{TEST_SERVER_DB_PASSWORD}@{TEST_SERVER_HOST}:3306/students"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
