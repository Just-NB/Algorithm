'''
Title   : 세 용액
Level   : G4
Problem : 산성 용액은 1 ~ 1,000,000,000까지의 양의 정수
          알칼리성 용액은 -1 ~ -1,000,000,000까지의 음의 정수로 나타낸다.
          같은 양의 세 가지 용액을 혼합하여 특성값이 0 에 가장 가까운 용액을 만들어내는 세 용액을 찾는 프로그램을 작성한다.
Type    : 투포인터, 이분탐색
Idea    : 1. 오름차순으로 용액의 특성을 정렬한다.
          2. 맨 왼쪽 left 사용을 고정으로 하고, 나머지 용액을 사용하여 0과 근사하게 한다.
'''
import math

N = int(input())
nums = sorted(list(map(int, input().split())))
ans = [0, 0, 0]
flag = False
min_val = math.inf
for l in range(N):
    num = nums[l]
    left, right = l+1, N-1
    while left < right:
        tmp = nums[right] + nums[left] + num
        if abs(tmp) < min_val:
            min_val = abs(tmp)
            ans = [num, nums[right], nums[left]]
        if tmp < 0:
            left += 1
        elif tmp > 0:
            right -= 1
        else:
            flag = True
            break

    if flag is True:
        break

for a in sorted(ans):
    print(a, end=' ')