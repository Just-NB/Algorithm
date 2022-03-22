N = int(input())

dp = [[1 for _ in range(10)] for _ in range(101)]
dp[0][0] = 0

for L in range(1, N):
    dp[L][0] = dp[L - 1][1]
    dp[L][9] = dp[L - 1][8]
    for num in range(1, 9):
        dp[L][num] = dp[L - 1][num - 1] + dp[L - 1][num + 1]

print(sum(dp[N - 1]) % 1000000000)
