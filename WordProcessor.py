"""
ID: ml8949
LANG: PYTHON3
TASK: word
"""
with open('word.in','r') as fin:
    fin = fin.read().split('\n')
    numword,maxword = (fin[0].split())
    numword,maxword = int(numword), int(maxword)
    sentence = fin[1].split(' ')
    print(sentence)
with open('word.out', 'w') as fout:
    charcount = 0
    output = ''
    for word in sentence:
        print(word)
        if len(word) + charcount <= maxword:
            print("yes got throug")
            charcount += len(word)
            if word == sentence[0]:
                output+=word
            else:
                output+= ' '+word

        else:
            fout.write(output + '\n')
            charcount = len(word)
            output =(word)
    fout.write(output+'\n')


