import sqlite3
from os import path

# basic python database code
# (for linux) ROOT = path.dirname(path.realpath(__file__))
# (for linux) conn = sqlite3.connect(ROOT + "/sample.db")

conn = sqlite3.connect("c://python27/devcode/mycode/db/sample.db")
c = conn.cursor()
x = 'jane@mail.com','Jane','Doe',
c.execute('Insert into users values(?,?,?)',x)
conn.commit()
conn.close()
print c.rowcount
