"""
Simplifies balances by minimizing transactions.
Uses net balance approach.
Time complexity: O(n log n)
"""

from collections import defaultdict
from app.models.ledger import Ledger


def simplify_group_balances(db, group_id):
    net_balance = defaultdict(float)

    # Build net balance for each user
    entries = db.query(Ledger).filter(Ledger.group_id == group_id).all()

    for entry in entries:
        net_balance[entry.from_user] -= entry.amount
        net_balance[entry.to_user] += entry.amount

    debtors = []
    creditors = []

    for user, balance in net_balance.items():
        if balance < 0:
            debtors.append([user, -balance])
        elif balance > 0:
            creditors.append([user, balance])

    i = j = 0
    simplified = []

    # Match debtors with creditors
    while i < len(debtors) and j < len(creditors):
        settle_amt = min(debtors[i][1], creditors[j][1])

        simplified.append(
            {
                "from": debtors[i][0],
                "to": creditors[j][0],
                "amount": round(settle_amt, 2),
            }
        )

        debtors[i][1] -= settle_amt
        creditors[j][1] -= settle_amt

        if debtors[i][1] == 0:
            i += 1
        if creditors[j][1] == 0:
            j += 1

    return simplified