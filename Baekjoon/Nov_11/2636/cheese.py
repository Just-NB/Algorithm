'''
Level   : G4
Problem : 사각형 모양의 판, 그 위에 얇은 치즈가 있다.
          판의 가장자리에는 치즈가 없다. 치즈에는 하나 이상의 구멍이 있을 수 있다.
          공기와 접촉하는 치즈는 한시간 후 녹아 없어진다.
          비어있지만 치즈로 둘러싸져 있는 부분은 녹지 않는다.
          몇 시간 후 모든 치즈가 녹는가?
Idea    : 1. (0,0)에서 시작
          2. 상하좌우중 치즈가 아닌 부분을 다음 탐색범위로 bfs를 실행
          2-1. 탐색여부를 저장할 배열 사용.
          3. 치즈인 부분일 경우 지운다.
'''
from collections import deque

R, C = map(int, input().split())
board = []
for r in range(R):
    board.append(list(map(int,  input().split())))

dq = deque()
hour = 0
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)  # 상 하 좌 우
last_melting = 0

while True:  # 모든 치즈가 녹아 없어질때까지 반복.
    hour += 1
    melting_cnt = 0
    dq.append((0, 0))  # 시작위치
    visit = [[False for _ in range(C)] for __ in range(R)]
    while len(dq) != 0:
        r, c = dq.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < R and 0 <= nc < C:  # 범위 안의 좌표이면서
                if visit[nr][nc] is True:  # 이미 방문한 좌표라면 넘어간다.
                    continue
                if board[nr][nc] == 0:  # 치즈가 아니면
                    dq.append((nr, nc))  # 다음 방문 추가.
                elif board[nr][nc] == 1:  # 치즈라면
                    board[nr][nc] = 0  # 녹인다.
                    melting_cnt += 1
                visit[nr][nc] = True

    if melting_cnt == 0:
        break
    else:
        last_melting = melting_cnt
print(hour-1)
print(last_melting)
