import sys
fin = sys.stdin.read().split('\n')
numcow = int(fin[0])
cowliste = []
cowlistn = []
original = []
for i in range(numcow):
    fin[i+1] = fin[i+1].split(' ')
    fin[i+1][1],fin[i+1][2] = int(fin[i+1][1]),int(fin[i+1][2])
    if fin[i+1][0] == 'E':
        cowliste.append(fin[i+1])
    else:
        cowlistn.append(fin[i+1])
    original.append(fin[i+1])

def find(i,q):
    ival = q[1]-i[1]
    qval = i[2] - q[2]
    if ival == qval:
        pass
    elif ival > qval:
        i.append(ival)
    else:
        q.append(qval)
    return (i,q)
def check(i,q):
    ival = q[1]-i[1]
    qval = i[2] - q[2]
    if ival == qval:
        pass
    #qwins
    elif ival > qval:
        if len(q[3:]) > 0:
            if min(q[3:]) < qval:
                i.remove(ival)
    #i wins
    elif qval > ival:
        if len(i[3:]) > 0:
            if min(i[3:]) < ival:
                q.remove(qval)
    return (i,q)
for i in cowliste:
    for q in cowlistn:
        if i[1] <=  q[1] and i[2] >= q[2]:
            #print(i,q)
            (find(i,q))
for i in cowliste:
    for q in cowlistn:
        if i[1] <=  q[1] and i[2] >= q[2]:
            check(i,q)
for i in original:
    if len(i[3:]) == 0:
        print('Infinity')
    else:
        print(min(i[3:]))