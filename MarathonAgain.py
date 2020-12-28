with open('marathon.in','r') as fin:
    fin = fin.read().split('\n')
    points = []
    for i in range(int(fin[0])):
        fin[i+1] = list(map(int,fin[i + 1].split(' ')))
        points.append(fin[i+1])
    print(points)
def distance(lis1,lis2):
    return abs(lis1[0]-lis2[0]) + abs(lis1[1]-lis2[1])
tot_dist = 0
for i in range(int(fin[0])-1):
    tot_dist+= distance(points[i],points[i+1])
print(tot_dist)
max1 = 0
for i in range(int(fin[0])-2):
    test = (distance(points[i],points[i+1])+distance(points[i+1],points[i+2])-distance(points[i],points[i+2]))
    max1 = max(test,max1)
print(max1)
with open('marathon.out','w') as fout:
    fout.write(str(tot_dist-max1)+'\n')