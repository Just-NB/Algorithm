'''
Title   : 평범한 배낭
Level   : G5
Problem : 배낭을 최대한 가치 있게 싸려고 한다.
          N개의 물건이 있다, 각 물건은 무게 W와 가치 V를 갖는다.
          최대 K만큼의 무게를 넣었을때의 가치의 최댓값을 찾는 프로그램을 만든다.
Type    : 다이나믹 프로그래밍
Idea    : 1. DP[k] : k무게만큼 넣었을때 가치의 최댓값
          2. w ~ K 까지 반복하며, DP[i] = max(DP[i-w]+V, DP[i])로 비교한다.
          2-1. DP[i-w] : w무게를 채우고 난후, 나머지 무게를 다른 물건으로 채웠을때의 가치
          2-2. w ~ K 를 역순으로 순회하여, 같은 물건이 2개 적제되지 않도록 한다.
'''

N, K = map(int, input().split())
dp = [0 for _ in range(K+1)]
for _ in range(N):
    w, v = map(int, input().split())
    for i in range(K, w-1, -1):
        dp[i] = max(dp[i-w] + v, dp[i])

print(dp[-1])