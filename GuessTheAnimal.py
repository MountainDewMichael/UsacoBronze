with open('guess.in','r') as fin:
    fin = fin.read().split('\n')
    numanimals = int(fin[0])
    animalslist = []
    for i in range(numanimals):
        fin[i+1] = fin[i+1].split(' ')
        fin[i+1][1] = int(fin[i+1][1])
        animalslist.append(fin[i+1])
    print(animalslist)
def check(one,two):
    thic= one + two
    copythic = thic[:]
    copythic = list(set(copythic))
    return (len(thic) - len(copythic))
mick = 0
for i in animalslist:
    for q in animalslist[animalslist.index(i):]:
        if i != q:
            #print(i[0],q[0])
            mick = max(mick,(check(i[2:],q[2:])))
mick +=1
with open('guess.out','w') as fout:
    fout.write(str(mick))
