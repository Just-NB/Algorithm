'''
Title   : Four Squares
Level   : S4
Problem : 모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현할 수 있다.
          자연수 n이 주어질 떄, n을 최소 개수의 제곱수 합으로 표현하자.
          1 <= n <= 50,000
Type    : DP
Idea    : 1. 각 자연수를 만들기 위한 최소 갯수를 저장할 배열을 만든다.
          2. i : 제곱수/ j : 만들고자하는 자연수라 할때
          3. dp[j] = min(1+dp[j-i], dp[j]) 이다.

'''
n = int(input())
max_depth = int(n**(1/2) + 1)
dp = [i for i in range(n+1)]
for i in range(2, max_depth) :
    for j in range(i*i, n+1):
        dp[j] = min(1+dp[j-i*i], dp[j])
print(dp[-1])