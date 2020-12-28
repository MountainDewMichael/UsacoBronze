with open('whereami.in','r') as fin:
    fin =fin.read().split('\n')
    num = int(fin[0])
    string = fin[1]
#print(string)
original = len(string)
thiclist = []
for q in range(original-1):
    biglist = []
    for i in range(1,len(string)):
        changestring =string[0:i]
        #print(changesing)
        changestring2 = string[i:]
        #print(changestring2)
        biglist.append((changestring,changestring2))
    thiclist.append(biglist)
    string = string[1:]
test = thiclist[0]
print(thiclist)
del thiclist[0]
def inorno(index):
    for q in thiclist:
        if len(q) > index + 1:
            if q[index][0] in q[index][1]:
                return False
    return True
ret = 0
for i in test:
    if i[0] not in i[1]:
        ind = test.index(i)
        if inorno(ind) == True:
            ret = str(ind+1)
            print(ret)
            break
with open('whereami.out','w') as fout:
    fout.write(ret)
#print(thiclist)


