with open('gymnastics.in','r') as fin:
    fin = fin.read().split('\n')
    fin[0] = fin[0].split(' ')
    numclasses = int(fin[0][0])
    numcows = int(fin[0][1])
    del fin[0]
    for i in range(numclasses):
        fin[i] = fin[i].split(' ')
testlist =[]
biglist = []
for b in range(numclasses):
    first_test = fin[b]
    for i in range (numcows-1):
        for q in range(i+1,numcows):
            testlist.append((first_test[i],first_test[q]))
    biglist.append(testlist)
    testlist = []
print(biglist)
testlist = biglist[0]
del biglist[0]
biggestlist = []
for i in biglist:
    for q in i:
        biggestlist.append(q)
#print(testlist)
#print(biggestlist)


with open('gymnastics.out','w') as fout:
    add = 0
    for i in testlist:
        count_of = biggestlist.count(i)
        if count_of == numclasses-1:
            add += 1
    fout.write(str(add))