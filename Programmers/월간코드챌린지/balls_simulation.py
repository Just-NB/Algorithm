d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def solution(n, m, r, c, queries):
    queries = queries[::-1]  # 역순으로 체크.
    R, C = [r, r], [c, c]  # [start, end]
    for i, dist in queries:
        dr, dc = dist * d[i][0], dist * d[i][1]
        if i == 0:
            if C[0] != 0:
                C[0] += dc
            C[1] = min(C[1] + dc, m - 1)
        elif i == 1:
            if C[1] != m - 1:
                C[1] += dc
            C[0] = max(C[0] + dc, 0)
        elif i == 2:
            if R[0] != 0:
                R[0] += dr
            R[1] = min(R[1] + dr, n - 1)
        else:
            if R[1] != n - 1:
                R[1] += dr
            R[0] = max(R[0] + dr, 0)

        if C[0] > m - 1 or C[1] < 0 or R[0] > n - 1 or R[1] < 0:
            return 0
    return (R[1] - R[0] + 1) * (C[1] - C[0] + 1)


print(solution(2, 2, 0, 0, [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]]), ': 4')
print(f'{solution(2, 5, 0, 1, [[3, 1], [2, 2], [1, 1], [2, 3], [0, 1], [2, 1]])} : 2')