import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())
nums = [0] * N
for i in range(N):
    nums[i] = int(input())

