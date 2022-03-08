# 33(562(71(9)))
# 1()66(5)
# 2(123)66(5) 6+1+6
import sys
input = sys.stdin.readline

S = '(' + input().strip() + ')'
idx = 0


def recursive() -> int:
    global idx
    idx += 1
    length = 0
    prev = 1
    while idx < len(S) - 1:
        if S[idx] == ')':
            return length
        if S[idx] == '(':
            length += prev * recursive() - 1
        else:
            length += 1
            prev = int(S[idx])
        idx += 1

    return length

print(recursive())