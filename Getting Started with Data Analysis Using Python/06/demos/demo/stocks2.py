import csv
from datetime import datetime
from dateutil.parser import parse
import operator

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
diff = {}
for date in sorted(marketDates):
    for stk in shares.keys():
        if date in diff:
            closeLessOpen = (myDict[(stk,date)][1]-myDict[(stk,date)][0])
            diff[date] = diff[date] + closeLessOpen * shares[stk]
        else:
            diff[date] = (myDict[(stk,date)][1]-myDict[(stk,date)][0])*shares[stk]
sorted_diff=sorted(diff.items(),key=operator.itemgetter(1))
for x in sorted_diff:
    print x[0], x[1]




