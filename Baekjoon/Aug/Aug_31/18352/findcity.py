import sys
from collections import deque
input = sys.stdin.readline
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
visit = [False for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
answer= []
bfs = deque()
bfs.append([X,0]) # 시작위치, 깊이
visit[X] = True

while bfs:
    cur,depth = bfs.popleft()
    if depth == K:
        answer.append(cur)
    elif depth < K:
        for i in graph[cur]:
            if visit[i] is False: # 방문한 적 없으면
                visit[i] = True
                bfs.append([i, depth+1])

if len(answer) != 0:
    for a in sorted(answer):
        print(a)
else:
    print(-1)