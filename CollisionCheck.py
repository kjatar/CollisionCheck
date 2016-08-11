import hashlib
import collections
from os import walk
import sys

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

#Test to make sure sha1 results are accurate, may or may not need chunking.
def sha1(fname):
    hash_sha1 = hashlib.sha1()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha1.update(chunk)
    return hash_sha1.hexdigest()

print "Usage: CollisionCheck.py [target directory]"
print "Default is current directory.\n\n\n"


if(len(sys.argv) > 1):
  targetDir = sys.argv[1]
else:
  targetDir = "./"

filenamesList = []
filemd5List = []
fileshaList = []
collisions = 0

#Puts all filenames in the list.  Order will be reference point for hashes.
for (dirpath, dirnames, filenames) in walk(targetDir):
  filenamesList.extend(filenames)
  break

maxIterate = len(filenamesList)

for i in range (0, maxIterate):
    filemd5List.append(md5(targetDir+filenamesList[i]))
    fileshaList.append(sha1(targetDir+filenamesList[i]))
    #Check for collisions as we go along, print names of two files and the similar hash.
    for x in range (0, i-1):
        if(filemd5List[i] == filemd5List[x]):
            print "MD5 hash collision: \n" + filenamesList[i] + "\n" + filenamesList[x] + "\n" + filemd5List[x]
            collisions+=1
        if(fileshaList[i] == fileshaList[x]):
            print "SHA1 hash collision: \n" + filenamesList[i] + "\n" + filenamesList[x] + "\n" + fileshaList[x]
            collisions+=1

print "Collisions found: "
print collisions
