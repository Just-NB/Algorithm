import re

C = int(input())
for _ in range(C) :
    print('???')
    W = input()
    str = ''
    for w in W :
        if w == '?' :
            str += '.'
        elif w == '*' :
            str += '.*'
        else :
            str += w
    N = int(input())
    files = []
    for __ in range(N) :
        files.append(input())
    p = re.compile(str)
    answer = set()
    for file in files :
        if ''.join(p.findall(file)) == file :
            answer.add(''.join(p.findall(file)))
    answer = sorted(answer)
    for a in answer :
        if a != '' :
            print(a)




'''
input :
2
he?p
3
help
heap
helpp
*p*
3
help
papa
hello

output :
heap
help
help
papa 
'''