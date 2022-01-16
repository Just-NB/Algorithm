'''
Title   : 행렬 곱셈 순서
Level   : G3
Problem : NxM 크기의 행렬 A와 MxK인 B를 곱할 때 연산의 수는 NxMxK번이다.
          행렬 N개를 곱하는데 필요한 곰셈 연산의 수는 행렬을 곱하는 순서에 따라 달라지게 된다.
          행렬 N개의 크기가 주어졌을때, 모든 행렬을 곱하는데 필요한 곱셈 연산 횟수의 최솟값을 구하는 프로그램을 작성한다.
Type    : 다이나믹 프로그래밍
Idea    : 1. ABC를 구하기 위해서는 AB/BC의 곱셈 횟수를 알아야 한다.
          2. ABCD를 구하기 위해서는 (ABC)D/ (AB)(CD)/ A(BCD)의 횟수를 알아야 한다
          3. 1의 과정을 통해 ABC의 횟수를 구할 수 있고, 이를 ABCD를 구할 때 사용할 수 있다.
          4. 곱셈의 길이 2 ~ N-1까지 반복하며 미리 계산하고 그 값을 이용한다.
          5. DP[i][j] : i ~ j 까지의 곱셈 횟수의 최솟값, k를 i ~ j 를 나누는 중간값
          5-1. DP[i][j] = min(DP[i][j], DP[i][k] + DP[k+1][j] + 나머지 곱셈횟수)
          5-2. ABCD : i = 0, j = 3, k : 1 -> (AB)(CD)
          5-3. ABCD : i = 0, j = 3, k : 2 -> (ABC)D
'''
import math

if __name__ == '__main__':
    N = int(input())
    dp = [[[math.inf, 0, 0] for _ in range(N)] for _ in range(N)] # val, A x B(행렬 크기)
    for n in range(N):
        a, b = map(int, input().split())
        dp[n][n] = [0, a, b] # value, 행렬의 크기

    for length in range(2, N+1): # 길이는 2부터 = 두 행렬의 곱 부터
        for i in range(N-length+1): # 시작 행렬은 j가 범위에 벗어나지 않게
            j = i + length - 1
            for k in range(i, j): # 중간 분리지점은 i부터 j이전까지
                a, b, c = dp[i][k][1], dp[i][k][2], dp[k+1][j][2]
                tmp = dp[i][k][0] + dp[k+1][j][0] + a*b*c
                if tmp < dp[i][j][0]:
                    dp[i][j] = [tmp, a, c]
    print(dp[0][-1][0])
