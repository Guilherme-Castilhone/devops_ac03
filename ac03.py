import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE ac03 (id int primary key, nome text not null, email)''')

conn.commit()
conn.close()
          
