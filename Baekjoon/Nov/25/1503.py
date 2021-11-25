'''
Title   : 세 수 고르기
Level   : S3
Problem : M개의 자연수로 이루어진 집합 S와 자연수 N
          S에 속하지 않는 자연수 x,y,z를 골라 |N-xyz|의 최솟값을 구한다.
Type    : 완전탐색
Idea    : 1. N의 최대범위는 1000이므로 확인할 x,y,z의 범위는 1001까지 하면된다.
          1-1. x,y,z는 1000을 넘겨도 상관없으나, 1001 이상으로 확인할 필요는 없다.
          1-2. x*y*1002 이상 될 경우 그 값보다 |N-xyz|이 작을 경우가 없다.
'''
import math

N, M = map(int, input().split())
S = list(map(int, input().split()))
e = [False] * 1002#안 되는 수 : 1 ~ 1000
for s in S:
    e[s] = True

ans = math.inf
for x in range(1, 1001):
    if e[x] is True:
        continue
    for y in range(x, 1001):
        if e[y] is True:
            continue
        for z in range(y, 1002):
            if e[z] is True:
                continue
            ans = min(ans, abs(N-x*y*z))
print(ans)
