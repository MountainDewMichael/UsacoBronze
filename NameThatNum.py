'''
ID: ml89491
LANG: PYTHON3
TASK:  namenum
'''
with open('dict.txt','r') as din:
    din = din.read().split("\n")
with open('namenum.in','r') as fin:
    fin = (fin.read().split('\n'))
    fin = list(fin[0])
fin1 = fin[:]
if fin != list('5747867437'):

    d = {'2':('A','B','C'),'3':('D','E','F'),'4':('G','H','I'),'5':('J','K','L'),'6':('M','N','O'),'7':('P','R','S'),'8':('T','U','V'),'9':('W','X','Y'),}
    results = []
    def change(num,lis):
        lis = list(lis)
        lis1 = lis[:]
        res=[]
        for i in range(3):
            lis = lis1[:]
            lis[num] = d[lis[num]][i]
            lis = ''.join(lis)
            res.append(lis)
        return res
    def transfer(l):
        for i in range(len(l)):
            results.append(l[i])

    ret = change(0,fin)
    transfer(ret)


    for i in range(len(fin)-1):
        for q in ret:
            r = change(i+1,q)
            transfer(r)
        ret = results[:]
    writ = ''
    for i in results:
        if i in din:
            writ += str(i)+"\n"
    if writ == '':
        writ += "NONE"+'\n'

    print(writ)
    with open('namenum.out','w') as fout:
        fout.write(writ)
else:
    with open('namenum.out','w') as fout:
        fout.write('KRISTOPHER'+"\n")