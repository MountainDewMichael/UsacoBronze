with open('lifeguards.in','r') as fin:
    fin = fin.read().split('\n')
    numguards= int(fin[0])
    times = []
    timeslist = []
    maxlist = 0
    for i in range(numguards):
        fin[i+1] = list(map(int,fin[i+1].split(' ')))
        times.append(fin[i+1])
        maxlist = max(maxlist,fin[i+1][0], fin[i+1][1])
    for i in range(maxlist):
        timeslist.append(0)
original = times[:]
originallist = timeslist[:]
mick = 0
for i in range(numguards):
    del times[i]
    for b in times:
        for q in range(b[0]-1,b[1]-1):
            timeslist[q] = 1
    mick = max(mick,(timeslist.count(1)))
    timeslist = originallist[:]
    times = original[:]
#print(mick)
with open('lifeguards.out','w') as fout:
    fout.write(str(mick))