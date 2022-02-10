import sys

input = sys.stdin.readline
N = int(input())
stack = []
for n in range(N):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
ans = 0
for s in stack:
    ans += s
print(ans)