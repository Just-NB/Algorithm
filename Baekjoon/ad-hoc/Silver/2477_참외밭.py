import sys
input = sys.stdin.readline


def calculate(boundary: list) -> int:
    b_width, b_idx = 0, 0
    for i, b in enumerate(boundary):
        if b_width < b:
            b_width, b_idx = b, i

    s_idx = b_idx - 1
    if boundary[(b_idx + 1) % 6] >= boundary[b_idx - 1]:
        s_idx = (b_idx + 1) % 6

    b_height = max(boundary[(b_idx + 1) % 6], boundary[b_idx - 1])
    s_height = abs(boundary[(b_idx + 1) % 6] - boundary[b_idx - 1])
    s_width = abs(boundary[(s_idx + 1) % 6] - boundary[s_idx - 1])

    bigger = b_width * b_height
    smaller = s_width * s_height
    return bigger - smaller


def solution() -> None:
    cost = int(input())
    boundary = [0] * 6
    for i in range(6):
        boundary[i] = int(input().split()[1])

    print(calculate(boundary) * cost)


solution()
