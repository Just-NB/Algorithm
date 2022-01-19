'''
Title   : 가장 긴 증가하는 부분 수열 5
Level   : P5
Problem : 수열 A가 주어졌을 떄, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성한다.
Type    : 다이나믹 프로그래밍
Idea    : 1. 이분탐색을 이용하여 LIS를 구한다.
          2. LIS를 구하는 과정에서 A[i]의 각 값이 LIS의 몇번째 위치에 있을지 기록한다(loc).
          3. loc을 역순으로 순회하며, 현재 크기에 해당하는 값들을 저장한다.
'''
import bisect

N = int(input())
A = list(map(int, input().split()))
DP = [] # idx : 길이, val : 해당 길이에 해당하는 가장 작은 값.
loc = [-1 for _ in range(N)]  # 해당 idx의 값이 몇 번째 순서에 위치하나?

for i, a in enumerate(A):
    idx = bisect.bisect_left(DP, a)
    loc[i] = idx
    if idx == len(DP):
        DP.append(a)
    else:
        DP[idx] = a

length = len(DP)
ans = [0] * length
lis_idx = length

for i in range(len(loc) - 1, -1, -1):
    if loc[i] == lis_idx - 1:
        lis_idx -= 1
        ans[lis_idx] = A[i]

print(len(ans))
for a in ans:
    print(a,end=' ')


