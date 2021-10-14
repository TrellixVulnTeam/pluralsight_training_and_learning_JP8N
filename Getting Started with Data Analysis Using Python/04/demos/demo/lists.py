

stocks = ['AAPL','F','MSFT','QCOM','AMZN']
print stocks

stocks.append('XOM')
print stocks

stocks.insert(1,'IBM')
print stocks

stocks.pop(0)
print stocks

sortedStocks = sorted(stocks)
print sortedStocks

print len(stocks)


