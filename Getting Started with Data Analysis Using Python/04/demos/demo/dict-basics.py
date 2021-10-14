myDict = {}
print myDict
myDict['ABC'] = "Company ABC"
myDict['XYZ'] = "Corporation XYZ"
myDict['ZZZ'] = "ZZZ Inc"
print myDict
print myDict['ABC']
for x in myDict.keys():
    print x, myDict[x]
for x in myDict:
    print x
myDict['ZZZ'] = "Updated Company"
print myDict['ZZZ']
if 'ZZZ' in myDict:
    print "True"
print 
print "Corporation XYZ" in myDict.values()

