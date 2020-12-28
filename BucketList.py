with open('blist.in','r') as fin:
    fin = fin.read().split('\n')
    numcows = int(fin[0])
    listofcows = []
    endtime = []
    for i in range(numcows):
        fin[i+1] = list(map(int,fin[i+1].split(' ')))
        listofcows.append(fin[i+1])
        endtime.append(fin[i+1][1])
    endtime.sort()
    max = endtime[-1]
    print(max)
    listofbucks = []
    for i in range(max):
        listofbucks.append(0)
for i in listofcows:
    reqbuck = i[2]
    for q in range(i[0],i[1]+1):
        listofbucks[q-1] += reqbuck
print(listofbucks)
listofbucks.sort()
with open('blist.out','w') as fout:
    fout.write(str(listofbucks[-1]))
