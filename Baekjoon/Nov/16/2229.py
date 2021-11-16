'''
Title   : 조 짜기
Level   : G5
Problem : 잘 하는 학생과 못하는 학생을 같은 조로 묶는다.
          나이차이가 많이 날 경우 부정적인 효과가 있을 수 있다.
          1. 우선 나이 순서대로 정렬한 다음, 학생을 나눈다.
          2. 조가 잘 짜여진 정도는, 가장 점수가 높은 학생의 점수와 낮은 점수의 차이가 된다.
          3. 전체적으로 잘 짜여진 정도는, 각 조의 잘 짜여진 정도의 합으로 나타난다.
          4. 한명일 경우 정도는 0이다.
          잘 짜여진 정도의 최댓값을 구한다.
Type    : 다이나믹 프로그래밍
Idea    : 1. dp[n] = n명으로 조를 짤 때, 잘 짜여진 정도의 최댓값
          2. dp[n] = max( n ~ n-i 의 최대,최소값의 차 + dp[n-i], dp[n])
          3. n명으로 조를 짤때 잘 짜여진 정도를 구하기 위해서는 1~n명을 그룹화 했을때의 값들을 비교한다.
          ex) 2 5 7 1 3 4 8 6 9 3, n = 4일때
          i = 1. dp[4] = max( 3 - 1 + dp[3], dp[4] )
          i = 2. dp[4] = max( 3 - 1 + dp[2], dp[4] ) ...
'''
n = int(input())
score = list(map(int, input().split()))
dp = [0 for _ in range(n+1)]
for i in range(n+1) :
    for j in range(1, i+1):
        max_v, min_v = max(score[i-j:i]), min(score[i-j:i])
        dp[i] = max(max_v - min_v + dp[i-j], dp[i])

print(dp)