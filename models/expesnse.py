"""
Expense table - stores expense metadata.
Actual balances are NOT stored here.
"""

from sqlalchemy import Column, Integer, Float, String
from app.database import Base


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer)
    paid_by = Column(Integer)
    total_amount = Column(Float)
    split_type = Column(String)  # EQUAL / EXACT / PERCENT