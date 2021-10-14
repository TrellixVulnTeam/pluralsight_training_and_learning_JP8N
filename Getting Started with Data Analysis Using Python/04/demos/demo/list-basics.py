
myStocks = []
myStocks = ['QCOM','AAPL','F']
print myStocks
myStocks.append('MSFT')
print myStocks
myStocks.insert(0,'GOOG')
print myStocks
myStocks.pop()
print myStocks
x = sorted(myStocks)
print x
if 'GM' in x:
    print "GM is in stocks"
else:
    print "GM not in stocks"

