import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, input().strip())))

bfs = deque()
delta = [(-1,0), (1,0), (0,-1), (0,1)] # 상 하 좌 우

bfs.append([0,0,1,K]) # [위치, cost, 벽 부수기 잔량]
visit = [[[False]*(K+1) for _ in range(M)] for __ in range(N)]
visit[0][0] = [True]*(K+1)
flag = False
while bfs:
    r, c, cost, skill = bfs.popleft()
    if r == N-1 and c == M-1:
        print(cost)
        flag = True
        break
    for dr, dc in delta:
        nr, nc = r+dr, c+dc
        if 0 <= nr < N and 0 <= nc < M :
            if maze[nr][nc] == 1 and skill != 0 and visit[nr][nc][skill-1] is False:
                visit[nr][nc][skill-1] = True
                bfs.append([nr, nc, cost+1, skill-1])
            if maze[nr][nc] == 0 and visit[nr][nc][skill] is False:
                visit[nr][nc][skill] = True
                bfs.append([nr, nc, cost+1, skill])

if flag is False:
    print(-1)