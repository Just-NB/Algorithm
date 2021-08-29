import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
Hx, Hy = map(int, input().split())
Ex, Ey = map(int, input().split())
maze = []
for n in range(N):
    maze.append(list(map(int, input().split())))

visit = [[[False,False] for _ in range(M)] for __ in range(N)]
bfs = deque() # [ x, y, cost, skill ]
bfs.append([Hx-1, Hy-1, 0, 1])
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우
result = False
while len(bfs) != 0:
    x, y, cost, skill = bfs.popleft()
    if x == Ex-1 and y == Ey-1 :
        print(cost)
        result = True
        break
    if visit[x][y][skill] is True:
        continue
    visit[x][y][skill] = True

    for dx,dy in delta:
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < M :
            if maze[nx][ny] == 0 :
                bfs.append([nx,ny,cost+1, skill])
            elif maze[nx][ny] == 1 and skill == 1:
                bfs.append([nx,ny,cost+1, 0])

if result is False:
    print(-1)