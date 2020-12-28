with open('diamond.in','r') as fin:
    fin = fin.read().split('\n')
    fin[0] = list(map(int,fin[0].split(' ')))
    numdiamonds, distance = int(fin[0][0]),int(fin[0][1])+1
    mick = 0
    for i in range(numdiamonds):
        fin[i+1] = int(fin[i+1])
        mick = max(mick,fin[i+1])
    cop = mick
    diamondlist= [0,]*mick
    for i in range(numdiamonds):
        diamondlist[fin[i+1]-1] += 1
    #print(diamondlist)
#mick = 0
hahahah = 0
for i in range(mick-(distance-1)):
    #print(i)
    sub = 0
    if diamondlist[i] != 0:
        for q in range(distance):
            sub+=(diamondlist[i+q])
        hahahah = max(hahahah,sub)
if distance >= cop:
    hahahah = numdiamonds
with open('diamond.out','w') as fout:
    fout.write(str(hahahah))