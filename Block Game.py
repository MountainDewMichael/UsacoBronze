with open('blocks.in','r') as fin:
    fin = fin.read().split('\n')
    numblocks = int(fin[0])
    blocks = []
    for i in range(numblocks):
        blocks.append(fin[i+1].split(' '))
alpha = [0,]*26
def count(string):
    string1list = [0, ] * 26
    string2list = [0,] * 26
    for i in string[0]:
        string1list[(ord(i)-97)] +=1
    for i in string[1]:
        string2list[(ord(i)-97)] +=1
    for i in range(26):
        string1list[i] = max(string1list[i],string2list[i])
    return (string1list)
for i in blocks:
    ack = (count(i))
    for q in range(26):
        alpha[q] += ack[q]
with open('blocks.out','w') as fout:
    for i in alpha:
        fout.write(str(i)+'\n')
