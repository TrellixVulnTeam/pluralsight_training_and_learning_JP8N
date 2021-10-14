import cPickle

# r = read; w = write; rb = read binary; wb = write binary
# r/w is for ascii (protocol 0); rb/wb is for binary (protocol 2)
my_file = open("stockPickle.dat", "rb")
myPickleList = cPickle.load(my_file)
for x in myPickleList:
    print x[0],x[1],x[6]

 
 

    
