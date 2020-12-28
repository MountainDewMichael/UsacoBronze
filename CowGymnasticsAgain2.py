with open('gymnastics.in','r') as fin:
    fin = fin.read().split('\n')
    first = fin[0].split(' ')
    numclasses,numcows = int(first[0]), int(first[1])
    classes = []
    for i in range(numclasses):
        fin[i + 1] = fin[i+1].split(' ')
        classes.append(fin[i+1])
#print(numclasses,numcows)
#print(classes)
order = []
for i in classes:
    smallorder = []
    for q in range(numcows-1):
        for b in range(q+1,numcows):
            smallorder.append((i[q],i[b]))
    order.append(smallorder)
print(order)
firstorder = order[0]
del order[0]
print(firstorder)
thiclist = []
for i in order:
    for q in i:
        thiclist.append(q)
print(thiclist)
with open('gymnastics.out','w') as fout:
    add = 0
    for i in firstorder:
        blah = thiclist.count(i)
        if blah == numclasses-1:
            add += 1
    fout.write(str(add))