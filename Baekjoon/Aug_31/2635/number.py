import sys
input = sys.stdin.readline

N = int(input())
answer = [N]
for i in range(1,N+1):
    tmp = [N,i]
    while tmp[-2]-tmp[-1] >= 0:
        tmp.append(tmp[-2]-tmp[-1])
    if len(answer) < len(tmp):
        answer = tmp
print(len(answer))
print(*answer)
