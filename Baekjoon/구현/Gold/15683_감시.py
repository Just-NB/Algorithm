import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
watch = [[0 for _ in range(M)] for _ in range(N)]
cctvs = []  # row, col, val
for r in range(N):
    for c in range(M):
        if board[r][c] == 0: continue
        if board[r][c] == 6: continue
        cctvs.append([r, c, board[r][c]])


ON, OFF = 1, -1
def recursive(idx:int) ->int:
    if idx == len(cctvs):
        ret = calculate()
        return ret
    ret = 65
    for i in range(4):
        cctv(idx, i, ON)
        ret = min(ret, recursive(idx + 1))
        cctv(idx, i, OFF)
    return ret

# 0123 = 상하좌우
# 1 : 0, 1, 2, 3
# 2 : 01, 23
# 3 : 02, 03, 12, 13
# 4 : 023, 013, 123, 012
# 5 : 1234
# CCTV가 바라보는 방향
directions = [[[0], [1], [2], [3]],
              [[0, 1], [2, 3]],
              [[0, 2], [0, 3], [1, 2], [1, 3]],
              [[0, 2, 3], [0, 1, 3], [1, 2, 3], [0, 1, 2]],
              [[0, 1, 2, 3]]]
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

def cctv(idx: int, i: int, flag: int) -> None:
    global watch
    row, col, t = cctvs[idx]
    if t == 2 and i >= 2: return
    if t == 5 and i >= 1: return
    for d in directions[t - 1][i]:
        r, c = row, col
        while True:
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                break
            if board[nr][nc] == 6: break
            if board[nr][nc] == 0:
                watch[nr][nc] += flag
            r, c = nr, nc

def calculate() -> int:
    ret = 0
    for r in range(N):
        for c in range(M):
            if board[r][c] != 0: continue
            if watch[r][c] == 0:
                ret += 1
    return ret

print(recursive(0))

