import sys

input = sys.stdin.readline

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
cleaner = []
for r in range(R):
    if len(cleaner) == 2: break
    for c in range(C):
        if len(cleaner) == 2: break
        if board[r][c] == -1:
            cleaner.append([r, c])

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
def spread(r: int, c: int) -> None:
    global board
    num_spread = 0
    dust = board[r][c] // 5
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            if board[nr][nc] == -1: continue
            num_spread += 1
            tmp[nr][nc] += dust
    board[r][c] -= num_spread * dust

def clean(row, col, cw):
    idx, nxt_dust, prev_dust = 0, 0, 0
    i = cw[idx]
    r, c = row, col
    while 1:
        nr, nc = r + dr[i], c + dc[i]
        if [nr, nc] == [row, col]:
            break
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            idx = (idx + 1) % 4
            i = cw[idx]
            continue
        nxt_dust = board[nr][nc]
        board[nr][nc] = prev_dust
        prev_dust = nxt_dust
        r, c = nr, nc

for t in range(T):
    tmp = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c] == 0: continue
            if board[r][c] == -1: continue
            spread(r, c)

    for r in range(R):
        for c in range(C):
            board[r][c] += tmp[r][c]
    # dr, dc를 사용하여 시계/반시계 방향 이동하기 위한 idx 순서 모음
    cw, ccw = [3, 0, 2, 1], [3, 1, 2, 0]
    clean(*cleaner[0], cw)
    clean(*cleaner[1], ccw)

answer = 0
for b in board:
    answer += sum(b)
answer += 2
print(answer)