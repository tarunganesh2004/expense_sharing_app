"""
Schema for settlement requests.
"""

from pydantic import BaseModel


class SettlementRequest(BaseModel):
    from_user: int
    to_user: int
    amount: float
    group_id: int