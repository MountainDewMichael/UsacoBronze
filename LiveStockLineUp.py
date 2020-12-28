from itertools import permutations
with open('lineup.in','r') as fin:
    fin = fin.read().split('\n')
    numcommand = int(fin[0])
    commands = []
    cows = ['Beatrice', 'Belinda', 'Bella', 'Bessie', 'Betsy', 'Blue', 'Buttercup', 'Sue']
    for i in range(numcommand):
        fin[i+1] = fin[i+1].split(' ')
        commands.append((fin[i+1][0],fin[i+1][-1]))
    print(commands)
def check(must,lis):
    for q in must:
        if lis.index(q[0]) != lis.index(q[1]) + 1 and lis.index(q[0]) + 1 != lis.index(q[1]):
            return False
    return True
cowlist = [1,2,3,4,5,6,7,8]
cowlist = permutations(cows)
ret = ''
for i in cowlist:
    if (check(commands,i))==True:
        ret = i
        break
print(ret)
with open('lineup.out','w') as fout:
    fout.write(ret[0]+'\n')
    fout.write(ret[1] + '\n')
    fout.write(ret[2] + '\n')
    fout.write(ret[3] + '\n')
    fout.write(ret[4] + '\n')
    fout.write(ret[5] + '\n')
    fout.write(ret[6] + '\n')
    fout.write(ret[7])
    #fout.write(ret[8])