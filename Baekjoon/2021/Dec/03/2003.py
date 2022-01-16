'''
Title   : 수들의 합 2
Level   : S3
Problem : N개로 된 수열이 잇다. i~j 번째수의 합이 M이 되는 경우의 수를 구한다.
Type    : prefix sum, 투 포인터
Idea    : 1. N길이의 배열에 각 idx까지의 누적합을 저장한다.
          2. left/right idx를 사용하여 A[right_idx] - A[left_idx]로 i~j 번째 수의 합을 구한다
          3. 누적합이 M 이상이 될 떄까지 right_idx를 늘린다.
          4. M이상이 되면 left_idx를 늘린다.
          5. M 이하가 되면 right_idx를 다시 늘리기 시작한다.
          6. 2~5를 반복하며 답을 구한다.
'''

n, m = map(int, input().split())
nums = list(map(int, input().split()))
pre_sum = [0 for _ in range(n+1)]
left, right = 0, 1
# 1. 누적합 더하기
for i, num in enumerate(nums):
    pre_sum[i+1] = nums[i]+pre_sum[i]
answer = 0
while right < n+1:
    tmp = pre_sum[right] - pre_sum[left]
    if tmp < m:
        right += 1
    elif tmp > m :
        left += 1
    else:
        answer += 1
        right += 1

print(answer)