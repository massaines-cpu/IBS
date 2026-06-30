import sqlite3

conn = sqlite3.connect("ibs.db")

with open("init.sql", "r") as f:
    conn.executescript(f.read())

conn.close()

print("ok")