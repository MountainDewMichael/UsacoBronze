with open('circlecross.in','r')as fin:
    fin = fin.read().split('\n')
    string = list(fin[0])
print(string)
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def check(lis):
    cop = lis[:]
    cop = list(set(cop))
    original = len(lis)
    sub = (original-len(cop))*2
    return original-sub
mick = 0
for i in alphabet:
    print()
    cop = string[:]
    cop.remove(i)
    first = string.index(i)
    second = cop.index(i)+1
    lis = string[first+1:second]
    mick += (check(lis))
with open('circlecross.out','w') as fout:
    fout.write(str(int(mick/2)))