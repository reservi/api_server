from sqlalchemy import DateTime, String, Column, Integer

from . import Base

class ForbiddenTokenModel(Base):
    __tablename__ = "forbidden_tokens"

    id = Column(Integer, primary_key=True)
    token = Column(String)