'''
Title   : 입국심사
Level   : S1
Problem : M명의 사람이 한 줄로 서서 입국심사를 기다리고 있다.
          한 번에 한 사람 심사, 비어있는 심사대가 있으면 그곳으로 갈 수 있지만 이동하지 않아도 된다.
          심사하는데 걸리는 시간이 각각 다르다.
          심사를 받는데 걸리는 시간의 최솟값
Type    : 이분탐색
Idea    : 1. 0 ~ 최대시간 을 시작으로 탐색한다.
          2. mid 시간에 각 심사대에서 처리할 수 있는 사람의 수를 센다.
          3. M명보다 많이 심사하면 right 를 mid로 설정한다.
          4. M명보다 적게 심사하면 left를 mid+1로 설정한다.
'''
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
time = [0 for _ in range(N)]
for i in range(N):
    time[i] = int(input())

left, right = 0, max(time)*M
while left < right:
    mid = (left + right) // 2
    complete = 0
    for t in time:
        complete += (mid // t)
    if complete < M:
        left = mid + 1
    else:
        right = mid
print(left)