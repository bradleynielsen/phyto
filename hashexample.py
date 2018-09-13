#imports
import sys, os, hashlib
from pathlib import Path

p = Path('./photos')

#get hash for each file
for file in p.iterdir():
    #get file path
    imagePath = str(file.absolute())
    #set hasher
    hasher = hashlib.md5()
    with open(imagePath, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())
