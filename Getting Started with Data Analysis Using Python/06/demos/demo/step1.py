import csv
from datetime import datetime
from dateutil.parser import parse

# Goal: calc value of holdings over time
# Goal: calc & sort daily diff of holdings over time
# https://finance.google.com/finance?q=nasdaq:goog
# https://www.google.com/finance?q=nyse:f

myDict = {}  # key is tuple(symbol, date) value is tuple (open, close)
for x in ["goog","f"]:
    stockSymbol = x
    fileName = stockSymbol + ".csv"
    f = open(fileName, "r")
    reader = csv.reader(f)
    next(reader, None)  # skip the headers
    #Date,Open,High,Low,Close,Volume
    for data in reader:
        myDict[(stockSymbol, parse(data[0]))] = (float(data[1]),float(data[4]))

for x in myDict:
    print x, myDict[x]
print len(myDict)




