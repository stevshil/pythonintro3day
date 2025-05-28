# import pymssql
import pyodbc

try:
    # conn = pymssql.connect(server='192.168.10.103', user='sa', password='P@SSw0rd123', database='steve', timeout=5)
    conn = pyodbc.connect(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=localhost\\SQLExpress;DATABASE=steve;UID=sa;PWD=secret;", timeout=5)
    print("Connected to the database")
except Exception as e:
    print("Unable to connect to the database")
    print("Issue is",e)
    exit(1)

# cursor = conn.cursor(as_dict=True)
cursor = conn.cursor()
cursor.execute('SELECT * FROM users;')
for row in cursor:
    # print("ID=%d, First Name=%s" % (row['id'], row['firstname']))
    print("ID=%d, First Name=%s" % (row.id, row.firstname))

cursor.close()
conn.close()
