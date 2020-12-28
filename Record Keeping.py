with open('records.in','r') as fin:
    fin = fin.read().split('\n')
    numgroup = int(fin[0])
    grouplist = []
    special = []
    for i in range (numgroup):
        fin[i+1] = fin[i+1].split(' ')
        fin[i+1] = sorted(fin[i+1])
        if fin[i+1] not in special:
            special.append(fin[i+1])
        grouplist.append(fin[i+1])
print(special)
print(grouplist)
mick = 0
for i in special:
    mick = max(mick,(grouplist.count(i)))
with open('records.out','w') as fout:
    fout.write(str(mick))