from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

#engine = create_engine("sqlite:///todo.db")
DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/ecom_db"
engine = create_engine(DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(bind = engine, expire_on_commit = False)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close
