'''
Title   : 부분합
Level   : G4
Problem : 10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다
          이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성한다.
Type    : 투포인터
Idea    : 1. 주어진 수열의 prefix_sum을 미리 구해둔다.
          2. i ~ j 구간합은 prefix_sum[j] - prefix_sum[i]로 구할 수 있다.
          3. left, right 투 포인터를 사용한다.
          4. prefix_sum[right] - prefix_sum[left] < S 일 때
          4-1. left ~ right 구간합이 목표보다 작으므로 right을 늘려 더 큰 수를 만든다.
          5. prefix_sum[right] - prefix_sum[left] >= S 일 때
          5-1. left ~ right 구간합이 목표보다 크거나 같으므로 원하는 구간을 찾았다.
          5-2. 최소 구간을 찾기 위해 기존에 찾은 구간보다 짧은지를 확인하고 left를 늘려 더 작은 수로 만든다.
          6. left 혹은 right가 범위 밖으로 나간다면 더이상 찾을 수 없다.
'''
import math

N, S = map(int, input().split())
seq = list(map(int, input().split()))
pre_sum = [0 for _ in range(N+1)]
pre_sum[1] = seq[0]
for i in range(2, N+1):
    pre_sum[i] = pre_sum[i-1] + seq[i-1]

left, right = 0, 0
ans = math.inf
while True:
    if right > N or left > N :
        break
    partial = pre_sum[right] - pre_sum[left]

    if partial < S:
        right += 1
    else:
        ans = min(right - left, ans)
        left += 1

print(ans if ans != math.inf else 0)




