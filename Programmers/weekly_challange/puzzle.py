import copy
from collections import deque, Counter

N = 0
MAX = 9999
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)  # 상 하 좌 우


def find_position(r, c, board, visit, val):
    bfs = deque()
    bfs.append([r, c])
    r_min, c_min = MAX, MAX
    pos = []

    while len(bfs) != 0:
        r, c = bfs.popleft()  # 실제 좌표
        r_min, c_min = min(r_min, r), min(c_min, c)
        visit[r][c] = True
        pos.append([r, c])
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] == val and visit[nr][nc] is False:
                    bfs.append([nr, nc])

    for i in range(len(pos)):
        pos[i][0] -= r_min
        pos[i][1] -= c_min
    return pos


def make_piece(pos):
    r_max, c_max = 0, 0
    for p in pos:
        r_max, c_max = max(p[0], r_max), max(p[1], c_max)
    r, c = r_max, c_max
    piece = [[0 for _ in range(c + 1)] for _ in range(r + 1)]
    for p in pos:
        piece[p[0]][p[1]] = 1
    return piece


def get_piece(r, c, board, visit, val):
    pos = find_position(r, c, board, visit, val)
    piece = make_piece(pos)
    return piece


def rotate(pattern):
    new_pattern = []
    for p in zip(*pattern[::-1]):
        new_pattern.append(list(p))
    return new_pattern


def get_pattern_size(pattern):
    return sum(sum(p) for p in pattern)


def fill_pattern(pattern, puzzles):
    for puzzle in puzzles:
        p = puzzle
        for i in range(4):
            p = rotate(p)
            if pattern == p:
                cnt = get_pattern_size(pattern)
                puzzles.remove(puzzle)
                return cnt
    return 0


def solution(game_board, table):
    global N
    N = len(game_board)
    visit_b = [[False for _ in range(N)] for _ in range(N)]
    visit_t = [[False for _ in range(N)] for _ in range(N)]
    patterns = []
    puzzles = []

    for r in range(N):
        for c in range(N):
            if visit_b[r][c] is False and game_board[r][c] == 0: # 방문하지 않았고 벽이 채워 넣을 수 있으면
                patterns.append(get_piece(r, c, game_board, visit_b, 0))
            if visit_t[r][c] is False and table[r][c] == 1:
                puzzles.append(get_piece(r, c, table, visit_t, 1))
            visit_b[r][c], visit_t[r][c] = True, True

    answer = 0
    for pattern in patterns:
        answer += fill_pattern(pattern, puzzles)

    return answer










# print(f'{solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]], [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]])} : 14')
print(f'{solution([[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]], [[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]])} : 54')