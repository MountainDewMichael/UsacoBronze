with open('mixmilk.in','r') as fin:
    milks = []
    max = []
    inbucket = []
    fin = fin.read().split('\n')
    for i in range(3):
        fin[i] = (fin[i].split(' '))
        fin[i][0],fin[i][1] = int(fin[i][0]),int(fin[i][1])
        milks.append(fin[i])
        max.append(fin[i][0])
        inbucket.append(fin[i][1])
print(inbucket)
print(max)
#first
if inbucket[0]+inbucket[1] <= max[1]:
    inbucket[1] += inbucket[0]
    inbucket[0] = 0
else:

    inbucket[0] -= max[1] - inbucket[1]
    inbucket[1] = max[1]
print(inbucket)
#secodn
if inbucket[1]+inbucket[2] <= max[2]:
    inbucket[2] += inbucket[1]
    inbucket[1] = 0
else:

    inbucket[1] -= max[2] - inbucket[2]
    inbucket[2] = max[2]
print(inbucket)
#third
if inbucket[2]+inbucket[0] <= max[0]:
    inbucket[0] += inbucket[2]
    inbucket[2] = 0
else:

    inbucket[2] -= max[0] - inbucket[0]
    inbucket[0] = max[0]

print(inbucket)
#first again
if inbucket[0]+inbucket[1] <= max[1]:
    inbucket[1] += inbucket[0]
    inbucket[0] = 0
else:

    inbucket[0] -= max[1] - inbucket[1]
    inbucket[1] = max[1]
print(inbucket)

#print(inbucket)
print('\n')

with open('mixmilk.out','w') as fout:
   for i in range(3):
      fout.write(str(inbucket[i])+'\n')

