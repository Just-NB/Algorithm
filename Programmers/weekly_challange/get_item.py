'''
1. 누적합으로 사각형 모두 그리기
2. 외부에서 시작하여 1이상의 값을 만나면 경계면 체크
'''
from collections import deque
MAX = 110  # 직사각형을 나타내는 모든 좌표값은 1 <= N <= 50

dr = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1), (1, 0), (1, 1), (-1, -1)]   # 8방향 확인.
def prefix_sum(rectangle):
    board = [[0 for _ in range(MAX)] for _ in range(MAX)]
    for r in rectangle:
        board[r[1] * 2][r[0] * 2] += 1  # 누적합 preprocessing
        board[r[3] * 2 + 1][r[2] * 2 + 1] += 1
        board[r[1] * 2][r[2] * 2 + 1] -= 1
        board[r[3] * 2 + 1][r[0] * 2] -= 1

    for r in range(1, MAX): # col을 고정, row
        for c in range(MAX):
            board[r][c] += board[r - 1][c]

    for c in range(1, MAX):
        for r in range(MAX):
            board[r][c] += board[r][c - 1]
    return board


def get_border(board):
    visit = [[False for _ in range(MAX)] for _ in range(MAX)]
    border = [[0 for _ in range(MAX)] for _ in range(MAX)]

    for start_r in range(MAX):
        for start_c in range(MAX):
            dq = deque()
            if visit[start_r][start_c] is True:
                continue
            if board[start_r][start_c] != 0:
                continue
            visit[start_r][start_c] = True
            dq.append([start_r, start_c])
            while len(dq) != 0:
                row, col = dq.popleft()

                for r, c in dr:  # 현재위치 8방향 확인.
                    nr = row + r
                    nc = col + c
                    if 0 <= nr < MAX and 0 <= nc < MAX:  # 범위 안에 있다.
                        if visit[nr][nc] is True:
                            continue
                        if board[nr][nc] == 0:  # 벽이 아니라면 이동대기 큐에 추가한다..
                            dq.append([nr, nc])
                        else:  # 벽이 있다면
                            border[nr][nc] = 1  # 경계면 체크하고 넘어간다.
                        visit[nr][nc] = True

    return border


def find_item(border, c_c, c_r, i_c, i_r):
    visit = [[False for _ in range(MAX)] for _ in range(MAX)]
    dq = deque()
    visit[c_r][c_c] = True
    dq.append([c_r, c_c, 0])  # c_r, c_c : character_row, character_col
    while len(dq) != 0:
        cr, cc, step = dq.popleft()  #cr, cc : current_row, current_col
        if (cr, cc) == (i_r, i_c):
            return step

        for r, c in dr[:4]:
            nr = cr + r
            nc = cc + c
            if 0 <= nr < MAX and 0 <= nc < MAX:
                if visit[nr][nc] is True:
                    continue
                if border[nr][nc] == 1:
                    visit[nr][nc] = True
                    dq.append([nr, nc, step + 1])

    return 9999


def solution(rectangle, characterC, characterR, itemC, itemR):
    answer = 0
    board = prefix_sum(rectangle)
    border = get_border(board)
    answer = find_item(border, characterC * 2, characterR * 2, itemC * 2, itemR * 2) // 2
    return answer


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8), " : 17")
print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1), " : 11")
print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3), " : 10")
