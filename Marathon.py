with open('marathon.in','r') as fin:
  fin = fin.read().split('\n')
  firstline = int(fin[0])
  cords = []
  for i in range(firstline):
    fin[i+1] = fin[i+1].split(' ')
    print(fin[i+1])
    fin[i+1] = list(map(int,fin[i+1]))
    cords.append((fin[i+1]))
print(cords)
def dist(point1,point2):
    return(abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]))

tot_dist = 0
for i in range(firstline-1):
    tot_dist+= dist(cords[i],cords[i+1])
print(tot_dist)
save = 0
for i in range(firstline-2):
    test_save = dist(cords[i],cords[i+1])+dist(cords[i+1],cords[i+2]) - dist(cords[i],cords[i+2])
    save = max(test_save, save)
print(save)
with open('marathon.out','w') as fin:
    fin.write(str(tot_dist-save)+'\n')