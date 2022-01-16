'''
Title   : RGB 거리
Level   : S1
Problem : N개의 집이 있다. 집은 R/G/B 하나의 색으로 칠해야 한다.
          각각의 색으로 칠하는 비용이 주어졌을 때, 규칙을 만족하며 모든 집을 칠하는 최소비용을 구한다
          1. 1번 - 2번 집의 색은 같지 않아야 한다
          2. N번 - N-1번 집의 색은 같지 않아야 한다.
          3. i번 집의 색은 i-1번/i+1번 집의 색과 같지 않아야 한다.
Type    : DP
Idea    : 1. 1~2규칙은 3번 규칙을 위한 말 같다.
          2. 집을 한칸씩 칠해나간다.
          3. 모든 색에 대해, 직전의 색과 다른 색으로 칠하면서 누적된 비용의 합이 최소가 되도록 모두 저장한다.
          4. DP[i][R or G or B] : i번째 집의 R, G, B 색을 칠했을 때의 누적 비용 합의 최소
          5. DP[i][R] = min(DP[i-1][G], DP[i-1][B]) + cur[R]
'''

N = int(input())
house = []
for _ in range(N):
    house.append(list(map(int, input().split())))
dp = [[0, 0, 0] for _ in range(N)]
R, G, B = 0, 1, 2
dp[0] = house[0]
for i in range(1, N):
    dp[i][R] = min(dp[i - 1][G], dp[i - 1][B]) + house[i][R]
    dp[i][G] = min(dp[i - 1][R], dp[i - 1][B]) + house[i][G]
    dp[i][B] = min(dp[i - 1][R], dp[i - 1][G]) + house[i][B]
print(min(dp[-1]))