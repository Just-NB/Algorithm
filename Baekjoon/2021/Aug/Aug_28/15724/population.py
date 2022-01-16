import sys,copy
input = sys.stdin.readline

territory = [] # 영토 내 인구 수
N, M = list(map(int, input().split()))
for _ in range(N):
    territory.append(list(map(int, input().split())))

dp = [[0 for _ in range(M+1)] for __ in range(N+1)]
for n in range(N):
    for m in range(M):
        dp[n+1][m+1] = dp[n+1][m] + territory[n][m]
K = int(input()) # 요청 개수

for _ in range(K):
    population = 0
    lr, lc, rr, rc = list(map(int, input().split()))
    for r in range(lr,rr+1):
        population += (dp[r][rc]-dp[r][lc-1])
    print(population)