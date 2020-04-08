import pyodbc
import csv
import config


conn = pyodbc.connect(
    "Driver={ODBC Driver 13 for SQL Server};"
    "Server=DESKTOP-8EVNU8B\SQLEXPRESS;"
    "Database=magazine_company;"
    "Trusted_Connection=yes;"
)


def read(conn):
    print("read")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {config.table_name}")
    for row in cursor:
        print(row)


def write(conn):
    cursor = conn.cursor()
    with open(config.file_name, "r") as file:
        reader = csv.reader(file)
        firstLine = True
        for row in reader:
            if firstLine:
                firstLine = False
                continue
            sql = f"""INSERT INTO {config.table_name} ( {','.join(config.columns)} ) VALUES (
                '{"','".join(row)}'
            );"""
            print(sql)
            cursor.execute(sql)
        conn.commit()


write(conn)
read(conn)

conn.close()


#  {0 if row[3]=='' else int(row[3])},{0 if row[4]=='' else float(row[4])}
