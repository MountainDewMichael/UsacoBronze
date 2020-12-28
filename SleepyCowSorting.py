with open('sleepy.in','r') as fin:
    fin = fin.read().split('\n')
    numcows = int(fin[0])
    currentcowplace = list(map(int,fin[1].split(' ')))
    print(currentcowplace)
    achoo = sorted(currentcowplace)
if achoo == currentcowplace:
    ret = 0
else:
    testlist = []
    def less(test,cur):
        for i in test:
            if cur > i:
                return False
        return True
    for i in range(-1,numcows*-1-1,-1):
        #print(currentcowplace[i])
        if i == -1:
            testlist.append(currentcowplace[i])
        else:
            if less(testlist,currentcowplace[i]) == False:
                ret = (currentcowplace.index(currentcowplace[i])+1)
                break
            else:
                testlist.append(currentcowplace[i])
        #print(testlist)
with open('sleepy.out','w') as fout:
    fout.write(str(ret))