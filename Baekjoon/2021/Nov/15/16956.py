'''
Title   : 늑대와 양
Level   : S3
Problem : 크기가 RxC인 목장이 있다. 각 칸은 비어있거나 양, 늑대가 있다.
          양은 이동하지 않는다. 늑대는 인접한 칸을 이동한다.(상하좌우)
          목장에 울타리를 설치해 늑대가 양이 있는 곳으로 못가게 하려고 한다.
Type    : bfs, 구현.
Idea    : 1. 양의 상하 좌우에는 양 또는 빈 공간만 있어야 한다.
          2. bfs를 통해 양의 상하좌우에 늑대가 없는지 확인한다.
'''
from collections import deque

R, C = map(int, input().split())
board = []
visit = [[False for _ in range(C)] for __ in range(R)]
for _ in range(R):
    board.append(list(input()))

bfs = deque()
dr, dc = (-1,1,0,0),(0,0,-1,1)
flag = True
for r in range(R):
    if flag is False:
        break
    for c in range(C):
        if flag is False:
            break

        if board[r][c] == 'S' and visit[r][c] is False:
            visit[r][c] = True
            bfs.append((r, c))
            while len(bfs) != 0:
                if flag is False:
                    break
                cur_r, cur_c = bfs.popleft()
                for i in range(4):
                    nr, nc = cur_r+dr[i], cur_c+dc[i]
                    if 0 <= nr < R and 0 <= nc < C and visit[nr][nc] is False:
                        if board[nr][nc] == 'S':
                            bfs.append((nr, nc))
                        elif board[nr][nc] == 'W':
                            flag = False # 실패
                            break
                        else:
                            board[nr][nc] = 'D'
                        visit[nr][nc] = True
if flag is True:
    print(1)
    for b in board:
        print(''.join(b))
else:
    print(0)
