'''
Title   : 가장 긴 증가하는 부분 수열 5
Level   : G3
Problem :
Type    :
Idea    : 1.
'''
import sys
import heapq
input = sys.stdin.readline

N = int(input())
pos = [[0, 0] for _ in range(N)]
for n in range(N):
    x, y = map(int, input().split())
    pos[n] = [min(x, y), max(x, y)]  # 작은 값이 왼쪽에 오게 입력
d = int(input())
pos.sort(key=lambda x: x[1])  # 오른쪽(좀더 큰 값)을 기준으로 오름차순 정렬

hq = []
ans = 0
for p in pos:
    left, right = p
    if abs(right - left) <= d:  # 집과 오피스의 거리가 d보다 작으면 체크한다.
        while hq:
            top = hq[0]
            if top >= (right - d):
                break
            # 기존의 집,오피스중 가장 left가 멀리 있는 값이 철도의 밖에 있을 경우
            heapq.heappop(hq)  # 값을 하나 뺀다.
        heapq.heappush(hq, left)
        ans = max(len(hq), ans)

print(ans)