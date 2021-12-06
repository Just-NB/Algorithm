'''
Title   : 스티커
Level   : S1
Problem : 스티커 2n개를 구매했다. 2행 n열로 배치되어 있다.
          스티커 한 장을 떼면, 변을 공유하는 스티커는 모두 사용할 수 없다.(왼쪽/오른쪽/위/아래)
          스티커에 점수를 매기고, 점수의 합이 최대가 되게 스티커를 떼어내려고 한다.
          점수의 최댓값을 구하는 프로그램을 작성한다.
Type    : 다이나믹 프로그래밍
Idea    : 1. 2행 N열의 DP배열을 사용한다.
          2. DP[0 or 1][i] : i번 째열 까지의 점수의 합의 최대
          3. 0행 i번째 스티커를 떼기 위해서는
             (1행 i-1열)의 스티커를 떼거나
             (1행 i-2열)의 스티커를 떼야 한다.
          4. DP[0][i] = max(DP[1][i-1], DP[1][i-2])+(0,i)의 점수
'''

T = int(input())
for tc in range(T):
    N = int(input())
    up_scores = list(map(int, input().split()))
    down_scores = list(map(int, input().split()))
    dp = [[0 for _ in range(N)] for _ in range(2)]
    for i in range(N):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + up_scores[i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + down_scores[i]
    print(max(dp[0][-1], dp[1][-1]))

