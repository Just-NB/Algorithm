'''
Title   : 철로
Level   : G2
Problem : 집과 사무실을 통근하는 N명의 사람이 있다. 집과 사무실은 수평선 상의 서로 다른점에 위치한다.
          일직선 상의 어떤 두 점을 잇는 철로를 건설하려고 한다. 철로의 길이는 d로 정해져있다.
          집과 사무실의 위치 모두 철로 선분에 포함되는 사람들의 수가 최대가 되도록 철로 선분을 정하고자 한다.
          집과 사무실의 위치가 모두 포함되는 사람들의 최대 수를 구하는 프로그램을 작성한다.
Type    : 우선순위 큐
Idea    : 1. 입력받은 집/ 오피스의 위치중 좀 더 멀리있는 값을 기준으로 오름차순으로 정렬한다.
          2. 편의상 오피스가 집보다 멀리 있다고 가정하고 생각한다.
          3. 철로의 마지막지점을 오피스 위치로 가정하고 모든 사람들의 사무실을 확인한다.
          4. 사람 i의 오피스 위치에 철로의 마지막 지점으로 설정했을 때, 집의 위치가 철로안에 들어간다면 우선순위 큐에 집의 위치를 넣는다.
          5. 사람 i의 오피스 위치에 철로의 마지막 지점으로 설정했을 때, 우선순위 큐 안의 맨 앞의 값(0 ~ i-1 사람의 집의 위치)이 철로의 길이 밖에 있다면 pop한다.
          6. 큐 안에 들어있는 사람의 최대 수를 답으로 출력한다.
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