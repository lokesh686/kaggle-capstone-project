from fastapi import FastAPI
from pydantic import BaseModel
from mcp_database import setup_db
from agent_graph import process_expense

# Deployability Concept: Wrapping the agent in a REST API
app = FastAPI(title="Ambient Expense Agent Pro")

class ExpenseRequest(BaseModel):
    emp_id: str
    amount: float
    description: str

@app.on_event("startup")
def startup_event():
    setup_db()

@app.post("/submit_expense")
def submit_expense(expense: ExpenseRequest):
    decision = process_expense(expense.emp_id, expense.amount, expense.description)
    return decision

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
