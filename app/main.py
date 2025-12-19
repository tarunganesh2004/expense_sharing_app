from fastapi import FastAPI
from app.database import Base, engine
from app.routers import expenses

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Sharing Application")

# Register routes
app.include_router(expenses.router)