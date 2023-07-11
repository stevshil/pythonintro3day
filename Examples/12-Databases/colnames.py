#!/usr/bin/env python

import pymssql

try:
    conn = pymssql.connect(server='192.168.10.103', user='sa', password='P@SSw0rd123', database='steve', timeout=5)
except Exception as e:
    print("Unable to connect to the database")
    print("Issue is",e)
    exit(1)

cursor = conn.cursor()
cursor.execute('SELECT * FROM users;')

colNameList = []
for i in range(len(cursor.description)):
    desc = cursor.description[i]
    colNameList.append(desc[0])

print(colNameList) # List containing column names