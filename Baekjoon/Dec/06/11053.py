'''
Title   : 가장 긴 증가하는 부분수열
Level   : S2
Problem : 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성한다.
Type    : DP
Idea    : 1. dp[i] : i번째 인덱스에서의 증가하는 부분수열의 길이
          2. i번째의 부분수열의 길이는 j 인덱스를 0~i까지 한칸씩 늘려가며 nums[i] > nums[j]
             즉, 증가한다면 j인덱스의 부분수열 길이 + 1한 값과 현재 본인의 값을 비교한다.
'''
N = int(input())
nums = list(map(int, input().split()))
lis = [1 for _ in range(N)]
for i in range(N):
    for j in range(i+1):
        if nums[i] > nums[j]:
            lis[i] = max(lis[i], lis[j]+1)
print(max(lis))