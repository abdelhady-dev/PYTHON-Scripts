import string
import math

from numpy import matrix

def decrypt(msg, key):
    msgLen = len(msg)
    cols = key

    rows = math.ceil(msgLen/cols)
    print = (rows)

    msgList = list(msg)

    matrix = [msgList[i : i + cols] for i in range(0, msgLen, cols)]
    msgDec = ""

    for i in range(cols):
        for row in matrix:
            msgDec += row[i]
    
    return msgDec

print('efg')
print(decrypt('efg', 3))