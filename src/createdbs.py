import sqlite3
import bcrypt

conn = sqlite3.connect("UserCredentials.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS credentials (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        active TEXT NOT NULL
    )
''')

conn.commit()
conn.close()
