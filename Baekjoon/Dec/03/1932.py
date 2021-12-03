'''
Title   : 정수 삼각형
Level   : S1
Problem : 정수가 입력된 삼각형이 있다.
          맨 위에서부터 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때,
          선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성한다.
          아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽/오른쪽 에 있는것만 가능하다.
Type    : 다이나믹 프로그래밍
Idea    : 1. DP[i][j] = max(DP[i-1][j-1],DP[i-1][j]) + triangle[i][j]
          2. 각 단계마다, 그 이전단계의 최대값과 더한다.
'''

N = int(input())
triangle = []
for _ in range(N):
    triangle.append(list(map(int, input().split())))

dp = [[0 for _ in range(N)] for __ in range(N)]

dp[0][0] = triangle[0][0]
for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j]+triangle[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1]+triangle[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
print(max(dp[-1]))