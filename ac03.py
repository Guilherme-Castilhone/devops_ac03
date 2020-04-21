import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE ac03 (id int primary key, nome text not null, email)''')

c.execute("INSERT INTO ac03 ('1', '', '')")

conn.commit()
conn.close()
          
