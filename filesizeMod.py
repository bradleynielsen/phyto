import sys, os

def filesize(file):
    filesize = os.stat(str(file))
    return(filesize.st_size)
