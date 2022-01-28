def make_sheet(sheet: list, skill: list) -> list:
    t, r1, c1, r2, c2, d = skill
    if t == 1: d *= -1
    sheet[r1][c1] += d
    sheet[r1][c2 + 1] += d * -1
    sheet[r2 + 1][c1] += d * -1
    sheet[r2 + 1][c2 + 1] += d


def solution(board, skills):
    answer = 0
    sheet = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]
    for skill in skills:
        make_sheet(sheet, skill)

    for c in range(len(board[0])):
        for r in range(1, len(board)):
            sheet[r][c] += sheet[r - 1][c]

    for r in range(len(board)):
        for c in range(1, len(board[0])):
            sheet[r][c] += sheet[r][c - 1]

    for r in range(len(board)):
        for c in range(len(board[0])):
            board[r][c] += sheet[r][c]
            if board[r][c] > 0:
                answer += 1

    return answer




#print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]))
