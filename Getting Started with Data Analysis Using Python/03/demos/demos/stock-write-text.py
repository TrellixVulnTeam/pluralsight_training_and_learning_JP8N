import urllib2

count = 0
with open('mystocks.csv', 'w') as f:
    for stk in ['AAPL','F']:
        url = "http://chartapi.finance.yahoo.com/instrument/1.0/" + stk + "/chartdata;type=quote;range=1y/csv"
        sourceCode = urllib2.urlopen(url).read()
        splitSource = sourceCode.split('\n')
        for eachLine in splitSource:
            splitLine = eachLine.split(',')
            if len(splitLine) == 6 and len(splitLine[0])==8:
                print splitLine
                f.write(stk + "," + eachLine + "\n")
                count = count + 1
f.close() 
print count
