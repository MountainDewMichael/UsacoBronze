"""
ID: ml89491
LANG: PYTHON3
TASK: friday
"""

with open('friday.in','r') as fin:
    fin = int(fin.read())

num13th = [0]*7
numofdays = [31,28,31,30,31,30,31,31,30,31,30,31]
numofleap = [31,29,31,30,31,30,31,31,30,31,30,31]
def leap(year):
    if (year%100==0 and year%400 ==0) or (year%100!=0 and year% 4==0):
        return True
    return False
day = 0
for i in range(1900,1900+fin):
    if leap(i):
        for m in range(12):

            for d in range(numofleap[m]):

                day+=1
                if day == 7:
                    day = 0
                if d==12:
                    num13th[day]+=1
    else:
        for m in range(12):

            for d in range(numofdays[m]):

                day+=1
                if day == 7:
                    day = 0
                if d==12:
                    num13th[day]+=1
with open('friday.out','w') as fout:
    le = list(map(str,num13th))
    ret = ("")
    ret+=(le[6])+' '
    ret += (le[0]) + ' '
    ret += (le[1]) + ' '
    ret += (le[2]) + ' '
    ret += (le[3]) + ' '
    ret += (le[4]) + ' '
    ret += (le[5]) + '\n'

    fout.write(ret)