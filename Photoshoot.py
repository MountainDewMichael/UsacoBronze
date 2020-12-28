with open('photo.in','r') as fin:
    fin = fin.read().split('\n')
    fin[1] = fin[1].split(' ')
    numcows = int(fin[0])
    inputnums = list(map(int,fin[1]))
    print(inputnums)

def dup(lis):
    test = len(lis)
    test2 = len(list(set(lis)))
    if test - test2 > 0:
        return True
    return False
def pos(lis):
    for i in lis:
        if i <=0:
            return False
    return True
with open('photo.out','w') as fout:
    for i in range(1,inputnums[0]):
        testlist = []
        #i is the change num
        changenum = i
        for q in range(numcows-1):
            testlist.append(changenum)
            changenum = inputnums[q] - changenum
        testlist.append(changenum)
        print(testlist)
        if dup(testlist) == False and pos(testlist) == True:
            #print(testlist)
            for b in testlist:
                if testlist.index(b) == len(testlist)-1:
                    #print('adfad')

                    fout.write(str(b))
                else:
                    fout.write(str(b)+' ')

