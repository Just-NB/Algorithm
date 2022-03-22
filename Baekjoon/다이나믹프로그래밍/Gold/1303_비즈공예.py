import sys

input = sys.stdin.readline

N = int(input())
beads = [0 for _ in range(5)]
for n in range(N):
    beads[n] = int(input())
memo = [[[[[[[-1 for _ in range(6)] for _ in range(6)] for a in range(11)] for b in range(11)] for c in range(11)] for d in range(11)] for e in range(11)]
total = sum(beads)


def memoization(size: int, pp: int, p: int) -> int:
    if size == total:
        return 1

    if memo[beads[0]][beads[1]][beads[2]][beads[3]][beads[4]][pp][p] != -1:
        return memo[beads[0]][beads[1]][beads[2]][beads[3]][beads[4]][pp][p]
    # 한번 확인한 경우, 다시 확인할 필요가 없다.
    ret = 0

    for i, b in enumerate(beads):
        if i == p or i == pp: continue
        if b == 0: continue
        beads[i] -= 1
        ret += memoization(size + 1, p, i)
        beads[i] += 1

    memo[beads[0]][beads[1]][beads[2]][beads[3]][beads[4]][pp][p] = ret
    return ret

print(memoization(0, -1, -1))