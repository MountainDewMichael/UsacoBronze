with open('promote.in','r') as fin:
    fin =fin.read().split('\n')
    bronze = list(map(int,fin[0].split(' ')))
    silver = list(map(int,fin[1].split(' ')))
    gold = list(map(int,fin[2].split(' ')))
    platinum = list(map(int,fin[3].split(' ')))

print(bronze,silver,gold,platinum)
movefromgold = platinum[1]- platinum[0]
movefromsilver = platinum[1] + gold[1] - (platinum[0] + gold[0])
movefrombronze = platinum[1] + gold[1] + silver[1] - (platinum[0] + gold[0]+silver[0])
print(movefromgold,movefromsilver,movefrombronze)
with open('promote.out','w') as fout:
    fout.write(str(movefrombronze)+'\n')
    fout.write(str(movefromsilver) + '\n')
    fout.write(str(movefromgold) + '\n')