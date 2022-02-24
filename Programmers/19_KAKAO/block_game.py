from collections import deque


def is_removable(board, r_min, r_max, c_min, c_max, val):
    for r in range(r_min, r_max):
        for c in range(c_min, c_max):
            if board[r][c] != val and board[r][c] != -1:
                return False
    return True


def change_block(board, valid, r_min, r_max, c_min, c_max):
    for r in range(r_min, r_max):
        for c in range(c_min, c_max):
            if valid[c]:
                board[r][c] = -1
            else:
                board[r][c] = 0


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
MAX = 9999
def get_block_pos(board, r, c, N, val):
    r_min, r_max, c_min, c_max = MAX, 0, MAX, 0
    visit = [[False for _ in range(N)] for _ in range(N)]
    visit[r][c] = True
    bfs = deque()
    bfs.append([r, c])
    while bfs:
        r, c = bfs.popleft()
        r_min, r_max, c_min, c_max = min(r, r_min), max(r, r_max), min(c, c_min), max(c, c_max)
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] == val and visit[nr][nc] is False:
                    bfs.append([nr, nc])
                    visit[nr][nc] = True
    return r_min, r_max + 1, c_min, c_max + 1


def valid_change(board, valid, r_min, c_min, c_max):
    if r_min == 0:
        for c in range(c_min, c_max):
            valid[c] = True
    else:
        for c in range(c_min, c_max):
            if board[r_min - 1][c] == -1:
                valid[c] = True
            else:
                valid[c] = False


def solution(board):
    N = len(board)
    valid = [True for _ in range(N)]
    answer = 0
    for r in range(N):
        for c in range(N):  # 블록 떨어 트리기.
            if valid[c] is False:
                continue
            if board[r][c] == 0:
                board[r][c] = -1
        for c in range(N):  # 터트릴 수 있는 블록 확인하기.
            if board[r][c] != 0 and board[r][c] != -1:
                val = board[r][c]
                valid[c] = False
                r_min, r_max, c_min, c_max = get_block_pos(board, r, c, N, val)
                if is_removable(board, r_min, r_max, c_min, c_max, val):
                    answer += 1
                    valid_change(board, valid, r_min, c_min, c_max)
                    change_block(board, valid, r_min, r_max, c_min, c_max)
    return answer

'''
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
[0, 0, 0, 0, 0, 4, 4, 0, 0, 0], 
[0, 0, 0, 0, 3, 0, 4, 0, 0, 0], 
[0, 0, 0, 2, 3, 0, 0, 0, 5, 5], 
[1, 2, 2, 2, 3, 3, 0, 0, 0, 5], 
[1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]

[0,0,0,0,0,0,0,0,0,0]
[0,0,0,2,2,0,0,0,0,0]
[0,0,0,2,1,0,0,0,0,0]
[0,0,0,2,1,0,0,0,0,0]
[0,0,0,0,1,1,0,0,0,0]
[0,0,0,0,0,0,0,0,0,0]

[[0, 0, 1, 1, 1], [0, 0, 0, 1, 0], [3, 0, 0, 2, 0], [3, 2, 2, 2, 0], [3, 3, 0, 0, 0]] 0
[[0, 0, 0, 0, 0], [1, 0, 0, 2, 0], [1, 2, 2, 2, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]] 2
[[0, 2, 0, 0], [1, 2, 0, 4], [1, 2, 2, 4], [1, 1, 4, 4]] 3

'''

print(f'{solution([[0, 2, 0, 0], [1, 2, 0, 4], [1, 2, 2, 4], [1, 1, 4, 4]])} : 3')
# print(f'{solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0], [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5], [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]])} : 2')
# print(f'{solution([[0,0,0,0,0,0,0,0,0,0], [0,0,0,2,2,0,0,0,0,0], [0,0,0,2,1,0,0,0,0,0], [0,0,0,2,1,0,0,0,0,0], [0,0,0,0,1,1,0,0,0,0], [0,0,0,0,0,0,0,0,0,0]])} : 1')