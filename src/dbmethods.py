import sqlite3
import bcrypt


def insert_user(username,password,active):
    conn = sqlite3.connect("UserCredentials.db")
    cursor = conn.cursor()
    cursor.execute(
    'insert into credentials (username,password,active) values (?,?,?)',(username,password,active))
    conn.commit()
    conn.close()
insert_user('iamjuant', 'password2','active')