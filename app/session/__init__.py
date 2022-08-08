from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData

engine = create_engine('sqlite:///testdb.sql')
Session = sessionmaker(bind=engine)