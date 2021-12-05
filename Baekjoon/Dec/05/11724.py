'''
Title   : 연결 요소의 개수
Level   : S2
Problem : 방향 없는 그래프가 주어졌을 때, 연결 요소의 개수를 구하는 프로그램을 작성한다.
Type    : bfs
Idea    : 1. 인덱스를 노드의 번호, 값을 인접 노드로 하는 리스트를 만든다.
          2. visit 리스트를 노드의 갯수만큼 만든다.
          3. 노드를 bfs로 순회한다.
          4. bfs 순회를 시작한 횟수를 출력한다.
'''
from collections import deque

N, M = map(int, input().split())
nodes = [[] for _ in range(N)]
for m in range(M):
    u, v = map(int, input().split())
    nodes[u-1].append(v-1)
    nodes[v-1].append(u-1)

visit = [False for _ in range(N)]
answer = 0
for i in range(N):
    if visit[i] is False:
        answer += 1
        bfs = deque()
        bfs.append(i)
        while len(bfs) != 0:
            node = bfs.popleft()
            for n in nodes[node]:
                if visit[n] is False:
                    bfs.append(n)
                    visit[n] = True

print(answer)