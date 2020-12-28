with open('cow.in','r') as fin:
    fin = fin.read().split('\n')
    numlets = int(fin[0])
    letslist = list(fin[1])
    print(letslist)
olist = []
totc = 0
toto = 0
for i in range(numlets):
    if letslist[i] == 'C':
        totc += 1
    if letslist[i] == 'O':
        toto += totc
    olist.append(toto)
total = 0
for i in range(numlets):
    if letslist[i] == 'W':
        total += olist[i]
print(total)
with open('cow.out','w') as fout:
    fout.write(str(total))

