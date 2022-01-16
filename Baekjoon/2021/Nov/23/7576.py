'''
Title   : 토마토
Level   : S1
Problem : MxN크기의 토마토 상자가 있다. 익은 토마토에 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토에 영향을 받아 익게 된다.
          창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 최소일수를 출력한다.
          토마토의 인접한 곳은 상/하/좌/우 4방향이다.
Type    : BFS
Idea    : 1. 1을 찾는다.
          2. 찾은 1을 기점으로 상하좌우를 탐색한다.
          3. 해당 칸이 인접해있는 토마토라면, 좀 더 가까운 토마토와 연관되어있는지 비교한다.
'''
import math
from collections import deque
C, R = map(int, input().split())
board = []
for r in range(R):
    board.append(list(map(int, input().split())))

visit = [[math.inf for _ in range(C)] for __ in range(R)]

bfs = deque()
dr, dc = (-1,1,0,0), (0,0,-1,1)

for r in range(R):
    for c in range(C):
        if board[r][c] == -1:
            visit[r][c] = -1
        if board[r][c] == 1: # 탐색 시작
            bfs.append([r, c, 1])
            visit[r][c] = 0

while len(bfs) != 0:
    cr, cc, d = bfs.popleft()
    for i in range(4):
        nr, nc = cr+dr[i], cc+dc[i]
        if 0 <= nr < R and 0 <= nc < C: # 범위 안에있고,
            if visit[nr][nc] > d and board[nr][nc] != -1: # 기록된 값이 현재 깊이보다 낮고, 토마토가 있다면
                bfs.append([nr, nc, d+1])
                visit[nr][nc] = d
flag = True
ans = 0
for v in visit:
    ans = max(ans, max(v))
    if math.inf in v:
        flag = False
        break
if flag is True:
    print(ans)
else:
    print(-1)