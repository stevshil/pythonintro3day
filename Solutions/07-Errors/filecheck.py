#!/usr/bin/env python

import sys

try:
    filename=sys.argv[1]
except:
    print("You need to supply a filename")
else:
    try:
        datafile=open(filename,"r")
    except:
        print("The file called "+filename+" does not exist")
    else:
        allLines=datafile.read()
        print(allLines)
        datafile.close()