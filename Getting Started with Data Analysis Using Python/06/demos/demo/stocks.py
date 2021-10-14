import csv
from datetime import datetime
from dateutil.parser import parse

shares = {"goog":10,"f":1000}
marketDates = []
myDict = {}  # key is tuple(symbol, date) value is tuple (open, close)

for x in shares.keys():
    stockSymbol = x
    fileName = stockSymbol + ".csv"
    f = open(fileName, "r")
    reader = csv.reader(f)
    next(reader, None)  # skip the headers
    #Date,Open,High,Low,Close,Volume
    for data in reader:
        if parse(data[0]) not in marketDates:
            marketDates.append(parse(data[0]))
        myDict[(stockSymbol, parse(data[0]))] = (float(data[1]),float(data[4]))
total = {}
for date in sorted(marketDates):
    for stk in shares.keys():
        if date in total:
            total[date] = total[date]+myDict[(stk,date)][1]*shares[stk]
        else:
            total[date] = myDict[(stk,date)][1]*shares[stk]
for date in sorted(marketDates):
    print date, total[date]




