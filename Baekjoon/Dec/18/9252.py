'''
Title   : LCS 2
Level   : G5
Problem : 두 수열이 주어졌을 떄, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
Type    : dp
Idea    : 1. A, B 문자열을 하나하나 읽어가며 부분수열의 길이를 찾는다.
          2. 만약 A[i] == B[j]일 경우, 이전 수열에서 하나를 추가한다.
          3. 만약 A[i] != B[j]일 경우, 이전 수열중 가장 긴 수열을 선택한다.
          4. row : b_idx, col : a_idx일 때, dp[row][col]은 a[0~col] 과 b[0~row]까지의 문자열 중 가장 긴 부분수열
          5. A[col] != B[row] 일 때
          5-1. dp[row][col] = max(dp[row-1][col], dp[row][col-1])
          5-2. A의 문자열중 하나를 덜 썻을떄 혹은, B의 문자열중 하나를 덜 썻을때의 부분 문자열중 더 긴것을 선택한다.
          6. A[col] == B[row] 일 때
          6-1. dp[row][col] = dp[row-1][col-1] + 1
          6-2. A/B 문자열 모두 한개씩 덜 썻을때 + 현재 문자를 더했을 때
'''
a = input()
b = input()
dp = [[[0,''] for _ in range(len(a)+1)] for __ in range(len(b)+1)]

for i in range(len(b)):
    for j in range(len(a)):
        if a[j] == b[i]: # 같으면 추가.
            dp[i+1][j+1][0] = dp[i][j][0] + 1
            dp[i+1][j+1][1] = dp[i][j][1] + a[j]
        else:
            if dp[i][j+1][0] < dp[i+1][j][0]:
                dp[i+1][j+1][0] = dp[i+1][j][0]
                dp[i+1][j+1][1] = dp[i+1][j][1]
            else:
                dp[i + 1][j + 1][0] = dp[i][j+1][0]
                dp[i + 1][j + 1][1] = dp[i][j+1][1]

print(dp[-1][-1][0])
print(dp[-1][-1][1])