import sqlite3
from os import path

# basic python database code
# (for linux) ROOT = path.dirname(path.realpath(__file__))
# (for linux) conn = sqlite3.connect(ROOT + "/sample.db")

conn = sqlite3.connect("c://python27/devcode/mycode/db/sample.db")
c = conn.cursor()
employees = [('jill@mail.com','Jill','AppleTree'),
             ('frank@mail.com','Frank','AppleTree'),
             ('desi@mail.com','Desi','AppleTree')]
c.executemany('Insert into users values(?,?,?)',employees)
conn.commit()
conn.close()
print c.rowcount
