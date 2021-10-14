import urllib2

count = 0
twoPercent = []
for stk in ['AAPL']:
    url = "http://chartapi.finance.yahoo.com/instrument/1.0/" + stk + "/chartdata;type=quote;range=1y/csv"
    sourceCode = urllib2.urlopen(url).read()
    splitSource = sourceCode.split('\n')
    for eachLine in splitSource:
        splitLine = eachLine.split(',')
        if len(splitLine) == 6 and len(splitLine[0])==8:
            #print splitLine[1], splitLine[4]
            cls = float(splitLine[1])
            opn = float(splitLine[4])
            chg = (cls-opn)/opn
            if chg > 0.02:
                print splitLine[0] + str(chg)
            count = count + 1
print count
