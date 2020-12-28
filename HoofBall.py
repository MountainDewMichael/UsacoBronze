with open('hoofball.in','r') as fin:
    fin = fin.read().split('\n')
    numcow = int(fin[0])
    cowlist = list(map(int,fin[1].split(' ')))
    cowlist.sort()
    subcow = []
    first = cowlist[0]
    for i in range(numcow):
       subcow.append(0)
    print(cowlist)

def check(i):
    #nd = cowlist.index(i)
    if i == numcow-1:
        print('adfadfadfadfasdfds')
        return i-1
    elif i == 0:
        print('eadadfadsfasd')
        return 1
    else:
        first = abs(cowlist[i - 1] - cowlist[i])
        second = abs(cowlist[i] - cowlist[i + 1])
    if first <= second:
        return i-1
    else:
        return i+1
for i in range(numcow):
    subcow[check(i)] += 1
print(subcow)
count = 0
for i in range(len(subcow)):
    if subcow[i] == 0:
        count+=1
    if i < check(i) and check(check(i)) == i and subcow[i] == 1 and subcow[check(i)] == 1:
        count += 1
with open('hoofball.out','w') as fout:
    fout.write(str(count))

