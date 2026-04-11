import sqlite3

# Connect to the database
conn = sqlite3.connect('hustle_theory.db')
cursor = conn.cursor()

# Get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("=" * 50)
print("HUSTLE THEORY DATABASE INSPECTION")
print("=" * 50)
print()

for table in tables:
    table_name = table[0]
    print(f"Table: {table_name}")
    print("-" * 50)
    
    # Get table structure
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    
    print("Columns:")
    for col in columns:
        col_id, col_name, col_type, not_null, default_val, pk = col
        pk_marker = " (PRIMARY KEY)" if pk else ""
        print(f"  - {col_name}: {col_type}{pk_marker}")
    
    # Count rows
    cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
    count = cursor.fetchone()[0]
    print(f"\nTotal rows: {count}")
    print()


conn.close()

print("=" * 50)
print("Database inspection complete!")
print("=" * 50)
