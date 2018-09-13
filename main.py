import sys, os, hashMod, filesizeMod, sqlite3
from ImageClass import Image
from pathlib import Path

#Open DB connection
conn = sqlite3.connect('images.db')
c = conn.cursor()
print("Starting DB connection")

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

    img_record = Image(filename, size, hash)
    c.execute("INSERT INTO images VALUES (:filename, :size, :hash)",{'filename': img_record.filename, 'size': img_record.size, 'hash': img_record.hash})
    conn.commit()



c.execute("SELECT * FROM images")
print(c.fetchall())


#close DB connection
conn.close()
print("DB connection closed")
