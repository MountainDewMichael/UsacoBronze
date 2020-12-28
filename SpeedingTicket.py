with open('speeding.in','r') as fin:
    fin = fin.read().split('\n')
    N,M = (fin[0].split(' '))
    N,M = int(N),int(M)
    del fin[0]
    if len(fin) > N+M:
        del fin[-1]
    for i in range(N+M):
        fin[i] = fin[i].split(' ')
        fin[i][0],fin[i][1] = int(fin[i][0]),int(fin[i][1])
    road = fin[:N]
    bessie = fin[N:]

roadlis,bessielis = [],[]
for i in road:
    for q in range(i[0]):
        roadlis.append(i[1])
for i in bessie:
    for q in range(i[0]):
        bessielis.append(i[1])
print(roadlis)
print(bessielis)
count = 0
for i in range(100):
    if bessielis[i] > roadlis[i] and bessielis[i]-roadlis[i] > count :
        count = bessielis[i]-roadlis[i]
#print(count)
with open('speeding.out','w') as fout:
    fout.write(str(count))