#!/usr/bin/env python

import pymssql
import json

# Key names
keys=("ID","Firstname","Lastname","Age","Phone","Postcode")
# The dictionary for the final JSON export
etlData=[]

try:
    conn = pymssql.connect(server='192.168.10.103', user='sa', password='P@SSw0rd123', database='steve', timeout=5)
except Exception as e:
    print("Unable to connect to the database")
    print("Issue is",e)
    exit(1)

cursor = conn.cursor()
# Tell the server what we want to execute as SQL
cursor.execute('SELECT * FROM users;')
# Data stored in row for our script
row = cursor.fetchone()
counter=0 # Just in case we get stuck
while row:
    # Check for bad postcode NE3 4RP
    if "NE3 4RP" in row:
        counter=counter+1
        if counter > 2:
            break # Because we're stuck in an infinite loop as we remove the last item
        else:
            continue
    tmpDict={}
    for idx,item in enumerate(row):
        tmpDict[keys[idx]]=item
    etlData.append(tmpDict)
    row = cursor.fetchone()
    counter=0
cursor.close()
conn.close()

# Open JSON file
jOut=open("dbetl.json","w")
jOut.write(json.dumps(etlData))
jOut.close()