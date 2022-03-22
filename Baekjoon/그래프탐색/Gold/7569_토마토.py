import sys
from collections import deque

input = sys.stdin.readline

C, R, H = map(int, input().split())
board = []
visit = [[[False for _ in range(C)] for _ in range(R)] for _ in range(H)]
tomato = []
for h in range(H):
    floor = []
    for r in range(R):
        tmp = list(map(int, input().split()))
        for c, t in enumerate(tmp):
            if t == 1: tomato.append((h, r, c, 0))
        floor.append(tmp)
    board.append(floor)

#  위, 아래, 왼쪽, 오른쪽, 앞, 뒤
dh, dr, dc = (-1, 1, 0, 0, 0, 0), (0, 0, -1, 1, 0, 0), (0, 0, 0, 0, -1, 1)

def BFS():
    bfs = deque()
    for t in tomato:
        bfs.append(t)
    while bfs:
        h, r, c, d = bfs.popleft()
        for i in range(6):
            nh, nr, nc = h + dh[i], r + dr[i], c + dc[i]
            if 0 <= nh < H and 0 <= nr < R and 0 <= nc < C:
                if board[nh][nr][nc] == 0:
                    bfs.append((nh, nr, nc, d + 1))
                    board[nh][nr][nc] = 1

    for floor in board:
        for t in floor:
            if 0 in t:
                return -1
    return d
print(BFS())

