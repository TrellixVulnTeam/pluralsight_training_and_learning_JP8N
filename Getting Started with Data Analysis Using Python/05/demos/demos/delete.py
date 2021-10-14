import sqlite3
from os import path

# basic python database code
# (for linux) ROOT = path.dirname(path.realpath(__file__))
# (for linux) conn = sqlite3.connect(ROOT + "/sample.db")

conn = sqlite3.connect("c://python27/devcode/mycode/db/sample.db")
c = conn.cursor()
x = 'john@mail.com',
c.execute('Delete from users where email=?',x)
conn.commit()
conn.close()
print c.rowcount

