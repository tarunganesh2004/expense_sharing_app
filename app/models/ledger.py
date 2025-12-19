"""
Ledger table - SINGLE SOURCE OF TRUTH.

Each row means:
'from_user owes to_user amount'

We never delete or modify rows.
Settlements are handled by reverse entries.
"""

from sqlalchemy import Column, Integer, Float
from app.database import Base


class Ledger(Base):
    __tablename__ = "ledger"

    id = Column(Integer, primary_key=True)
    from_user = Column(Integer, index=True)
    to_user = Column(Integer, index=True)
    amount = Column(Float)
    group_id = Column(Integer)