import sqlite3
import os

DB_PATH = os.path.join("database", "invoices.db")
os.makedirs("database", exist_ok=True)

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()


c.execute("""
CREATE TABLE IF NOT EXISTS invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    raw_text TEXT
)
""")
conn.commit()

def init_db():
    global conn, c
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

def insert_invoice(data: dict):
    """Insert only the raw_text into the database."""
    c.execute("INSERT INTO invoices (raw_text) VALUES (?)", (data["raw_text"],))
    conn.commit()

def query_invoices(sql_query: str):
    """Run any SQL query and return results as string."""
    c.execute(sql_query)
    rows = c.fetchall()
    return "\n".join(str(r) for r in rows)