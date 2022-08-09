
from sqlalchemy import Column, Integer, String

from . import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surename = Column(String)
    nickname = Column(String)
    username = Column(String)
    email = Column(String)
    password = Column(String)

    def as_dict(self):
        return {
            c.name: getattr(self, c.name) for c in self.__table__.columns
        }