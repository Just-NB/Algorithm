'''
Title   : 1,2,3 더하기
Level   : S3
Problem : 정수 n이 주어졌을때, 1,2,3의 합으로 나타내는 방법의 수를 구한다.
Type    : dp
Idea    : 1. dp[n] = dp[n-1] + dp[n-2] + dp[n-3]
          2. n이라는 숫자를 1을 이용해 만드려면, (n-1)을 만들고 1을 추가하는것 과 같다.
          2-1. (n-1)를 만들기 위해서는 (n-2)를 만들고 1을 추가한다.
          3. n이라는 숫자를 2를 이용해 만드려면, (n-2)를 만들고 2를 추가하는것 과 같다.
          4. 2~3을 이용하면 dp[n]을 1과 2로 만들기 위해서는 dp[n] = dp[n-1] + dp[n-2]
'''

T = int(input())
for tc in range(T):
    dp = [1, 1, 2, 4]
    n = int(input())
    for i in range(4, n+1):
        dp.append(dp[i-1]+dp[i-2]+dp[i-3])
    print(dp[n])