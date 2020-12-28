with open('gymnastics.in','r') as fin:
    fin = fin.read().split('\n')
    classes,numcows = fin[0].split(' ')
    classes,numcows = int(classes),int(numcows)
    del fin[0]
    for i in range(classes):
        fin[i] = fin[i].split(' ')
        fin[i] = list(map(int,fin[i]))
lis = []
finaltest = []
for b in range(classes):

    for i in range(numcows):

        for q in range(fin[b].index(fin[b][i])+1,numcows):

            lis.append((fin[b][i],fin[b][q]))
    finaltest.append(lis)
    lis = []

def testfunc(val):
    for i in (finaltest):
        #print(i)
        if val not in i:
            return False
    return True
test = finaltest[0]
del finaltest[0]
print(finaltest)
count = 0

for i in test:
    if testfunc(i) == True:
        count+=1

with open('gymnastics.out','w') as fout:
    fout.write(str(count))


