"""
Handles expense creation logic.
Supports:
- Equal split
- Exact split
- Percentage split
"""

from app.models.ledger import Ledger


def add_expense(db, req):
    # EQUAL SPLIT
    if req.split_type == "EQUAL":
        split_amount = req.amount / len(req.users)

        for user in req.users:
            if user != req.paid_by:
                db.add(
                    Ledger(
                        from_user=user,
                        to_user=req.paid_by,
                        amount=split_amount,
                        group_id=req.group_id,
                    )
                )

    # EXACT SPLIT
    elif req.split_type == "EXACT":
        for user, amt in req.splits.items():
            if user != req.paid_by:
                db.add(
                    Ledger(
                        from_user=user,
                        to_user=req.paid_by,
                        amount=amt,
                        group_id=req.group_id,
                    )
                )

    # PERCENTAGE SPLIT
    elif req.split_type == "PERCENT":
        for user, percent in req.splits.items():
            amt = (percent / 100) * req.amount
            if user != req.paid_by:
                db.add(
                    Ledger(
                        from_user=user,
                        to_user=req.paid_by,
                        amount=amt,
                        group_id=req.group_id,
                    )
                )

    db.commit()