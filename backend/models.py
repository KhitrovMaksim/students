from sqlalchemy import Column, Integer, String
from database import Base


class Students(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(String)
    email = Column(String)
    phone = Column(String)
    favorite_sports = Column(String)
