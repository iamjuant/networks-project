from flask import Flask, render_template
import sqlite3
#from ..dbmethods import * 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/connect')
def connect_to_database():
    try:
        connection = sqlite3.connect('UserCredentials.db')
        return 'Successfully connected to DB!'
    except sqlite3.Error as error:
        return f'ERROR: Failed to connect to DB: {error}'

@app.route('/view_table')
def view_table():
    try:
        connection = sqlite3.connect('UserCredentials.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM credentials;")
        rows = cursor.fetchall()
        return '<br>'.join(map(str, rows))
    except sqlite3.Error as error:
        return f'Failed to view table: {error}'

if __name__ == '__main__':
    app.run(debug=True)