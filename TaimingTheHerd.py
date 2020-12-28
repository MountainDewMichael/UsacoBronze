with open('taming.in','r') as fin:
    fin = fin.read().split('\n')
    numcow = int(fin[0])
    cowlist = list(map(int,fin[1].split(' ')))
    lis = []
    for i in range(numcow):
        lis.append(0)
    cowlist[0] = 0
    lis[0] = 1
    print(cowlist)
curr = 0
for i in range(len(cowlist)):
    if cowlist[i] != -1:
        lis[i-cowlist[i]] = 1
print(lis)
min = lis.count(1)
for i in range (len(cowlist)):
    if cowlist[i] >0:
        for q in range(cowlist[i],0,-1):
            cowlist[i-q] = 0
max = min
for i in range(numcow):
    if lis[i] == 0 and cowlist[i] == -1:
        max += 1
with open('taming.out','w') as fout:
    fout.write(str(min)+' '+str(max))
