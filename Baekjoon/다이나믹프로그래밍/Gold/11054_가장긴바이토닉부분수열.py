import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
dp = [1 for _ in range(N)]
dp_r = [1 for _ in range(N)]
nums_r = list(reversed(nums))
for end in range(N):
    for i in range(end):
        if nums[end] > nums[i]:
            dp[end] = max(dp[end], dp[i] + 1)
        if nums_r[end] > nums_r[i]:
            dp_r[end] = max(dp_r[end], dp_r[i] + 1)

answer = 0
for a, b in zip(dp, dp_r[::-1]):
    answer = max(answer, a + b - 1)
print(answer)