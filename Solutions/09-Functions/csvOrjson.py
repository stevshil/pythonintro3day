#!/usr/bin/env python
import sys
import json

def checkCSVorJSON(theFile):
    # Check if the file is CSV
    firstLine=theFile.readline()
    if "," in firstLine:
        theFile.seek(0)
        return "csv"
    
    theFile.seek(0)
    for line in theFile:
        if "{" in line:
            theFile.seek(0)
            return "json"
    
    return False

def loadDataCSV(dataFile):
    strHeader=dataFile.readline()
    headers=strHeader.split(",")
    for line in dataFile:
        info=line.split(",")
        tmpDict={}
        for idx,header in enumerate(headers):
            tmpDict[header]=info[idx]
        dataStore[info[1]]=tmpDict
    
    print(dataStore)
    return dataStore

def loadDataJSON(dataFile):
    dataStore = json.load(dataFile)
    print(dataStore)
    return dataStore


dataFile=open(sys.argv[1],"r")

fileType=checkCSVorJSON(dataFile)
dataStore={}
if fileType == "csv":
    # Do CSV stuff
    print("CSV")
    dataStore=loadDataCSV(dataFile)

elif fileType == "json":
    # Do JSON stuff
    print("JSON")
    dataStore=loadDataJSON(dataFile)
else:
    # Report invalid format
    print("Unknown file type")

dataFile.close()