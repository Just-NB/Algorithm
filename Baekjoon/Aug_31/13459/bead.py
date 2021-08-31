import sys,copy
from collections import deque
input = sys.stdin.readline

N,M = map(int, input().split())
maze = []
RED, BLUE = [0, 0], [0, 0]
EXIT = [0, 0]
visit = [[[[False for _ in range(M)]for __ in range(N)]for ___ in range(M)] for ____ in range(N)]
for r in range(N):
    line = list(input().strip())
    if 'B' in line:
        BLUE = [r, line.index('B')]
    if 'R' in line:
        RED = [r, line.index('R')]
    maze.append(line)
visit[RED[0]][RED[1]][BLUE[0]][BLUE[1]] = True

def move(bead, d):
    row, col = bead
    cnt = 0
    while True:
        row += d[0]
        col += d[1]
        cnt += 1
        if 0 <= row < N and 0 <= col < M:
            if maze[row][col] == '#':
                return row-d[0], col-d[1], cnt-1
            if maze[row][col] == 'O':
                return row, col, cnt


def bfs():
    queue = deque()
    queue.append([RED, BLUE, 1]) # 위치, 횟수
    direction = [(-1,0), (1,0), (0,-1), (0,1)] # 위 아래 왼쪽 오른쪽
    while queue:
        red, blue, cnt = queue.popleft()
        if cnt > 10:
            return 0
        for m in direction:
            red_r, red_c, red_cnt = move(red, m)
            blue_r, blue_c, blue_cnt = move(blue, m)
            if maze[blue_r][blue_c] == 'O':
                continue
            if maze[red_r][red_c] == 'O':
                return 1
            if red_r == blue_r and red_c == blue_c:
                if red_cnt < blue_cnt:
                    blue_r -= m[0]
                    blue_c -= m[1]
                else :
                    red_r -= m[0]
                    red_c -= m[1]
            if visit[red_r][red_c][blue_r][blue_c] is False:
                visit[red_r][red_c][blue_r][blue_c] = True
                queue.append([[red_r,red_c], [blue_r,blue_c], cnt+1])
    return 0

print(bfs())