with open('breedflip.in','r') as fin:
    fin = fin.read().split('\n')
    numcows = int(fin[0])
    model = fin[1]
    given = fin[2]
    #print(model)
    #print(given)
changelis = []
for i in range(numcows):
    if model[i] == given[i]:
        changelis.append('yes')
    else:
        changelis.append('no')
#print(changelis)
changenum = 0
ret = 0
for i in changelis:
    if i == 'no':
        ret = 1
    else:
        changenum += ret
        ret = 0
with open('breedflip.out','w') as fout:
    fout.write(str(changenum))