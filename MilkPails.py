with open('pails.in','r') as fin:
    x , y , m = fin.read().split(' ')
    x,y,m = int(x),int(y),int(m)
max = int((m-m%x)/x)
print(max)
addlist = []
for i in range(max):
    add = ((x)*(i+1))
    addlist.append(add)
print(addlist)
for i in range(len(addlist)):
    while True:

        if addlist[i] + y <= m:
            addlist[i] += y
        else:
            break

with open('pails.out','w') as fout:
    addlist.sort()
    print(addlist[-1],file=fout)
