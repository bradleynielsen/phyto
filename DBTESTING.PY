##################
####TESTING#######
##################

c.execute("""CREATE TABLE images (
    filename text,
    hash text,
    size integer
    )""")

c.execute("INSERT INTO images VALUES ('R:\Images\WallpaperszynB8vW.jpg', '744518a9a4162ca8beab916324d25fec', 453083 )")
c.execute("SELECT * FROM images WHERE size=453083")
c.execute("SELECT * FROM images WHERE filename='R:\Images\WallpaperszynB8vW.jpg'")
c.execute("SELECT * FROM images")
print(c.fetchone())
c.fetchmany(5)
print(c.fetchall())










##################
####TESTING#######
##################
