import sqlite3
con = sqlite3.connect('db.sqlite3')
c = con.cursor()
c.execute('SELECT * FROM auth_user')
data = c.fetchall()
for row in data:
    row = str(row)
    print(row.replace(',',' | '))