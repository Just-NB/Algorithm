import sys
sys.setrecursionlimit(10**6)
dr = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 왼쪽으로/ 아래로/ 오른쪽으로/ 위로 이동
board = []
visit = []
ROW, COL = 0, 0


def change_dir(r, c, d):
    if board[r][c] == 'S':
        return d
    elif board[r][c] == 'L':
        return (d + 1) % 4
    else:
        return (d - 1) % 4


def dfs(r, c, d, step):
    if visit[r][c][d] is True:
        return step
    visit[r][c][d] = True

    nd = change_dir(r, c, d)
    nr, nc = (r + dr[nd][0]) % ROW, (c + dr[nd][1]) % COL
    return dfs(nr, nc, nd, step + 1)


def solution(grid):
    global board, visit, ROW, COL
    board = grid
    ROW, COL = len(grid), len(grid[0])
    visit = [[[False, False, False, False] for _ in range(COL)] for _ in range(ROW)]  # 4방향

    answer = []
    for r in range(ROW):
        for c in range(COL):
            for d in range(4):
                if visit[r][c][d] is False:
                    answer.append(dfs(r, c, d, 0))

    answer.sort()
    return answer


print(solution(["SL", "LR"]), " : [16]")
print(solution(["S"]), " : [1, 1, 1, 1]")
print(solution(["R", "R"]), " : [4, 4]")
