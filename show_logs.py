import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM api_logs")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
