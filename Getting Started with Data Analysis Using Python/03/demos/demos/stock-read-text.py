
count = 0
with open('mystocks.csv', 'r') as f:
    for line in f:
        print line
        count = count + 1
f.close()
print count
