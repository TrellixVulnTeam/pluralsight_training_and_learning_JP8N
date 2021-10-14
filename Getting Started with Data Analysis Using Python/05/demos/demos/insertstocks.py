import urllib2
import sqlite3

myList = []
for s in ['F', 'MSFT']:
    url = "http://chartapi.finance.yahoo.com/instrument/1.0/" + s
    url = url + "/chartdata;type=quote;range=1y/csv"
    sourceCode = urllib2.urlopen(url).read()
    splitSource = sourceCode.split('\n')
    for eachLine in splitSource:
        spl = eachLine.split(',')
        if len(spl) == 6 and len(spl[0])==8:
            tup = (spl[0],spl[1],spl[2],spl[3],spl[4],spl[5],s)
            myList.append(tup)

conn = sqlite3.connect("c://python27/devcode/mycode/db/stocks.db")
c = conn.cursor()
c.executemany('Insert into stockprices values(?,?,?,?,?,?,?)',myList)
conn.commit()
conn.close()
print c.rowcount
 
