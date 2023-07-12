#!/usr/bin/env python

import pymssql
import pandas as pd

# Connect to the database
try:
    conn = pymssql.connect(server='192.168.10.103', user='sa', password='P@SSw0rd123', database='NorthWind')
except Exception as e:
    print("Unable to connect to the database")
    print("Issue is",e)
    exit(1)

sqlQ = pd.read_sql_query('''
                            SELECT Orders.OrderId, CustomerId, UnitPrice, Quantity, Discount, Freight, 
                            CONVERT(VARCHAR,ShippedDate,105) AS "ShippedDate", 
                            ((UnitPrice*IIF(Discount=0,1,Discount))*Quantity) AS "Order Total"
                            FROM [Order Details] 
                            LEFT JOIN Orders ON [Order Details].OrderID = Orders.OrderID
                            WHERE ShippedDate is not null;
                         ''', conn)

df = pd.DataFrame(sqlQ)

# Create the Order Totals grouped
ds=df.groupby(["OrderId","CustomerId"])["Order Total"].sum()
df2=pd.DataFrame(columns=["Order Total"], data=ds)

# Grab the Freight price for each order
ds=df.groupby(["OrderId","CustomerId"])["Freight"].unique()
df3=pd.DataFrame(columns=["Freight"], data=ds)
# Convert list to number
df3=df3.astype({"Freight": "float64"})

# Join Freight and totals
df4=df2.join(df3, how='right')

# Add the Freight to the order total
df4["Order Total"]=df4["Order Total"]+df4["Freight"]

# Drop the Freight column as we no longer need it
df4.drop("Freight",inplace=True,axis=1)
# Reuse a previous name to clean up
df2=df4.copy()

# Remove the unused DFs from memory
df3=None
df4=None

# Grab the Shipped Dates
ds=df.groupby(["OrderId","CustomerId"])["ShippedDate"].unique()
df3=pd.DataFrame(columns=["ShippedDate"], data=ds)

# Convert list to string as there is only 1 date
df3["ShippedDate"]=[''.join(map(str, l)) for l in df3['ShippedDate']]

# Join the data so we have what we need
df=df2.join(df3, how='right')
print(df)

# Remove all other DF and DS
ds=None
df2=None
df3=None

# Output to CSV
df.to_csv("orderTotals.csv")