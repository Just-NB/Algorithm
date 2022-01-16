'''
Title   : 1로 만들기 2
Level   : S1
Problem : 정수 X에 사용할 수 있는 연산은 3가지 있다.
          1. X % 3 == 0 일 경우, 3으로 나눈다.
          2. X % 2 == 0 일 경우, 2로 나눈다.
          3. 1을 뺀다.
          정수 N이 주어졌을 때, 위의 연산을 적절히 사용하여 1을 만든다.
          연산을 사용하는 횟수와 최솟값을 출력한다.
Type    : bfs, dp
Idea    : 1. 정수 X에 대해 각 3가지 연산을 queue에 넣고 bfs 순회한다.
          2. bfs순회를 할 경우, 1을 만들 수 있는 최소 횟수를 구할 수 있다.
          3. 각 정수 X에 대해, X가 만들어지기 위해 거쳐온 정수 X`을 dict자료형에 저장한다.
          4. 1을 만들고 난 후, dict[1]부터 시작하여 원래 정수 X를 찾아간다.
'''
from collections import deque

N = int(input())
dp = dict()
bfs = deque()
bfs.append([N, 0])

while len(bfs)!=0:
    num, cnt = bfs.popleft()
    if num == 1:
        print(cnt)
        break
    if num % 3 == 0 and not dp.get(num//3):
        bfs.append([num//3, cnt+1])
        dp[num//3] = num
    if num % 2 == 0 and not dp.get(num//2):
        bfs.append([num//2, cnt+1])
        dp[num//2] = num
    if not dp.get(num-1):
        bfs.append([num-1, cnt+1])
        dp[num-1] = num

ans = [-1]*cnt
idx = 1
for i in range(cnt):
    ans[cnt-i-1] = dp[idx]
    idx = dp[idx]

for a in ans:
    print(a, end=' ')
print(1)