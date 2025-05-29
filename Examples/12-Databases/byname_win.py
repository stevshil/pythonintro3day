import pyodbc

try:
    conn = pyodbc.connect(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=localhost\\SQLExpress;DATABASE=steve;UID=sa;PWD=P@SSw0rd123;", timeout=5)
    print("Connected to the database")
except Exception as e:
    print("Unable to connect to the database")
    print("Issue is",e)
    exit(1)

cursor = conn.cursor()
cursor.execute('SELECT * FROM users;')
for row in cursor:
    print("ID=%d, First Name=%s" % (row.id, row.firstname))

cursor.close()
conn.close()
