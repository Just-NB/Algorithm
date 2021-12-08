'''
Title   : LCS
Level   : G5
Problem : LCS란 두 수열이 주어졌을 떄, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
          문자열이 주어졌을때, 문자열의 LCS를 찾는 프로그램을 만든다.
Type    : 다이나믹 프로그래밍
Idea    : 1. 2차원 배열로 DP를 구현한다.
          2. 두 문자열 S1, S2라 할 때, dp[i][j] : S1의 0~i, S2의 0~j까지의 문자열 사이의 LCS 최장 길이
          3. S1[i] == S[j] 일 경우, LCS의 길이는 1칸 늘어난다.
          3-1. dp[i][j] = dp[i-1][j-1]+1
          3-2. i-1, j-1까지의 최장 LCS길이에 +1 한다.
          4. S1[i] != S[j] 일 경우, LCS의 길이는 이전의 값을 가져온다.
          4-1. dp[i][j] = max(dp[i][j-1], dp[i-1][j])
          4-2. 다를 경우, S1혹은 S2의 1칸 전의 LCS 길이 중 큰 것을 가져온다.
'''

s1 = input()
s2 = input()
dp = [[0 for _ in range(len(s2)+1)] for __ in range(len(s1) + 1)]
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

print(max(dp[-1]))