import sys

input = sys.stdin.readline

shape_one = [[1, 1, 1, 1]]
shape_two = [[1, 1], [1, 1]]
shape_three = [[1, 1, 1], [0, 1, 0]]
shape_four = [[1, 0], [1, 0], [1, 1]]
shape_five = [[1, 0], [1, 1], [0, 1]]
shape_six = [[0, 1], [0, 1], [1, 1]]
shape_seven = [[0, 1], [1, 1], [1, 0]]
shapes = [shape_one, shape_two, shape_three, shape_four, shape_five, shape_six, shape_seven]


def brute(N: int, M: int, r: int, c: int, board: list) -> int:
    max_size = 0
    for i, shape in enumerate(shapes):
        for _ in range(4):
            size = 0
            shape = list(zip(*shape[::-1]))
            for sr in range(len(shape)):
                for sc in range(len(shape[0])):
                    nr, nc = r + sr, c + sc
                    if 0 <= nr < N and 0 <= nc < M:
                        size += (board[nr][nc] * shape[sr][sc])
                    else:
                        size = 0
                        break
                if size == 0:
                    break
            max_size = max(size, max_size)

    return max_size

def solve(N: int, M: int, board: list) -> None:
    answer = 0
    for r in range(N):
        for c in range(M):
            answer = max(answer, brute(N, M, r, c, board))
    print(answer)


if __name__ == '__main__':
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    solve(N, M, board)

    # tetrominos = [[[0, 1], [0, 2], [0, 3]],
    #               [[1, 0], [2, 0], [3, 0]],
    #               [[0, 1], [1, 0], [1, 1]],
    #               [[1, 0], [2, 0], [2, 1]],
    #               [[1, 0], [1, -1], [1, -2]],
    #               [[0, 1], [1, 1], [2, 1]],
    #               [[0, 1], [0, 2], [1, 0]],
    #               [[1, 0], [1, 1], [2, 1]],
    #               [[0, 1], [1, 0], [1, -1]],
    #               [[0, 1], [0, 2], [1, 1]],
    #               [[1, 0], [1, 1], [2, 0]],
    #               [[1, 0], [1, -1], [1, 1]],
    #               [[1, 0], [2, 0], [1, -1]],
    #               ]

    # def brute(N: int, M: int, r: int, c: int) -> int:
    #     max_size = 0
    #
    #     for tetromino in tetrominos:
    #         size = board[r][c]
    #         for row, col in tetromino:
    #             nr, nc = r + row, c + col
    #             if 0 <= nr < N and 0 <= nc < M:
    #                 size += board[nr][nc]
    #             else:
    #                 size = 0
    #                 break
    #         if size:
    #             max_size = max(size, max_size)
    #
    #     return max_size
