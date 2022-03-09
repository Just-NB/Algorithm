import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list(input()) for _ in range(N)]
visit = [[[False, False] for _ in range(N)] for _ in range(N)]

dr, dc = (0, 0, -1, 1), (-1, 1, 0, 0)

def sector(r: int, c: int, color:str, b: int):
    bfs = deque()
    bfs.append([r, c])
    visit[r][c][b] = True
    while bfs:
        r, c = bfs.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if visit[nr][nc][b]: continue
                if board[nr][nc][b] != color: continue
                visit[nr][nc][b] = True
                bfs.append([nr, nc])


for r in range(N):
    for c in range(N):
        if board[r][c] == 'G':
            board[r][c] = ['G', 'R']
        else:
            board[r][c] = [board[r][c], board[r][c]]

answer_n = 0
answer_b = 0

for r in range(N):
    for c in range(N):
        if visit[r][c][0] is False:
            answer_n += 1
            sector(r, c, board[r][c][0], 0)
        if visit[r][c][1] is False:
            answer_b += 1
            sector(r, c, board[r][c][1], 1)
print(f'{answer_n} {answer_b}')