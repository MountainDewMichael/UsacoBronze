import sys
fin = sys.stdin.read().split('\n')
N = int(fin[0])
flowers = list(map(int,fin[1].split(' ')))
from itertools import combinations
#print(flowers)
oddlist = []
def Average(lst):
    return sum(lst) / len(lst)
total = 0
#print(flowers)
def check(tup,ave):
    for i in tup:
        if i == ave:
            return True
    return False
for i in range(1,N+1):
    for q in range(N-(i-1)):
        current = (flowers[q:q + i])
        ave = Average(current)
        #print(current)
        #print(ave,current)
        if check(current,ave) == True:
            total += 1

print(total)