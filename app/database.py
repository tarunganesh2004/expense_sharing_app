"""
for production , postgresql can be used directly
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./expense.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
