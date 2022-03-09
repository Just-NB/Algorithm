import copy
import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
total_area = 0
for b in board:
    for num in b:
        if num == 0:
            total_area += 1
# print(total_area)
wall_list = []
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
def infected_area() -> int:
    bfs = deque()
    for r in range(R):
        for c in range(C):
            if board[r][c] == 2:
                bfs.append([r, c])
    visit = [[False for _ in range(10)] for _ in range(10)]
    area = -len(bfs)
    while bfs:
        r, c = bfs.popleft()
        if visit[r][c]:
            continue
        visit[r][c] = True
        area += 1
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < R and 0 <= nc < C:
                if board[nr][nc] == 1:
                    continue
                bfs.append([nr, nc])
    return area


def set_wall(cr: int, cc: int, wall: list):
    if len(wall) == 3:
        wall_list.append(copy.deepcopy(wall))
        return
    for nr in range(cr, R):
        if nr != cr: cc = -1
        for nc in range(cc + 1, C):
            if board[nr][nc] == 0:
                wall.append([nr, nc])
                set_wall(nr, nc, wall)
                wall.remove([nr, nc])

set_wall(0, -1, [])
answer = 0
for wall in wall_list:
    a, b, c = wall
    board[a[0]][a[1]] = 1
    board[b[0]][b[1]] = 1
    board[c[0]][c[1]] = 1
    answer = max(answer, total_area - infected_area() - 3)
    board[a[0]][a[1]] = 0
    board[b[0]][b[1]] = 0
    board[c[0]][c[1]] = 0

print(answer)