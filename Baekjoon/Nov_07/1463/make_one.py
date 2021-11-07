'''
Level   : S3
Problem : 1. X가 3으로 나누어 떨어지면 3으로 나눈다.
          2. X가 2로 나누어 떨어지면 2로 나눈다.
          3. 1을 뺸다.
          3가지 규칙을 이용하여 숫자 N을 1로 만드는 연산 최소횟수를 출력
Idea    : f(x) = x를 1로 만들기 위한 최소횟수라 할때
          f(x) = min(f(x-1) , f(x/2), f(x/3))+1
'''

x = int(input())
dp = [0 for _ in range(x+1)]
#dp[1],dp[2],dp[3] = 0,1,1
for i in range(2, x+1):
    r_one, r_two, r_three = x+2, x+2, x+2
    r_one = dp[i-1]
    if i % 2 == 0:
        r_two = dp[i//2]
    if i % 3 == 0:
        r_three = dp[i//3]
    dp[i] = min(r_one, r_two, r_three) + 1
print(dp[x])