#!/usr/bin/env python

import json

# Open the CSV file
dormantData = open("dormantcos.csv","r")

# Read in the header
header=(dormantData.readline()).strip()
# Turn header into list
header=header.split(",")

# Create a dictionary
dormant={}
for data in dormantData:
    # Convert to list
    info=data.split(",")

    # Build the dictionary for the data
    tmpDict={}
    for idx,key in enumerate(header):
        if info[idx].isnumeric():
            tmpDict[key]=int(info[idx].strip())
        else:
            tmpDict[key]=info[idx].strip()

    # We want company name as the key which is index 1
    dormant[info[1]]=tmpDict

# Dump the data to JSON file
jsonData = json.dumps(dormant)
# Open JSON file
jsonFile = open("dormantcos.json","w")
jsonFile.write(jsonData)
jsonFile.close()