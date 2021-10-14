
watchList = ['MSFT','AAPL','QCOM']
openPos = [('AAPL',100.00,100),('F',8.35,100),('DIS',87.35,100)] #(sym,buy,sh)
closedPos = [('MSFT',25.50,32.65,100),('INTC',35.35,27.89,100)] #(sym,buy,sell,sh)

myStocks = set()
for x in watchList:
    myStocks.add(x)

for x in openPos:
    myStocks.add(x[0])

for x in closedPos:
    myStocks.add(x[0])

print myStocks

x = sorted(myStocks)
print x
