with open('hps.in','r') as fin:
    fin = fin.read().split('\n')
    numcow = int(fin[0])
    cowlist = []
    for i in range(numcow):
        fin[i+1] = list(map(int,fin[i+1].split(' ')))
        cowlist.append(fin[i+1])
    changelist = ['hoof','scizzors','paper']
    def permutation(lst):
        if len(lst) == 0:
            return []
        if len(lst) == 1:
            return [lst]
        l = []
        for i in range(len(lst)):
            m = lst[i]
            remLst = lst[:i] + lst[i + 1:]
            for p in permutation(remLst):
                l.append([m] + p)
        return l
    changelist = permutation(changelist)
    print(cowlist)
    print(changelist)
def win(one,two):
    if one == two:
        return 0
    if one == 'hoof' and two == 'scizzors':
        return 1
    if one == 'scizzors' and two == 'paper':
        return 1
    if one == 'paper' and two == 'hoof':
        return 1
    return 0
mick = 0
for i in changelist:
    smallmick = 0
    for q in cowlist:
        sub1,sub2 = i[q[0]-1],i[q[1]-1]
        if win(sub1,sub2) == 1:
            smallmick += 1
        #print(win(sub1,sub2))
    mick = max(smallmick,mick)
print(mick)
with open('hps.out','w') as fout:
    fout.write(str(mick))