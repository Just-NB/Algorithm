import sys

input = sys.stdin.readline
def foo():
    n, k = map(int, input().split())
    dp = [0 for _ in range(k + 1)]
    dp[0] = 1
    for _ in range(n):
        coin = int(input())
        for i in range(coin, k + 1):
            dp[i] += dp[i - coin]
    return dp[-1]
print(foo())
