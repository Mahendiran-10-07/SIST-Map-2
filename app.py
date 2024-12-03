import sqlite3
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/api/buildings')
def get_buildings():
    conn = sqlite3.connect('college_map.db')
    c = conn.cursor()
    c.execute("SELECT name, lat, lng FROM Buildings")
    buildings = c.fetchall()
    conn.close()
    print()
    return json.dumps(buildings)

def init_db():
    conn = sqlite3.connect('college_map.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Buildings 
                (id INTEGER PRIMARY KEY, name TEXT, lat REAL, lng REAL)''')
    conn.commit()
    conn.close()

def remove_records():
    conn = sqlite3.connect('college_map.db')
    c = conn.cursor()
    c.execute("DELETE FROM Buildings")
    conn.commit()
    conn.close()
remove_records()

def add_building(name, lat, lng):
    conn = sqlite3.connect('college_map.db')
    c = conn.cursor()
    c.execute("INSERT INTO Buildings (name, lat, lng) VALUES (?, ?, ?)", (name, lat, lng))
    conn.commit()
    conn.close()
add_building("Admin Block", 12.873, 80.222)
add_building("Library", 12.873222759413746, 80.21895802552135)

def display_db():
    conn = sqlite3.connect('college_map.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Buildings")

    rows = c.fetchall()

    print("id | name  | age")
    print("-----------------")
    for row in rows:
        print(row[0], "|", row[1], "|", row[2])
    conn.close()
display_db()

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
