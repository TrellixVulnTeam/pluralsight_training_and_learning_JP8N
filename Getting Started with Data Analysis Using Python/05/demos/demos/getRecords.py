import sqlite3
from os import path

# basic python database code
# (for linux) ROOT = path.dirname(path.realpath(__file__))
# (for linux) conn = sqlite3.connect(ROOT + "/sample.db")

conn = sqlite3.connect("c://python27/devcode/mycode/db/sample.db")
c = conn.cursor()
c.execute('Select email, last, first from users')
for row in c.fetchall():
    print row[0]
