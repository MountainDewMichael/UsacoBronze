    with open('swap.in','r') as fin:
    fin = fin.read().split('\n')
    fin[0] = fin[0].split(' ')
    numcows, numswitch = int(fin[0][0]), int(fin[0][1])
    moves = []
    startlis = []
    for i in range(numcows):
        startlis.append(str(i+1))
    original = startlis
    firstmove = list(map(int,fin[1].split(' ')))
    secondmove = list(map(int,fin[2].split(' ')))
def swap(lis,move):
    ret = lis[move[0]-1:move[1]]
    ret.reverse()
    first = lis[0:move[0]-1]
    second = lis[move[1]:]
    return(first+ret+second)
add = 0
while True:
    add+=1
    startlis = swap(startlis,firstmove)
    #print(startlis)
    startlis =swap(startlis,secondmove)
    if startlis == original:
        ret= (numswitch%add)
        break
for i in range(ret):
    startlis = swap(startlis, firstmove)
    # print(startlis)
    startlis = swap(startlis, secondmove)
#print(startlis)
with open('swap.out','w') as fout:
    for i in (startlis):
        fout.write(str(i)+'\n')
