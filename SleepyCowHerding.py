with open('herding.in','r') as fin:
    fin =fin.read().split('\n')
    thic = (list(map(int,fin[0].split(' '))))
    print(thic)
def checkConsecutive(l):
    return l[0] == l[1] - 1 and l[1] == l[2] -1
with open('herding.out','w') as fout:
    if (checkConsecutive(thic)) == True:
        fout.write('0'+'\n')
    elif thic[2] == thic[1] + 2 or thic[1] == thic[0] + 2:
       fout.write('1'+'\n')
    else:
        fout.write('2'+'\n')
    ret = max(thic[1]-thic[0], thic[2] - thic[1])-1
    fout.write(str(ret))