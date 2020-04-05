import pyodbc

conn = pyodbc.connect(
    "Driver={ODBC Driver 13 for SQL Server};"
    "Server=DESKTOP-8EVNU8B\SQLEXPRESS;"
    "Database=codeacademy;"
    "Trusted_Connection=yes;"
)

def read(conn):
    print("read")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM friends")
    for row in cursor:
        print(row)


read(conn)

conn.close()
