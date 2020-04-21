import sqlite3

conn = conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('''CREATE TABLE ac03 (id int primary key, nome text not null, email)''')

c.execute("INSERT INTO ac03 ('1', '', '')")

conn.commit()
conn.close()
          
