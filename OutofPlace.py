with open('outofplace.in','r') as fin:
    fin = fin.read().split('\n')
    numcows = int(fin[0])
    cowslist = []
    for i in range(numcows):
        fin[i+1] = int(fin[i+1])
        cowslist.append(fin[i+1])
    original = cowslist[:]
    original.sort()
    print(original)
ret = 0
for i in range(numcows):
    if original[i] != cowslist[i]:
        ret += 1

with open('outofplace.out','w') as fout:
    fout.write(str(ret-1))