with open ('paint.in','r') as fin:
    fin = fin.read().split('\n')
    fin[0] = fin[0].split(' ')
    fin[1] = fin[1].split(' ')
    if len(fin) > 2:
        del fin[2]
    print(fin)
    if fin[0][0] < fin[1][0]:
        fin1 = fin[0][:]
        fin[0] = fin[1]
        fin[1] = fin1

    print(fin)

lis = []
lis.append(fin[0][0])
lis.append(fin[0][1])
lis.append(fin[1][0])
lis.append(fin[1][1])

lis = list(map(int,lis))
lis.sort()
print(lis)
with open('paint.out','w') as fout:
    ret = (abs(lis[0] - lis[-1]))
    if int(fin[0][1]) < int(fin[1][0]):
        print(int(fin[1][0]) - int(fin[0][1]))
        ret -= (int(fin[1][0]) - int(fin[0][1]))

    fout.write(str(ret))