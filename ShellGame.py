with open('shell.in','r') as fin:
    fin = fin.read().split('\n')
    numofgame = int(fin[0])
    newlists = []
    for i in range(numofgame):
        fin[i+1] = list(map(int,fin[i+1].split(' ')))
        newlists.append(fin[i+1])
print(newlists)
def swap(lis1,current):
    #print(lis1)
    lis = lis1[:]
    lis[0]-=1
    lis[1]-=1
    cop = current[:]

    current[lis[0]] = current[lis[1]]
    current[lis[1]] = cop[lis[0]]
    return current
print('\n')
addlist = []
startlist = [[1,0,0],[0,1,0],[0,0,1]]
start = [1,0,0]
for q in startlist:
    start = q
    add = 0
    for i in newlists:
         start = (swap(i,start))
         #print(start)
         if start[i[2]-1] == 1:
             add += 1
    addlist.append(add)
with open('shell.out','w') as fout:
    if len(addlist) >=1:
        fout.write(str(max(addlist)))
    else:
        fout.write('0')