import sys, os, hashMod, filesizeMod, sqlite3
from ImageClass import Image
from pathlib import Path

#Open DB connection
#set db to save to memory
conn = sqlite3.connect(':memory:')

##set db to save to file
# conn = sqlite3.connect('images.db')

c = conn.cursor()
print("Starting DB connection")

#create table
print("Creating Images Table")
c.execute("""CREATE TABLE images (
    filename text,
    hash text,
    size integer
    )""")

#Set Path string
p = Path(r'R:\Images\Wallpapers')

#Start looping over images
for file in p.iterdir():

    #get image filename
    filename = str(file)
    # print(filename)

    #get image size
    size = filesizeMod.filesize(file)
    # print(size)

    #get image hash
    hash = hashMod.hasher(file)
    # print(hash)

    #insert recort into table
    img_record = Image(filename, size, hash)
    print("Inserting " + hash)
    c.execute("INSERT INTO images VALUES (:filename, :size, :hash)",{'filename': img_record.filename, 'size': img_record.size, 'hash': img_record.hash})
    conn.commit()

    # Find duplicate VALUES
    # c.execute("SELECT * FROM images WHERE hash='img_record.hash'")


# print(c.fetchall())


# #close DB connection
# conn.close()
# print("DB connection closed")
