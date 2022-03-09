import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
board = [input() for _ in range(R)]
visit_board = [[False for _ in range(C)] for _ in range(R)]
visit_alpha = [False for _ in range(26)]
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
visit_alpha[ord(board[0][0]) - 65] = True


def dfs(r: int, c: int, depth: int, a: str) -> int:
    if visit_board[r][c] == a:
        return depth
    ret = depth
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            alpha = ord(board[nr][nc]) - 65
            if visit_alpha[alpha]: continue
            visit_alpha[alpha] = True
            ret = max(ret, dfs(nr, nc, depth + 1, a + board[nr][nc]))
            visit_alpha[alpha] = False
    return ret

print(dfs(0, 0, 1, board[0][0]))