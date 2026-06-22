import sqlite3

# MCP Server Concept: Local knowledge base access for the agent
DB_PATH = "employee_data.db"

def setup_db():
    """Creates a mock employee database."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS employees 
                 (emp_id TEXT PRIMARY KEY, name TEXT, remaining_budget REAL)''')
    
    # Insert mock data if empty
    c.execute("SELECT COUNT(*) FROM employees")
    if c.fetchone()[0] == 0:
        c.execute("INSERT INTO employees VALUES ('EMP001', 'Alice', 5000.00)")
        c.execute("INSERT INTO employees VALUES ('EMP002', 'Bob', 50.00)")
        conn.commit()
    conn.close()

def query_employee_budget(emp_id: str) -> float:
    """Agent uses this 'tool' to check budget before approving."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT remaining_budget FROM employees WHERE emp_id=?", (emp_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else 0.0
