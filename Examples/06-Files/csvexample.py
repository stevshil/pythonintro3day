#!/usr/bin/env python

countryData = open("country_full.csv")

# Grab the header information
header=countryData.readline()
print(header)

# Split the header into a list to use in creating list of dictionary objects
header=header.split(",")
print(header)

countryInfo={}
for countries in countryData:
    dataList=countries.split(",")
    tmpDict={}
    for idx,element in enumerate(header):
        tmpDict[element.strip()]=dataList[idx].strip()
    
    countryInfo[dataList[0]]=tmpDict

print(countryInfo["United Kingdom of Great Britain and Northern Ireland"])

countryData.close()