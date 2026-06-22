import os
from security import scrub_pii
from mcp_database import query_employee_budget
from google import genai

# Multi-Agent ADK Routing Concept
def process_expense(emp_id: str, amount: float, description: str) -> dict:
    """Routes the expense based on deterministic rules or LLM generative review."""
    
    # 1. Check MCP Database (Context)
    budget = query_employee_budget(emp_id)
    if amount > budget:
        return {"status": "REJECTED", "reason": f"Amount ${amount} exceeds remaining budget ${budget}."}

    # 2. ADK Deterministic Fast Path
    if amount < 100:
        return {"status": "APPROVED", "reason": "Deterministic Fast-Track (Under $100)"}
    
    # 3. Security PII Scrubbing
    safe_description = scrub_pii(description)

    # 4. LLM Generative Smart Path
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return {"status": "ERROR", "reason": "GEMINI_API_KEY not set. Cannot run LLM review."}
        
    try:
        client = genai.Client(api_key=api_key)
        prompt = f"You are a corporate expense auditor. Review this expense for policy violations. Amount: ${amount}. Description: '{safe_description}'. Respond strictly with 'APPROVED' or 'REJECTED' followed by a short reason."
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        llm_decision = response.text.strip()
        
        if llm_decision.startswith("APPROVED"):
            return {"status": "APPROVED", "reason": f"LLM Reviewed: {llm_decision}"}
        else:
            return {"status": "REJECTED", "reason": f"LLM Reviewed: {llm_decision}"}
            
    except Exception as e:
        return {"status": "ERROR", "reason": str(e)}
