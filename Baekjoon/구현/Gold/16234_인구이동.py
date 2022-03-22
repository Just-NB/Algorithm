from collections import deque
N, L, R = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dr, dc = [0, 0, -1, 1], [-1, 1, 0, 0]
# grouping
def grouping(row: int, col: int) -> list:
    bfs = deque()
    bfs.append([row, col, grid[row][col]])
    group = [(row, col)]
    total = grid[row][col]
    visit[row][col] = True
    while bfs:
        r, c, val = bfs.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
            if visit[nr][nc]: continue
            if L <= abs(grid[nr][nc] - val) <= R:
                group.append((nr, nc))
                total += grid[nr][nc]
                bfs.append([nr, nc, grid[nr][nc]])
                visit[nr][nc] = True
    group.append(total)
    return group  # [좌표] + [총 인구수]


# division
def division(group):
    global grid
    group, total = group[:-1], group[-1]
    nums_group = len(group)
    for r, c in group:
        grid[r][c] = total//nums_group


answer = 0
while True:
    end_flag = True
    visit = [[False for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if visit[r][c]: continue
            group = grouping(r, c)
            if len(group) != 2: # 본인 좌표와 본인 값만 들어가 있는 경우 제외.
                end_flag = False
            division(group)
    if end_flag:
        break
    answer += 1

print(answer)
