import csv
import pygal
from pygal.style import CleanStyle

stockPrices = {}  #key is symbol, value is list of closing prices
stockSymbols = ['goog','amzn']
for symbol in stockSymbols:
    fileName = symbol + ".csv"
    f = open(fileName, "r")
    reader = csv.reader(f)
    reader.next()
    dataset = []
    dates = []
    count = 0
    #Date,Open,High,Low,Close,Volume
    for data in reader:
        count = count + 1
        if count%10 == 0:
            dates.append(data[0])
            dataset.append(float(data[4]))
    stockPrices[symbol] = list(reversed(dataset))
    
line_chart = pygal.Line(style=CleanStyle)
line_chart.title = "Stock Prices"
line_chart.x_labels = dates  #List
for symbol in stockSymbols:
    line_chart.add(symbol, stockPrices[symbol])
# Save the svg to a file
line_chart.render_to_file('stock-chart.svg')
