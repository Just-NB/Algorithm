'''
Title   : 조합
Level   : S3
Problem : nCm을 출력한다.
Type    : DP
Idea    : 1. nCm = (n)! / ((n-r)! * r!)
          2. fact를 DP로 구한다.
          3. fact[i] = fact[i-1]*i
'''

# 100 6
N , M = map(int, input().split())
fact = [1] * (N+1)
for i in range(1, N+1):
    fact[i] = fact[i-1]*i
print(fact[N] // (fact[N-M] * fact[M]))
