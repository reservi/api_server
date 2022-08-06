
from sqlalchemy import Column, Integer, String

from . import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surename = Column(String)
    email = Column(String)
    password = Column(String)