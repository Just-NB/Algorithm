import sys

input = sys.stdin.readline
'''
0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0
'''
board = [list(map(int, input().split())) for _ in range(9)]
used_r = [[False for _ in range(10)] for _ in range(10)]
used_c = [[False for _ in range(10)] for _ in range(10)]
used_g = [[False for _ in range(10)] for _ in range(10)]

def get_group(row: int, col: int)-> int:
    return 3 * (row // 3) + col // 3

for r in range(9):
    for c in range(9):
        num = board[r][c]
        g = get_group(r, c)
        if board[r][c] != 0:
            used_r[r][num] = True
            used_c[c][num] = True
            used_g[g][num] = True

def backtracking(row:int, col:int)-> bool:
    nr, nc = row, col + 1
    if col == 8:
        nr, nc = row + 1, 0
    if row == 9:
        return True
    ret = False
    if board[row][col] != 0:
        ret = backtracking(nr, nc)
    else:
        g = get_group(row, col)
        for num in range(1, 10):
            if used_r[row][num]: continue
            if used_c[col][num]: continue
            if used_g[g][num]: continue
            board[row][col] = num
            used_r[row][num] = True
            used_c[col][num] = True
            used_g[g][num] = True

            ret = backtracking(nr, nc)
            if ret: return ret
            board[row][col] = 0
            used_r[row][num] = False
            used_c[col][num] = False
            used_g[g][num] = False
    return ret
backtracking(0, 0)
for r in range(9):
    for c in range(9):
        print(board[r][c], end=' ')
    print()
# for b in board:
#     print(b)
# for g in used_g:
#     print(g[1:])
# for ur, uc in zip(used_r, used_c):
#     print(ur[1:], uc[1:])
