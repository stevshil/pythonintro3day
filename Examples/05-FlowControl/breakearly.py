#!/usr/bin/env python

data = [1,3,5,42,4,6,65,42,5,6,7]

# Searching for the meaning of life
for item in data:
    if item == 42:
        print("Found 42 reporting life exists")
        nolife=1
        break

data = [1,3,5,4,6,65,5,6,7]
nolife=0
for item in data:
    if item == 42:
        print("Found 42 reporting life exists")
        nolife=1
        break

if nolife == 0:
    print("No life found")