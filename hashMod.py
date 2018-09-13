import hashlib, os

print("Loading Hashing Module")
def hasher(path):
    #get file path
    imagePath = str(path)
    #set hasher
    hasher = hashlib.md5()
    with open(imagePath, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
        filehash = hasher.hexdigest()
    return(filehash)
