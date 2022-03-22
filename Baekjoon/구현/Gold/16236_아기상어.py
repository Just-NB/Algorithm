import sys
from collections import deque
input = sys.stdin.readline
'''
4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
'''
N = 0
board = []
sr, sc = 0, 0
shark = 2
feed_cnt = 0
fishes = []
dr, dc = (-1, 0, 0, 1), (0, -1, 1, 0)


def INIT():
    global N, board, sr, sc, shark, feed_cnt, fishes
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    fishes = [[] for _ in range(10)]
    for r in range(N):
        for c in range(N):
            if 0 < board[r][c] < 9:
                for size in range(board[r][c], 10):
                    fishes[size].append([r, c])
            if board[r][c] == 9:
                board[r][c] = 0
                sr, sc = r, c


def BFS(r: int, c: int, fr: int, fc: int) -> list:
    visit = [[False for _ in range(N)] for _ in range(N)]
    visit[r][c] = True
    bfs = deque()
    bfs.append([r, c, 0])
    while bfs:
        r, c, d = bfs.popleft()
        if (r, c) == (fr, fc):
            return d
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if visit[nr][nc]: continue
                if board[nr][nc] > shark: continue
                bfs.append([nr, nc, d + 1])
                visit[nr][nc] = True

    return 0


def SOLVE():
    global sr, sc, feed_cnt, shark, fishes
    answer = 0
    eat = [[False for _ in range(N)] for _ in range(N)]

    while True:
        dist = sys.maxsize

        r, c = 0, 0
        for fr, fc in fishes[shark - 1]:
            if eat[fr][fc]: continue
            d = BFS(sr, sc, fr, fc)
            if 0 < d < dist:
                r, c, dist = fr, fc, d
        if dist == sys.maxsize:
            return answer
        eat[r][c] = True
        sr, sc = r, c
        board[sr][sc] = 0
        feed_cnt += 1
        if feed_cnt == shark:
            feed_cnt = 0
            shark = shark + 1 if shark < 10 else 10

        answer += dist

INIT()
print(SOLVE())

