#!/usr/bin/env python

# Connection string for DB connection
import pymssql

# Original
# conn = pymssql.connect(server='192.168.10.111', user='sa', password='P@SSw0rd123', database='steve')

try:
    conn = pymssql.connect(server='192.168.10.103', user='sa', password='P@SSw0rd123', database='steve', timeout=5)
except Exception as e:
    print("Unable to connect to the database")
    print("Issue is",e)
    exit(1)

# Now we are connected let's get some data
cursor = conn.cursor()
# Tell the server what we want to execute as SQL
cursor.execute('SELECT * FROM users;')
# Data stored in row for our script
row = cursor.fetchone()
print("ID,Firstname,Lastname,Age,Phone,Postcode") # CSV format, could change print to write to file

# Loop through all rows returned from our query
while row:
    # Loop through each column of the row
    for item in row:
        print(str(item) + ",", end="") # CSV format, could change print to write to file
    print()
    row = cursor.fetchone()
cursor.close()

# Inserting data
cursor = conn.cursor()
# Tell the server what we want to execute as SQL
try:
    # Skip if 4 already exists
    cursor.execute("INSERT INTO users VALUES(4,'John','Smith',53,'555-2222','NE3 4RP')")
except:
    pass
# Store the data
cursor.execute("SELECT max(id) FROM users")
row=cursor.fetchone()
print("Last ID insert: "+repr(row[0]))
conn.commit() # Ensures data is written to the database, without this it rolls back the change.
cursor.close()

# Updating data
cursor = conn.cursor()
# Tell the server what we want to execute as SQL
newage=55
id=4
cursor.execute("UPDATE users SET age="+str(newage)+" WHERE id="+str(id))
# Show update
cursor.execute("SELECT * FROM users WHERE id="+str(id))
row=cursor.fetchone()
print(repr(row))
conn.commit()
cursor.close()


# Like files we should close our connection to the database when finished
conn.close()