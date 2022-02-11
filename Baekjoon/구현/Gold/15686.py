from itertools import combinations
MAX = 9999
def get_dist(chicken, home):
    c_dist = 0
    for h in home:
        hm_dist = MAX  # 현재 집에서 치킨과의 최소 거리.
        hr, hc = h
        for c in chicken:
            cr, cc = c
            dist = abs(hr - cr) + abs(hc - cc)
            hm_dist = min(dist, hm_dist)
        c_dist += hm_dist
    return c_dist


N, M = map(int, input().split())
board = []
chickens = []  # 치킨 집 좌표
homes = []  # 집 좌표
for n in range(N):
    tmp = list(map(int, input().split()))
    for i, t in enumerate(tmp):
        if t == 1:
            homes.append([n, i])
        elif t == 2:
            chickens.append([n, i])
    board.append(tmp)

comb = combinations(chickens, M)  # 살아남을 치킨집들의 조합.
ans = MAX
for c in comb:
    c_dist = get_dist(c, homes)
    ans = min(ans, c_dist)
print(ans)

