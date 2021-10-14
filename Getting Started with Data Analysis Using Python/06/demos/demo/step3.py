import csv
from datetime import datetime
from dateutil.parser import parse
import operator
shares = {"goog":10, "f":1000}
marketDates = set()
myDict = {}
for x in shares.keys():
    stockSymbol = x
    fileName = stockSymbol + ".csv"
    f = open(fileName, "r")
    reader = csv.reader(f)
    next(reader, None)  # skip the headers
    #Date,Open,High,Low,Close,Volume
    for data in reader:
        marketDates.add(parse(data[0]))
        myDict[(stockSymbol, parse(data[0]))] = (float(data[1]),float(data[4]))
diff = {}
for date in marketDates:
    for stk in shares.keys():
        if date in diff:
            diff[date] = diff[date] + (myDict[(stk,date)][1]-myDict[(stk,date)][0]) * shares[stk]
        else:
            diff[date] = (myDict[(stk,date)][1]-myDict[(stk,date)][0]) * shares[stk]
sorted_diff = sorted(diff.items(), key=operator.itemgetter(1))
for x in sorted_diff:
    print x[0],x[1]



