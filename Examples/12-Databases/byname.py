import pymssql

try:
    conn = pymssql.connect(server='192.168.10.103', user='sa', password='P@SSw0rd123', database='steve', timeout=5)
except Exception as e:
    print("Unable to connect to the database")
    print("Issue is",e)
    exit(1)

cursor = conn.cursor(as_dict=True)
cursor.execute('SELECT * FROM users;')
for row in cursor:
    print("ID=%d, First Name=%s" % (row['id'], row['firstname']))

cursor.close()
conn.close()
