with open('cowqueue.in','r') as fin:
    fin = fin.read().split('\n')
    numcow = int(fin[0])
    cowlist  = []
    for i in range(numcow):
        fin[i+1] = list(map(int,fin[i+1].split(' ')))
        cowlist.append(fin[i+1])
    cowlist.sort()
    print(cowlist)
turncount = 0
for i in range(numcow):
    if i == 0:
        turncount += cowlist[i][0] + cowlist[i][1]

    elif turncount <= cowlist[i][0]:
        turncount = cowlist[i][0]+cowlist[i][1]
    else:
        turncount += cowlist[i][1]
with open('cowqueue.out','w') as fout:
    fout.write(str(turncount))