with open('triangles.in','r') as fin:
    fin = fin.read().split('\n')
    sides = int(fin[0])
    lispoints = []
    for i in range(sides):
        fin[i+1] = list(map(int,fin[i+1].split(' ')))
        lispoints.append(fin[i+1])
    #print(lispoints)
def findarea(i,q,b):
    height = abs(i[1]-q[1])
    width = abs(q[0]-b[0])
    return (int(height*width/2))
max = 0
for i in lispoints:
    for q in lispoints:
        for b in lispoints:
            if i != q and i != b and q != b:
                #print(i,q,b)
                if i[0] == q[0] and q[1] == b[1]:
                    if (findarea(i,q,b)) > max:
                        max = (findarea(i,q,b))
print(max)
with open('triangles.out','w') as fout:
    fout.write(str(max*2))