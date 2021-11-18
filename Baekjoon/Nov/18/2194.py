'''
Title   : 유닛 이동시키기
Level   : G5
Problem : NxM 크기의 2차원 행렬의 맵.
          AxB 크기의 유닛, 상하좌우 이동가능. 장애물이 있는 경우, 이동 불가능
          목적지까지 이동하기 위한 최소 이동횟수 구하기
Type    : 시뮬레이션
Idea    : 1. bfs를 사용하여 이동한다.
          2. visit여부는 왼쪽 위를 기준으로 한다.
'''
from collections import deque
# NxM : N행 M열
n, m, a, b, k = map(int, input().split())
board = [[0 for _ in range(m)] for __ in range(n)]
visit = [[False for _ in range(m)] for __ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1
sr, sc = map(int, input().split())
er, ec = map(int, input().split())
sr -= 1
sc -= 1
er -= 1
ec -= 1

bfs = deque()
bfs.append([sr, sc, 0])
visit[sr][sc] = True
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
success = False

while len(bfs) != 0:
    r, c, d = bfs.popleft()
    if (r, c) == (er, ec):
        print(d)
        success = True
        break

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i] # nr,nc는 왼쪽 맨위.
        if 0 <= nr < (n - a + 1) and 0 <= nc < (m - b + 1):
            is_wall = False

            for k in range(a):
                if is_wall is True:
                    break
                for j in range(b):
                    if is_wall is True:
                        break
                    if board[nr+k][nc+j] == 1:
                        is_wall = True

            if visit[nr][nc] is False and is_wall is False:
                bfs.append([nr, nc, d+1])
                visit[nr][nc] = True

if success is False:
    print('-1')
