with open('square.in','r') as fin:
    fin = fin.read().split('\n')
    fin[0] = fin[0].split(' ')
    fin[0] = list(map(int,fin[0]))
    ur1 = fin[0][0:2]
    ll1 = fin[0][2:]

    fin[1] = fin[1].split(' ')
    fin[1] = list(map(int, fin[1]))
    ur2 = fin[1][0:2]
    ll2 = fin[1][2:]
print(ur1,ll1)
print(ur2,ll2)
list =[]
x = [ur1[0],ll1[0],ur2[0],ll2[0]]
y = [ur1[1],ll1[1],ur2[1],ll2[1]]
print(x)
print(y)
smallest = abs((min(x) - max(x)))
big = abs((min(y) - max(y)))
print(smallest)
print(big)
with open('square.out','w') as fout:
    if smallest >= big:
        fout.write(str(smallest ** 2))
    else:
        fout.write(str(big**2))
