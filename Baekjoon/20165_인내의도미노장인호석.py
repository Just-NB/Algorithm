import sys

input = sys.stdin.readline

dir = {'E' : (0, 1), 'N': (-1, 0), 'W' : (0, -1), 'S': (1, 0)}

N, M, R = map(int, input().split())
domino = [list(map(int, input().split())) for _ in range(N)]
visit = [['S' for _ in range(M)] for _ in range(N)]


def attack(r: int, c:int, d: str) -> int:
    global visit
    if visit[r][c] == 'F':
        return 0

    score = 1
    visit[r][c] = 'F'
    K = domino[r][c] - 1
    while K > 0:
        nr, nc = r + dir[d][0], c + dir[d][1]
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            break
        if visit[nr][nc] != 'F':
            visit[nr][nc] = 'F'
            K = max(domino[nr][nc] - 1, K - 1)
            score += 1
        else:
            K -= 1
        r, c = nr, nc

    return score

answer = 0
for _ in range(R):
    r, c, d = input().split()
    answer += attack(int(r) - 1, int(c) - 1, d)
    r, c = map(int, input().split())
    visit[r - 1][c - 1] = 'S'

print(answer)
for v in visit:
    print(' '.join(v))