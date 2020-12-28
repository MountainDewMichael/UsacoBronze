with open('lostcow.in','r') as fin:
    fin = fin.read().split('\n')
    fin[0] = list(map(int,fin[0].split(' ')))
    john,bess = fin[0][0],fin[0][1]
    print(john,bess)
def negswap(negpos):
    if negpos == -1:
        return 1
    return -1
ret = 0
if bess == john:
    ret = 0
else:
    mult = 1
    negpos = 1
    while True:
        change = (mult*negpos)
        if (negpos == 1 and john < bess and john + mult >=bess) or (negpos == -1 and john > bess and john + (mult*-1) <= bess):
            ret += abs(bess-john)
            break
        else:
            ret += (mult*2)
        #change
        mult *= 2
        negpos = negswap(negpos)
        #change
with open('lostcow.out','w') as fout:
    fout.write(str(ret))