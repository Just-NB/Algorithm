TC = int(input())

for tc in range(TC):
    N = int(input())
    coins = list(map(int, input().split()))
    money = int(input())

    dp = [0] * (money+1)
    dp[0] = 1
    for coin in coins:
        dp[coin] += 1
        for i in range(coin+1, money+1):
            dp[i] += dp[i-coin]

    print(dp[-1])