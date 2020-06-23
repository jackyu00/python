
import os

for dirPath, dirNames, fileNames in os.walk("D:/downloads"):
    print (dirPath)
    for f in dirNames :
        print(os.path.join(dirPath,f))
		
		
#--------------------------------------------------------------------------		
from os import listdir
from os.path import isfile, isdir, join

mypath = "/var/log"

files = listdir(mypath)

for f in files:
  fullpath = join(mypath, f)
  if isfile(fullpath):
    print("file:", f)
  elif isdir(fullpath):
    print("folder:", f)