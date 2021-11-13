'''
Level   : S3
Problem : 1,2,5,7 원 동전이 있다. 물건을 계산할 때, 동전의 개수가 최소가 되도록 한다.
          ex) 17원 = 7원 1개, 5원 2개
Idea    : knapsack 문제의 일종같으니 DP로 풀어본다.
          f(x) = x원 만들때 필요한 동전의 최소개수
          f(x) = min(f(x), 1 + f(x-coin))
'''
# 지불 금액
x = int(input())
coins = [2,5,7]
dp = [i for i in range(x+1)]
# 시간복잡도 : O(4n)
for coin in coins:
    for i in range(coin, x+1) :
        dp[i] = min(dp[i], 1 + dp[i-coin])

print(dp[-1])