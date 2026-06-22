import requests
import sys

BASE_URL = "http://localhost:8000"

def run_tests():
    print("Running Baseline Tests...\n")
    
    # Test 1: Fast-track approval (< $100)
    print("Test 1: Fast-track auto-approval (Amount < $100)")
    r1 = requests.post(f"{BASE_URL}/submit_expense", json={
        "emp_id": "EMP001", "amount": 45.0, "description": "Coffee for client"
    })
    print(f"Result: {r1.json()}\n")
    
    # Test 2: High-value expense requiring LLM Review
    print("Test 2: High-value expense (LLM Review required)")
    r2 = requests.post(f"{BASE_URL}/submit_expense", json={
        "emp_id": "EMP001", "amount": 1200.0, "description": "Flight to Vegas 1234-5678-9012-3456"
    })
    print(f"Result: {r2.json()}\n")
    
    # Test 3: Insufficient Budget (MCP DB check)
    print("Test 3: Budget Exceeded")
    # Assuming EMP001 has a set budget, let's try a huge amount
    r3 = requests.post(f"{BASE_URL}/submit_expense", json={
        "emp_id": "EMP001", "amount": 99999.0, "description": "Buying a yacht"
    })
    print(f"Result: {r3.json()}\n")

if __name__ == "__main__":
    try:
        requests.get(f"{BASE_URL}/docs")
        run_tests()
    except requests.exceptions.ConnectionError:
        print("Error: FastAPI server is not reachable. Make sure it is running on port 8000.")
        sys.exit(1)
