with open('cowsignal.in', 'r') as fin:
    fin = fin.read().split('\n')
    #print(fin)
    numsrows, letrows, amp = fin[0].split(' ')
    numsrows, letrows, amp = int(numsrows),int(letrows),int(amp)
    rows = []
    del fin[0]
    for i in range(numsrows):
        rows.append(fin[i])
    #print(rows)
returnlist = []
for i in range(numsrows):
    add = ''
    for b in range(letrows):
        #print(rows[i][b])
        for q in range(amp):
            add += (rows[i][b])
    for meow in range(amp):
        returnlist.append(add)
print(returnlist)
with open('cowsignal.out','w') as fout:
    for i in range(len(returnlist)):
        print(returnlist[i])
        fout.write(returnlist[i]+'\n')