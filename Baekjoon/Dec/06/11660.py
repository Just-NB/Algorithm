'''
Title   : 구간 합 구하기 5
Level   : S1
Problem : NxN개의 수가 NxN 크기의 표에 채워져 있다
          (x1, y1) ~ (x2,y2)까지의 합을 구하는 프로그램을 작성한다.
Type    : DP
Idea    : 1. 각 row 마다 누적합을 저장한 DP배열을 만든다..
          2. 임의의 x에 대해 dp[x][y2] - dp[x][y1-1] 은 y1~y2의 누적합을 의미한다.
          3. 입력된 x범위만큼 2. 과정을 반복한다.
'''
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list() for _ in range(N)]
dp = [[0 for _ in range(N+1)] for __ in range(N+1)]
for n in range(N):
    board[n] = list(map(int, input().split()))

for i in range(N):
    for j in range(N):
        dp[i+1][j+1] = dp[i+1][j] + board[i][j]

for m in range(M):
    x1, y1, x2, y2 = map(int, input().split()) # x == row/ y == col
    answer = 0
    for x in range(x1, x2+1):
        answer += (dp[x][y2] - dp[x][y1-1])
    print(answer)