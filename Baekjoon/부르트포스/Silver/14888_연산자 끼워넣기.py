import sys
input = sys.stdin.readline

length = int(input())
N = list(map(int, input().split()))
operator = list(map(int, input().split())) # [+, -, *, /]

def calc(op, pre, cur):
    if op == 0:
        return pre + cur
    if op == 1:
        return pre - cur
    if op == 2:
        return pre * cur
    if op == 3:
        if pre < 0 or cur < 0:
            return -(abs(pre) // abs(cur))
        return pre // cur

def backtracking(idx : int, num : int) -> int:
    # idx : 수열 N에서 현재 위치
    # num : 현재까지 누적된 결과값
    if idx == len(N):
        return [num, num]
    min_val = sys.maxsize
    max_val = -1000000001

    for i in range(4):
        if operator[i] == 0:
            continue
        operator[i] -= 1
        a, b = backtracking(idx + 1, calc(i, num, N[idx]))
        max_val = max(a, max_val)
        min_val = min(b, min_val)
        operator[i] += 1

    return [max_val, min_val]

answer = backtracking(1, N[0])
for a in answer:
    print(a)
