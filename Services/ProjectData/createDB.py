#!/usr/bin/env python

import re

# Create Database schema for OECD accounts

datacsv=open("OECDStats-Belgium.csv")
sqlFile=open("OECD.sql","w")
datacsv.readline()
# Remove header
allData=datacsv.readlines()
datacsv.close()

# Grab first column to get field names
cols={}
countries={}
mainData={}
for line in allData:
    data=line.split(",")
    # Remove the number, dot and space before the column name
    heading=re.sub(r'^"[0-9]+\.(\S+\.)? ','',data[1])
    heading=re.sub(r'"$','',heading)
    cols[heading]=1
    country=re.sub(r'"','',data[5])
    countries[re.sub(r'"','',data[5])]=1
    if country not in list(mainData.keys()):
        mainData[country]={}
    if data[6] not in list(mainData[country].keys()):
        mainData[country][data[6]]={}

    # mainData[country][data[6]].append({heading: data[8]})
    mainData[country][data[6]][heading]=data[8]

# print(list(cols.keys()))
# print(list(country.keys()))
print(mainData['Belgium'])
# Create database and table
sqlFile.write("DROP DATABASE IF EXISTS Account\nGO\n")
sqlFile.write("CREATE DATABASE Accounts\nGO\nuse Accounts\nGO\n")
sqlFile.write("DROP TABLE IF EXISTS Countries\nGO\n")
tableStr="""CREATE TABLE Countries (
            Country varchar(20),
            Year int"""
for col in list(cols.keys()):
    tableStr=tableStr+""",
            ["""+col+"] numeric(20,5)"
tableStr=tableStr+"""
)
GO
"""
sqlFile.write(tableStr)

# Create SQL Statement for Insert
for data in mainData:
    # print(data) # Is the key of the country
    for year in mainData[data]:
        # print(mainData[data][year]) # Each years data for country
        sqlstrFields="INSERT INTO Countries ([Country],[Year]"
        sqlstrValues="VALUES('"+ data +"',"+ year.replace('"','')
        for item in mainData[data][year]:
            sqlstrFields=sqlstrFields+",["+item+"]"
            sqlstrValues=sqlstrValues+","+mainData[data][year][item]
        sqlstrFields=sqlstrFields+")"
        sqlstrValues=sqlstrValues+")"
        # print(sqlstrFields+" "+sqlstrValues)
        sqlFile.write(sqlstrFields+" "+sqlstrValues+";\n")

sqlFile.close()