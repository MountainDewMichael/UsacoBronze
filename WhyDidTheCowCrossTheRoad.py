with open('maxcross.in','r') as fin:
    fin = fin.read().split('\n')
    fin[0] = fin[0].split(' ')

    numwalks, need, numbroken = int(fin[0][0]),int(fin[0][1]), int(fin[0][2])
    walkslist = [0,]*numwalks
    print(walkslist)
    for i in range(numbroken):
        walkslist[int(fin[i+1])-1] = 1
    print(walkslist)
answer = sum(walkslist[0:need])
temp = answer
for i in range(1,numwalks-need + 1):
    temp = temp - walkslist[i-1] + walkslist[i+need-1]
    answer = min(answer,temp)
with open('maxcross.out','w') as fout:
    fout.write(str(answer))