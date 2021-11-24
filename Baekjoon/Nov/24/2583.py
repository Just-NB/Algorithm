'''
Title   : 영역 구하기
Level   : S1
Problem : MxN 크기의 모눈종이가 있다. 눈금에 맞추어 K개의 직사각형을 그릴 떄, K개 직사각형의 내부를 제외한 나머지 부분이 몇개의 분리된 영역으로 나누어진다
          분리된 영역의 갯수와, 각 넓이가 얼마인지를 구하여 출력한다.
Type    : bfs
Idea    : 1. 입력받은 영역의 범위를 통해 2차원 배열의 값을 채운다.
          2. bfs를 통해 분리된 영역의 갯수와 넓이를 출력한다.
'''
from collections import deque
M, N, K = map(int, input().split())
board =[[0 for _ in range(N)] for __ in range(M)]
for _ in range(K):
    c1, r1, c2, r2 = map(int, input().split()) #왼아/ 오위
    for r in range(r1, r2):
        for c in range(c1, c2):
            board[r][c] = 1
visit = [[False for _ in range(N)] for __ in range(M)]
dr, dc = (-1,1,0,0), (0,0,-1,1)


def bfs(r,c):
    q = deque()
    q.append([r, c])
    visit[r][c] = True
    ret = 0
    while len(q) != 0:
        ret += 1
        cr, cc = q.popleft()
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            if 0 <= nr < M and 0 <= nc < N:
                if board[nr][nc] == 0 and visit[nr][nc] is False:
                    q.append([nr,nc])
                    visit[nr][nc] = True
    return ret

cnt, area = 0, []
for r in range(M):
    for c in range(N):
        if board[r][c] == 0 and visit[r][c] is False:
            cnt += 1
            area.append(bfs(r, c))
print(cnt)
for a in sorted(area):
    print(a,end=' ')