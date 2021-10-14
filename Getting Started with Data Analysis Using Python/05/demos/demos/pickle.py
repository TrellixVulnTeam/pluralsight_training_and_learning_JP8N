import sqlite3
import cPickle
 
# create list of tuples
def getStocks():
    stockList = []
    conn = sqlite3.connect("c://python27/devcode/mycode/db/stocks.db")
    c = conn.cursor()
    c.execute('Select date, close, high, low, open, volume, symbol from stockprices')
    for row in c.fetchall():
        stockTuple = (row[0],row[1],row[2],row[3],row[4],row[5],row[6])
        stockList.append(stockTuple)
    return stockList

# initial list
stockList=[]
stockList = getStocks()
print len(stockList)

# write pickle
# r = read; w = write; rb = read binary; wb = write binary
my_file = open("stockPickle.dat","wb")
# protocol version 0 (ascii) ,1 (binary), or 2 (binary)
cPickle.dump(stockList,my_file,2)
my_file.close()




