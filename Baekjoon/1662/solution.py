'''
input : 
33(562(71(9)))
33(32(5)6(71(9)))
output :
19
46
K(Q) -> Q 0자리 이상 str
    -> K 1자리 정수
'''

S = input()
ret = 0
pos = 0

def solution(S) :
    ret = 0
    global pos
    while pos < len(S)-1 :
        cur = S[pos]
        pos += 1
        ret += 1
        if S[pos] == '(' :
            pos += 1
            ret -= 1
            ret = ret + int(cur) * solution(S)
            pos += 1
        elif S[pos] == ')' :
            if ret == 0 : return 1
            if cur != ')' :
                return ret
            return ret-1
    return ret

print(solution(S))