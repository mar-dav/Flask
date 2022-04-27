import sqlite3 as sql

con = sql.connect("database.db")
c = con.cursor()

c.execute("SHOW TABLES")


con.close()