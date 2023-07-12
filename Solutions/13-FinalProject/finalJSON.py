#!/usr/bin/env python

import requests
import pymssql
import random
import json
from datetime import datetime, timedelta

# The final script
# Dormant account information

# Testing data of service
# Good Data
# jFile=open("example.json","r")
# Bad data
# jFile=open("example-err.json","r")
# jFile=open("example-err2.json","r")
# data="".join(jFile.readlines())
# jFile.close()
# Connect to the database

try:
    conn = pymssql.connect(server='192.168.10.103', user='sa', password='P@SSw0rd123', database='Accounts')
except Exception as e:
    print("Unable to connect to the database")
    print("Issue is",e)
    exit(1)

cursor = conn.cursor(as_dict=True)
cursor.execute('''
SELECT Country As Company, Year, [Shares and participations] AS "shareholdersFund", 
[Cash and balance with Central bank] AS "cash", 
[Other assets]+[Risk-weighted assets]+[Other liabilities]+[Liabilities to non-residents] AS "netAssets"
FROM Countries
WHERE Country = 'Austria' and Year=2008;
''')

row = cursor.fetchone()
               
# Generate Dictionary for JSON
month=random.randint(1,12)
day=random.randint(1,28)
approvaldate=datetime.now()+timedelta(days=-90)
dictData={
    "companyDetails": {
      "number": random.randint(100000000,999999999),
      "name": row["Company"]
    },
    "balanceSheetDate": {
      "year": row["Year"],
      "month": month,
      "day": day
    },
    "accounts": {
      "shareholdersFund": round(float(row['shareholdersFund']),2),
      "cash": round(float(row['cash']),2),
      "netAssets": round(float(row['netAssets']),2)
    },
    "statement": {
      "yearEnding": {
        "year": row['Year'],
        "month": datetime.now().month,
        "day": datetime.now().day
      }
    },
    "approval": {
      "year": approvaldate.year,
      "month": approvaldate.month,
      "day": approvaldate.day
    },
    "presenter": {
      "contact": "Steve Shilling",
      "companyName": "Training For Today",
      "address": "This Road, This Town, That County, Some Postcode"
    }
}
print(dictData)
# data=json.dumps(dictData, default=str)
data=json.dumps(dictData)

webreq = requests.post("http://localhost:8080/accounts/submission/json", json=data)

if webreq.status_code == 200:
    myhols = webreq.json()
    print(myhols)  
else:
    print("We were unable to complete the request with "+repr(webreq.status_code))

cursor.close()
conn.close()