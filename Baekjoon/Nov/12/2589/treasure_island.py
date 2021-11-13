'''
Level   : G5
Problem : 보물지도의 각 칸은 육지/바다로 표시되어있다.
          상하좌우에 이웃한 육지로만 이동가능하다. 같은곳을 두번이상 지나갈 수 없다.
          보물은 최단 거리로 이동할때 가장 긴 시간이 걸리는 육지 두곳에 나뉘어 묻혀있다.
          최단 거리로 이동하는 시간을 구한다.
Idea    : 1. 완전 탐색을 한다.
          2. L을 만나면 bfs를 통해 다른 육지들과의 거리를 적는다.
          3. 시작위치/도착위치/거리를 비교하며 저장한다.
'''
from collections import deque

def bfs(r, c) :
    dq = deque()
    dq.append((r, c))  # row, col
    visit = [[0 for _ in range(C)] for __ in range(R)]
    visit[r][c] = 1
    ret = 0
    while len(dq) != 0:
        r, c = dq.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < R and 0 <= nc < C:
                if board[nr][nc] == 'L' and visit[nr][nc] == 0:
                    visit[nr][nc] = visit[r][c] + 1
                    ret = max(ret, visit[nr][nc])
                    dq.append((nr, nc))
    return ret - 1

R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(input()))

dr, dc = (-1,1,0,0), (0,0,-1,1)
answer = 0
for r in range(R):
    for c in range(1,C):
        if board[r][c] == 'L':
            answer = max(answer, bfs(r,c))

print(answer)