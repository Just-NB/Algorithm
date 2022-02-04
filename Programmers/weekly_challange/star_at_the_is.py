import math
from itertools import combinations

INF = math.inf
def is_parallel(a, b):
    A, B, E = a
    C, D, F = b
    if (A * D) - (B * C) == 0:
        return True  # 평행이다.
    return False  # 평행이 아니다.


def get_intersection(a, b):
    A, B, E = a
    C, D, F = b
    c = (B * F - E * D) / (A * D - B * C)
    r = (E * C - A * F) / (A * D - B * C)
    return [c, r]


def solution(line):
    N = len(line)
    comb = combinations(line, 2)
    inter = list()
    r_min, r_max, c_min, c_max = INF, -INF, INF, -INF
    for a, b in comb:
        if is_parallel(a, b):
            continue
        c, r = get_intersection(a, b)
        if c % 1 != 0 or r % 1 != 0:  # x, y 모두 정수가 아닐 때
            continue
        c, r = int(c), int(r)
        r_min = min(r, r_min)
        r_max = max(r, r_max)
        c_min = min(c, c_min)
        c_max = max(c, c_max)
        inter.append([r, c])

    row = int(r_max - r_min + 1)
    col = int(c_max - c_min + 1)

    answer = [['.' for _ in range(col)] for _ in range(row)]
    for r, c in inter:
        answer[r_max - r][c - c_min] = '*'
    return [''.join(a) for a in answer]



print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print('["....*....", ".........", ".........", "*.......*", ".........", ".........", ".........", ".........", "*.......*"]')
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print('["*.*"]')