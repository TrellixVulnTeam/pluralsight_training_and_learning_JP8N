import csv
import pygal
from pygal.style import CleanStyle

#download goog.csv, amzn.csv from google finance
stockPrices = {}  #key is symbol, value is list of closing prices
stockSymbols = ["goog","amzn"]
for symbol in stockSymbols:
    fileName = symbol + ".csv"
    f = open(fileName, "r")
    reader = csv.reader(f)
    reader.next()
    dates = []
    dataset = []
    count = 0
    #Date,Open,High,Low,Close,Volume
    for x in reader:
        count = count + 1
        if count%10==0:
            dates.append(x[0])
            dataset.append(float(x[4]))
    stockPrices[symbol]=list(reversed(dataset))
    
    
line_chart = pygal.Line(style=CleanStyle)
line_chart.title = "Stock Prices"
line_chart.x_labels = dates                       #List of dates (string)
for symbol in stockSymbols:
    line_chart.add(symbol, stockPrices[symbol])   #List of closing prices (float)
# Save the svg to a file
line_chart.render_to_file('stock-chart.svg')
