from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.expense import ExpenseRequest
from app.schemas.settlement import SettlementRequest
from app.services.expense_service import add_expense
from app.services.balance_service import simplify_group_balances
from app.services.settlement_service import settle_amount

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create an expense
@router.post("/expenses")
def create_expense(req: ExpenseRequest, db: Session = Depends(get_db)):
    add_expense(db, req)
    return {"message": "Expense added successfully"}


# Simplify balances for a group
@router.get("/groups/{group_id}/simplify")
def simplify(group_id: int, db: Session = Depends(get_db)):
    return simplify_group_balances(db, group_id)


# Settle an amount
@router.post("/settle")
def settle(req: SettlementRequest, db: Session = Depends(get_db)):
    settle_amount(db, req)
    return {"message": "Settlement recorded successfully"}