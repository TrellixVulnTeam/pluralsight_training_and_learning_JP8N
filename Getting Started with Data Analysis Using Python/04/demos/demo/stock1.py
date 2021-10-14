import urllib2
 
url = "http://chartapi.finance.yahoo.com/instrument/1.0/F/chartdata;type=quote;range=1y/csv"
sourceCode = urllib2.urlopen(url).read()
splitSource = sourceCode.split('\n')
for eachLine in splitSource:
    splitLine = eachLine.split(',')
    if len(splitLine) == 6 and len(splitLine[0])==8:
        print splitLine
 
