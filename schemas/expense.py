"""
Schema for creating an expense.
"""

from pydantic import BaseModel
from typing import List, Dict


class ExpenseRequest(BaseModel):
    paid_by: int
    users: List[int]
    amount: float
    group_id: int
    split_type: str  # EQUAL / EXACT / PERCENT
    splits: Dict[int, float] = {}  # user_id → amount or percentage