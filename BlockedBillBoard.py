with open('billboard.in','r') as fin:
    fin = fin.read().split('\n')
    fin[0] = list(map(int,fin[0].split(' ')))
    board1 = (fin[0][0],fin[0][1]),(fin[0][2],fin[0][3])
    fin[1] = list(map(int, fin[1].split(' ')))
    board2 = (fin[1][0], fin[1][1]), (fin[1][2], fin[1][3])
    fin[2] = list(map(int, fin[2].split(' ')))
    bus = (fin[2][0], fin[2][1]), (fin[2][2], fin[2][3])
    #print(board1)
    #print(board2)
    #print(bus)
boardlis = []
for i in range(board1[0][0],board1[1][0]):
    for q in range(board1[0][1], board1[1][1]):
        boardlis.append((i,q))
for i in range(board2[0][0],board2[1][0]):
    for q in range(board2[0][1], board2[1][1]):
        boardlis.append((i,q))
#print(boardlis)
with open('billboard.out','w') as fout:
    hack = 0
    for i in range(bus[0][0], bus[1][0] ):
        #print(i)
        for q in range(bus[0][1], bus[1][1] ):
            if (i,q) in boardlis:
                hack += 1
    fout.write(str(len(boardlis)-hack))
