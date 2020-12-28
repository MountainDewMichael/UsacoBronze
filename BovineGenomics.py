with open('cownomics.in','r') as fin:
    fin =fin.read().split('\n')
    fin[0] = fin[0].split(' ')
    numcows,genenum = int(fin[0][0]),int(fin[0][1])
    cows = []
    for i in range(numcows*2):
        cows.append(fin[i+1])
    #print(cows)
    nonspot = []
    spot = []
    for q in range(genenum):
        sublistspot =[]
        sublist = []
        for i in cows[numcows:]:
            sublistspot.append(i[q])
        for i in cows[:numcows]:
            sublist.append(i[q])
        nonspot.append(sublistspot)
        spot.append(sublist)
    #print(spot)
    #print(nonspot)
def find(spot,nonspot):
    spot,nonspot = sorted(set(spot)),sorted(set(nonspot))
    for i in spot:
        if i in nonspot:
            return False
    return True
add = 0
for i in range(genenum):
    if find(spot[i],nonspot[i]) == True:
        add+=1
with open('cownomics.out','w') as fout:
    fout.write(str(add))