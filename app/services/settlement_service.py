"""
Handles settlements.
Instead of modifying existing data,
we add a reverse ledger entry.
"""

from app.models.ledger import Ledger


def settle_amount(db, req):
    reverse_entry = Ledger(
        from_user=req.to_user,  # Reverse direction
        to_user=req.from_user,
        amount=req.amount,
        group_id=req.group_id,
    )

    db.add(reverse_entry)
    db.commit()