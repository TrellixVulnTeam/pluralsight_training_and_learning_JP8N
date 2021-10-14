import cPickle

class Stock: pass

# r = read; w = write; rb = read binary; wb = write binary
# r/w is for ascii (protocol 0); rb/wb is for binary (protocol 2)
my_file = open("stockObjects.dat", "rb")
myPickleList = cPickle.load(my_file)
for x in myPickleList:
    stk = Stock()
    stk = x
    print stk.close, stk.volume, stk.date, stk.symbol

 
 

    
