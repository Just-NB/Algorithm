'''
Title   : 수 고르기
Level   : G5
Problem : N개의 정수로 이루어진 수열이 있다. 두 수를 골랐을 때, 차이가 M 이상이며 제일 작은 경우를 구한다.
Type    : 투포인터
Idea    : 1. 투 포인터를 사용하기 위해 수열을 오름차순으로 정렬한다.
          2. left, right를 0,1에서 시작하여 두 수의 차를 계산한다.
          3. 두 수의 차가 M 이상이면, 차 들의 최솟값을 저장하고 left를 1 증가한다.
          4. 두 수의 차가 M 보다 크면, right를 1 증가한다.
'''
import math
n, m = map(int, input().split())
seq = [0 for _ in range(n)]
for i in range(n):
    seq[i] = int(input())
seq.sort()

left, right = 0, 1
min_diff = math.inf
while left < n and right < n:
    diff = seq[right] - seq[left]
    if diff >= m:
        min_diff = min(min_diff, diff)
        left += 1
    else :
        right += 1

print(min_diff)

