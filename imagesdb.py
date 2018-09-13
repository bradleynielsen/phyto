import sqlite3


#Open DB connection
conn = sqlite3.connect('images.db')
c = conn.cursor()
print("Starting DB connection")
conn.commit()

c.execute("SELECT * FROM images")
# print(c.fetchone())
# c.fetchmany(5)
print(c.fetchall())

#close DB connection
conn.close()
print("DB connection closed")
