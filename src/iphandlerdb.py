import sqlite3
import bcrypt

conn = sqlite3.connect("validip.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS whitelist (
        id INTEGER PRIMARY KEY,
        ipaddress TEXT NOT NULL,
        active BOOLEAN NOT NULL
    )
''')

conn.commit()
conn.close()
