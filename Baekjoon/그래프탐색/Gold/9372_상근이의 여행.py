import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    visit = [False for _ in range(N + 1)]
    for m in range(M):
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1

    answer = 0
    for start in range(1, N + 1):
        if visit[start]: continue
        bfs = deque()
        bfs.append(start)
        visit[start] = True
        while bfs:
            cur = bfs.popleft()
            for i in range(N + 1):
                if graph[cur][i] == 0: continue
                if visit[i]: continue
                answer += 1
                visit[i] = True
                bfs.append(i)

    print(answer)