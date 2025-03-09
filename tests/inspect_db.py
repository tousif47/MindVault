# tests/inspect_db.py

import sqlite3
import os


# Connect to the database
db_path = os.path.join(os.path.dirname(__file__), "..", "test_mindvault.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# List all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in the database:")

for table in tables:
    print(table[0])

# Inspect the contents of each table
for table in tables:
    table_name = table[0]
    print(f"\nContents of table '{table_name}':")
    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)

# Close the connection
conn.close()