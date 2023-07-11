#!/usr/bin/env python

import pymssql

# Connect to the database
try:
    conn = pymssql.connect(server='192.168.10.103', user='sa', password='P@SSw0rd123', database='NorthWind')
except Exception as e:
    print("Unable to connect to the database")
    print("Issue is",e)
    exit(1)

csvData=[]

cursor = conn.cursor(as_dict=True)
cursor.execute('''
SELECT Orders.OrderId, CustomerId, UnitPrice, Quantity, Discount, Freight, 
CONVERT(VARCHAR,ShippedDate,105) AS "ShippedDate", 
((UnitPrice*IIF(Discount=0,1,Discount))*Quantity) AS "Order Total"
FROM [Order Details] 
LEFT JOIN Orders ON [Order Details].OrderID = Orders.OrderID
WHERE ShippedDate is not null;
''')

row = cursor.fetchone()
tmpDict={}
while row:
    if row['OrderId'] in tmpDict:
        tmpDict[row['OrderId']]={'OrderId': row['OrderId'], 'CustomerId': row['CustomerId'], 'ShippedDate': row['ShippedDate'], 'Freight': row['Freight'], 'Order Total': round(row['Order Total']+tmpDict[row['OrderId']]['Order Total'],2)}
    else:
        tmpDict[row['OrderId']]={'OrderId': row['OrderId'], 'CustomerId': row['CustomerId'], 'ShippedDate': row['ShippedDate'], 'Freight': row['Freight'], 'Order Total': round(row['Order Total'],2)}
    row=cursor.fetchone()

cursor.close()
conn.close()

for data in tmpDict:
    tmpDict[data]['Order Total']=round(float(tmpDict[data]['Order Total'])+float(tmpDict[data]['Freight']),2)
    del tmpDict[data]['Freight']


firstID=list(tmpDict.keys())[0]
header=",".join(list(tmpDict[firstID].keys()))
orderTotals=open("orderTotals.csv","w")
orderTotals.write(header+"\n")
for data in tmpDict:
    tmpline=list(tmpDict[data].values())
    tmpline=",".join(str(e) for e in tmpline)
    orderTotals.write(tmpline+"\n")
orderTotals.close()