'''
Title   : 다각형의 면적
Level   : G5
Problem : 2차원 평면상에 N개의 점으로 이루어진 다각형이 있다. 이 다각형의 면적을 구하는 프로그램을 작성한다.
Type    : 수학.
Idea    : 1. 신발끈 공식을 이용하여 문제르 푼다.
          2. 신발끈 공식 : 1/2 * ( ((x1 * y2) + (x2 * y3) ... (xn-1 * yn)) - ((x2 * y1) - (x3 * y2) ... (xn * yn_1)) )
'''
import sys

input = sys.stdin.readline
N = int(input())
coord = [[0, 0] for _ in range(N)]
for n in range(N):
    coord[n] = list(map(int, input().split()))
coord.append(coord[0])

ans = 0
for n in range(N):
    ans += (coord[n][0] * coord[n+1][1]) - (coord[n][1] * coord[n+1][0])
ans = abs(round(ans / 2, 1))

print(ans)