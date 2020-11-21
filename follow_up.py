import sqlite3
import datetime

conn = sqlite3.connect('follow_ups.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS flw_ups (id INTEGER PRIMARY KEY, person TEXT NOT NULL, day TEXT NOT NULL)')

name = input('Name\n')
n = int(input('When?\n'))
day = datetime.datetime.today().toordinal()
day2 = day + n
cursor.execute('INSERT INTO flw_ups(person, day) VALUES(?, ?)', (name, str(day2)))
conn.commit()
