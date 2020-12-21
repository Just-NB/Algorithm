'''
input 
4
FFFMMM
MMMFFF
FFFFF
FFFFFFFFFF
FFFFM
FFFFFMMMMF
MFMFMFFFMMMFMF
MMFFFFFMFFFMFFFFFFMFFFMFFFFMFMMFFFFFFF
output
1
6
2
2
'''
'''
책에는 분할 정복 예시(카라츠바 곱)으로 되어있지만
bit연산으로 하는 방법이 생각나서 풀이.
'''

#F = 0, M = 1
def genTobin(lst) :
    lst = ['0' if l == 'F' else '1' for l in lst ]
    return ''.join(lst)

def solution(members, fans) :
    ret = 0
    M = len(members)
    N = len(fans)
    bmembers = int(members,2)
    bfans = int(fans,2)
    tmp = bmembers & bfans
    for _ in range(N-M+1) :
        tmp = bmembers & bfans
        if tmp == 0 :
            ret += 1
        bmembers = bmembers << 1
    return ret

C = int(input())
for _ in range(C) :
    members = genTobin(input())
    fans = genTobin(input())
    print(solution(members,fans))