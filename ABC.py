import sys
fin = sys.stdin.read().split('\n')
cows = list(map(int,fin[0].split(' ')))
cows.sort()

vara = cows[0]
varb = cows[1]
cows.remove(vara+varb)
#print(cows)
for i in cows[1:]:
    if i+vara in cows:
        cows.remove(i+vara)
for i in cows[2:]:
    if i+vara in cows:
        cows.remove(i+vara)
print(cows[0],cows[1],cows[2])