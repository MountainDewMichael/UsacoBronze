with open('socdist2.in','r') as fin:
    fin =fin.read().split('\n')
    numcow = int(fin[0])
    lis = []
    numinfect = []
    for i in range(numcow):
        fin[i+1] = list(map(int,fin[i+1].split(' ')))
        if fin[i+1][1] == 0:
            numinfect.append(fin[i+1])
        lis.append(fin[i+1])
    lis.sort()
#biglist and non infected list
print(lis)
print(numinfect)
#find r
varr = 10000000000
for i in numinfect:
    ind = lis.index(i)
    if ind < numcow -1 and lis[ind+1][1] != 0:
        varr = min(varr,(abs(i[0] - lis[ind+1][0])))
        print(varr)
    if ind -1 >= 0 and lis[ind-1][1] != 0:
        varr = min(varr,(abs(i[0] - lis[ind -1][0])))
        print(varr)
varr -= 1
print()
#find original
for i in numinfect:
    lis.remove(i)
#remove non infected
print(lis)
tot = 1
for i in range(len(lis)-1):
    print(lis[i])
    if lis[i][0] + varr >= lis[i+1][0]:
        continue
    else:
        tot += 1
#tot +=1
with open('socdist2.out','w') as fout:
    fout.write(str(tot))

