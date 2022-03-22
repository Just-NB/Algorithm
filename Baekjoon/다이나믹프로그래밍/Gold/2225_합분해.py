N, K = map(int, input().split())
dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]
MOD = 1000000000
dp[0][0] = 1
for k in range(1, K + 1):
    for n in range(N + 1):
        for l in range(n + 1):
            dp[k][n] += dp[k-1][n - l]
            dp[k][n] = dp[k][n] % MOD
print(dp[K][N] % MOD)
