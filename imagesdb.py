import sqlite3

conn = sqlite3.connect('images.db')

c = conn.cursor()

print("Starting DB connection")

conn.commit()

conn.close()
print("DB connection closed")
