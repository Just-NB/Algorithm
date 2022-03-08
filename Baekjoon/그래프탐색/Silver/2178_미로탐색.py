# input
# 4 6
# 101111
# 101010
# 101011
# 111011

import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
board = [input() for _ in range(R)]
visit = [[False for _ in range(C)] for _ in range(R)]
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)


def BFS():
    queue = deque()
    queue.append([0, 0, 1])
    visit[0][0] = True
    while queue:
        r, c, move = queue.popleft()
        if r == R - 1 and c == C - 1:
            return move
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < R and 0 <= nc < C:
                if visit[nr][nc] is True:
                    continue
                if board[nr][nc] == '0':
                    continue
                visit[nr][nc] = True
                queue.append([nr, nc, move + 1])

print(BFS())