# Ambient Expense Agent Pro
**Track:** Agents for Business | **Kaggle 5-Day Intensive Vibe Coding Capstone**

## Problem Statement
Corporate expense management relies on manual managerial review. Low-value expenses waste time, while high-value expenses leak through without proper audit. 

## Solution & Architecture
This project implements an **Ambient ADK 2.0 Agent** with a smart routing graph:
1. **MCP Server Integration:** Checks local `employee_data.db` to ensure the employee has sufficient budget.
2. **Deterministic Fast-Track:** Auto-approves expenses < $100 without using LLM credits.
3. **Security PII Scrubber:** Scrubs Credit Card / SSN data from descriptions using regex.
4. **Generative LLM Review:** High-value expenses are routed to Gemini for fraud/policy auditing.
5. **Deployability:** Packaged with FastAPI and Docker.

## Setup Instructions
1. `pip install -r requirements.txt`
2. `export GEMINI_API_KEY="your_key_here"`
3. Run the app: `python app.py`
4. Send a test POST request to `http://localhost:8000/submit_expense`:
```json
{
  "emp_id": "EMP001",
  "amount": 1200.0,
  "description": "Flight to Vegas 1234-5678-9012-3456"
}
```
