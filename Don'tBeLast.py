with open('notlast.in','r') as fin:
    fin = fin.read().split('\n')
    logs = int(fin[0])
    del fin[0]
    listlogs = []
    for i in range(logs):
        fin[i] = fin[i].split(' ')
        fin[i][1] = int(fin[i][1])
        listlogs.append(fin[i])
#print(listlogs)
retlist = [['Bessie',0],['Elsie',0],['Daisy',0],['Gertie',0],['Annabelle',0],['Maggie',0],['Henrietta',0]]
for i in listlogs:
    #print(i[0])
    for b in retlist:
        if b[0] == i[0]:
            b[1]+=i[1]
print(retlist)
with open('notlast.out','w') as fout:
    minlist = []
    for i in retlist:
        minlist.append(i[1])

    tes = sorted(list(set(minlist)))
    tes = (tes[1])
   # print(tes)
    minlist = []
    for q in retlist:
        if q[1] == tes:
            minlist.append(q[0])
    #print(minlist)
    if len(minlist) == 1:
        fout.write(minlist[0]+'\n')
    else:
        fout.write('Tie\n')