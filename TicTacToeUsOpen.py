with open('tttt.in','r') as fin:
    fin = fin.read().split('\n')
    line1 = list(fin[0])
    line2 = list(fin[1])
    line3 = list(fin[2])
    print(line1,line2,line3)
    checklist = [line1, line2, line3, [line1[0],line2[0],line3[0]], [line1[1],line2[1],line3[1]],
                 [line1[2],line2[2],line3[2]], [line1[0],line2[1],line3[2]], [line1[2],line2[1],line3[0]]]
    print(checklist)
singlelist = []
doublelist = []
for i in checklist:
    if len(set(i)) == len(i)-2:
        singlelist.append(i[0])
    elif len(set(i)) == len(i)-1:
        doublelist.append(sorted(list(set(i))))
print(singlelist)
print(doublelist)
single = []
for i in singlelist:
    if i not in single:
        single.append(i)
double = []
for i in doublelist:
    if i not in double:
        double.append(i)
with open('tttt.out','w') as fout:
    fout.write(str(len(single))+'\n')
    fout.write(str(len(double))+'\n')