'''
Title   : 단지번호붙이기
Level   : S1
Problem : 정사각형 모양의 지도가 있다. 1은 집이 있는곳, 0은 집이 없는곳이다
          연결된 집의 모임인 단지를 정의하고, 번호를 붙인다.
          연결은 좌우,아래위로 다른집이 있는 경우이다.
          단지 수를 출력하고, 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력한다.
Type    : bfs
Idea    : 1. bfs로 현재위치에서 상하좌우가 1인 경우에만 탐색의 범위로 추가하여 단지를 모은다.
          2. dict자료구조를 이용하여 각 단지별 집 갯수를 저장한다.
          3. dict를 value기준으로 정렬 후, 출력한다.
'''
from collections import deque
N = int(input())
board = [input() for _ in range(N)]
visit = [[False for _ in range(N)] for __ in range(N)]
dr, dc = (-1,1,0,0), (0,0,-1,1)


def bfs(row, col): # 좌표, 단지 번호
    dq = deque()
    dq.append([row, col])
    visit[row][col] = True
    cnt = 0
    while len(dq) != 0:
        r, c = dq.popleft()
        cnt += 1
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] == '1' and visit[nr][nc] is False:
                    dq.append([nr, nc])
                    visit[nr][nc] = True
    return cnt

complex_num = 0
complex_dict = {}
for i in range(N):
    for j in range(N):
        if board[i][j] == '1' and visit[i][j] is False:
            complex_dict[complex_num] = bfs(i, j)
            complex_num += 1

answer = sorted(complex_dict.items(), key= lambda item: item[1])
print(len(answer))
for a in answer:
    print(a[1])
