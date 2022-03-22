N = int(input())
if N % 2 != 0: print(0)
else:
    dp = [0 for _ in range(N + 1)]
    dp[0], dp[2] = 1, 3

    for i in range(3, N + 1):
        if i % 2 != 0: continue
        dp[i] = dp[i - 2] * 3 + sum(dp[:i - 3]) * 2

    print(dp[-1])