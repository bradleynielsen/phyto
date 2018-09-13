import sys, os, hashMod, imagesdb, filesizeMod
from pathlib import Path



p = Path(r'R:\Images\Wallpapers')
for file in p.iterdir():
    #get image filename
    print(str(file))


    #get image size
    size = filesizeMod.filesize(file)
    print(size)


    #get image hash
    image = hashMod.hasher(file)
    print(image)
