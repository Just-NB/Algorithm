'''
Title   : 벽 부수고 이동하기
Level   : G4
Problem : NxM의 행렬로 표현되는 맵이 있다. 0은 이동할 수 있고, 1은 이동할 수 없다.
          (1,1) -> (N,M)으로 이동할 때, 최단 경로를 찾는다.
          만약 이동하는 도중 한개의 벽을 부수고 이동하는 것이 경로가 짧다면 1개 까지 부술 수 있다.
          최단 경로를 구해내는 프로그램을 작성한다.
Type    : bfs
Idea    : 1. 기본적인 bfs 미로찾기 알고리즘을 사용한다.
          2. 방문 여부를 확인할 때, 해당 좌표에 도달하기 까지 벽을 뚫고 왔는지 여부를 한번 더 체크한다.
          2-1. visit[row][col][0/1] : 0 - 벽을 안뚫음 / 1 - 벽을 뚫음
'''
from collections import deque
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1) #상 하 좌 우
visit = [[[False, False] for _ in range(M)] for __ in range(N)]
# visit[row][col][0/1]

bfs = deque()
bfs.append([0, 0, 0, 1]) # row, col, 벽 뚫었는지 여부, 걸음걸이
flag = True
while len(bfs) != 0:
    row, col, wall, step = bfs.popleft()
    if [row, col] == [N-1, M-1]:
        flag = False
        print(step)
        break
    for i in range(4):
        nr, nc = row+dr[i], col+dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if wall == 0:
                if board[nr][nc] == '1' and visit[nr][nc][wall] is False:
                    bfs.append([nr, nc, 1, step+1])
                    visit[nr][nc][1] = True
                if board[nr][nc] == '0' and visit[nr][nc][0] is False:
                    bfs.append([nr, nc, 0, step+1])
                    visit[nr][nc][0] = True
            else:
                if board[nr][nc] == '0' and visit[nr][nc][1] is False:
                    bfs.append([nr, nc, 1, step+1])
                    visit[nr][nc][1] = True
if flag is True:
    print(-1)