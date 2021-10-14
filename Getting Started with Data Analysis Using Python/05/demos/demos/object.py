import sqlite3
import cPickle

class Stock: pass
 
# create list of objects
def getStocks():
    stockList = []
    conn = sqlite3.connect("c://python27/devcode/mycode/db/stocks.db")
    c = conn.cursor()
    c.execute('Select date, close, high, low, open, volume, symbol from stockprices')
    for row in c.fetchall():
        stockTuple = (row[0],row[1],row[2],row[3],row[4],row[5],row[6])
        stock = Stock()
        stock.date = row[0]
        stock.close = row[1]
        stock.high = row[2]
        stock.low = row[3]
        stock.open = row[4]
        stock.volume = row[5]
        stock.symbol = row[6]
        stockList.append(stock)
    return stockList

# initial list
stockList=[]
stockList = getStocks()
print len(stockList)

for x in stockList:
    print x.close, x.symbol, x.date
    






