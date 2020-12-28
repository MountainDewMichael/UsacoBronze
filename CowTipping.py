with open('cowtip.in','r') as fin:
    fin = fin.read().split('\n')
    N = int(fin[0])
    cowlist = []
    for i in range(N):
        fin[i+1] = list(map(int,list(fin[i+1])))
        cowlist.append(fin[i+1])
    print(cowlist)
def change(inlist,numlist):
    for i in cowlist[:numlist+1]:
        for q in range(inlist+1):
            if i[q] == 1:
                i[q] = 0
            else:
                i[q] = 1
    #print(cowlist)
    #print(cowlist,'cowlist')
def check(curr):
    for i in curr:
        if i == 1:
            return False
    return True
count = 0
for i in range(N-1, -1, -1):
    current = cowlist[i]
    for q in range(N-1,-1,-1):

        if current[q] == 1:
            change(q,i)
            count+=1
        if check(current)==True:
            break
print(cowlist)
with open('cowtip.out','w') as fout:
    fout.write(str(count))