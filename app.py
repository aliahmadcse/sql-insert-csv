import pyodbc
import csv


conn = pyodbc.connect(
    "Driver={ODBC Driver 13 for SQL Server};"
    "Server=DESKTOP-8EVNU8B\SQLEXPRESS;"
    "Database=codeacademy;"
    "Trusted_Connection=yes;"
)


def read(conn):
    print("read")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies")
    for row in cursor:
        print(row)


def write(conn):
    cursor = conn.cursor()
    with open("movies.csv", "r") as file:
        reader = csv.reader(file)
        firstLine = True
        for row in reader:
            if firstLine:
                firstLine = False
                continue
            sql = f"""INSERT INTO movies (id, name, genre, year, imdb_rating) VALUES (
                {int(row[0])}, '{row[1]}', '{row[2]}', {0 if row[3]=='' else int(row[3])},{0 if row[4]=='' else float(row[4])}
                );"""
            print(sql)
            cursor.execute(sql)
        conn.commit()


write(conn)
read(conn)

conn.close()
