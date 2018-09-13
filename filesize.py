import sys, os

def filesize(file):
    filesize = os.stat(imagePath)
    return(str(filesize))
