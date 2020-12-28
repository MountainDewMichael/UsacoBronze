"""
ID: ml89491
LANG: PYTHON3
TASK: ride
"""
with open('ride.in','r') as fin:
    fin = fin.read().split("\n")
    comet = list(fin[0])
    ship = list(fin[1])
def ret(li):
    return(ord(li)-64)
li = list(map(ret,comet))
le = list(map(ret,ship))
def addlist(l):
    mult=1
    for i in range(len(l)):
        mult*=l[i]
    return mult%47
tot = (le,li)
total = list(map(addlist,tot))


with open('ride.out','w') as fout:
    if total[0] == total[1]:
        fout.write('GO\n')
    else:
        fout.write('STAY\n')