import sqlite3
import hashlib
conn = sqlite3.connect("userdata.db")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS userdata (
        id INTEGER PRIMARY KEY,
        username VARCHAR(225) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
""")
username1, password1 = "ManMan", hashlib.sha256("ManManDIDit".encode()).hexdigest()
username2, password2 = "MotherChild", hashlib.sha256("JohnCarter".encode()).hexdigest()
username3, password3 = "LucySmith", hashlib.sha256("Johndoe".encode()).hexdigest()
username4, password4 = "PerryTim", hashlib.sha256("TheU".encode()).hexdigest()
username5, password5 = "ZombieCraft", hashlib.sha256("Minecraftlover".encode()).hexdigest()

cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username5, password5))

conn.commit()
