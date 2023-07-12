#!/usr/bin/env python

import requests
import pymssql
import random
from datetime import datetime, timedelta
# The final script
# Dormant account information

# Test data to test service
# Good Data
# jFile=open("example.csv","r")
# Bad data
# jFile=open("example-err.csv","r")
# data="".join(jFile.readlines())
# jFile.close()

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
headerCSV = ("companyNumber","companyName","balYear","balMonth","balDay","shareholdersFund","cash","netAssets","stmntYear","stmntMonth","stmntDay","approvYear","approvMonth","approvDay","presContact","presCoName","presAddress")
dataCSV = [ random.randint(100000000,999999999), row["Company"], row["Year"], month, day, round(float(row['shareholdersFund']),2), round(float(row['cash']),2), round(float(row['netAssets']),2), row['Year'], datetime.now().month, datetime.now().day, approvaldate.year, approvaldate.month, approvaldate.day, "Steve Shilling", "Training For Today", "This Road - This Town - That County - Some Postcode"]
# Failed data
# dataCSV = [ random.randint(100000000,999999999), row["Company"], row["Year"], month, day, round(float(row['shareholdersFund']),2), round(float(row['cash']),2), round(float(row['netAssets']),2), row['Year'], datetime.now().month, datetime.now().day, approvaldate.year, approvaldate.month, approvaldate.day, "Steve Shilling", "This Road - This Town - That County - Some Postcode"]
dataCSV = map(str,dataCSV)
data=",".join(headerCSV)
moredata=",".join(dataCSV)
data=data+"\n"+moredata

webreq = requests.post("http://localhost:8080/accounts/submission/csv", json=data)

if webreq.status_code == 200:
    myhols = webreq.json()  
    print(myhols)  
else:
    print("We were unable to complete the request with "+repr(webreq.status_code))

cursor.close()
conn.close()