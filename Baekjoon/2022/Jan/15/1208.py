'''
Title   : 부분수열의 합
Level   : G1
Problem : N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서
          그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성한다.
Type    : 투포인터, combinations
Idea    : 1. 길이 40 수열의 모든 조합을 만들면 시간이 많이 들어간다
          2. 길이 20의 수열 2개로 나누어 조합을 만들면 2^40 에서 2^20 * 2^20 시간이 들어간다.
          3. combinations함수를 이용하여 조합들을 구한다. 조합은 0 ~ N//2개 사용한다.
          4. 원본 수열을 left, right로 절반 나누어 조합을 구한다.
          5. i개 뽑아 만든 조합들의 합을 keys로 하는 dict를 사용하여, 같은 값이 몇개 나오는지 저장한다.
          6. left, right 조합의 합들을 list로 저장하고, 오름차순으로 정렬한다
          7. left_idx, right_idx를 0, N//2에서 시작한다
          8. left + right < S 이면 left_idx를 증가, left + right > S이면 right를 감소시킨다.
          9. left + right == S이면 각 left, right의 갯수들을 곱하여 ans에 더한다.
          10. S가 0이면 -1한다(공집합 2개를 합친 경우를 제외)
'''
from itertools import combinations
N, S = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0
left = nums[:N // 2]
right = nums[N // 2:]

def get_comb_sum(lst: list) -> dict:
    l = len(lst)
    result = dict()
    for i in range(l + 1):
        comb = combinations(lst, i)
        for c in comb:
            ret = sum(c)
            if ret in result.keys():
                result[ret] += 1
            else:
                result[ret] = 1

    return result

left_sum, right_sum = get_comb_sum(left), get_comb_sum(right)

left_sum = sorted(left_sum.items())
right_sum = sorted(right_sum.items())
l_idx, r_idx = 0, len(right_sum) - 1
while True:
    if l_idx >= len(left_sum) or r_idx < 0: # 범위 밖이면 종료
        break

    tmp = left_sum[l_idx][0] + right_sum[r_idx][0]
    if tmp > S:
        r_idx -= 1
    elif tmp < S:
        l_idx += 1
    else:
        ans += (left_sum[l_idx][1] * right_sum[r_idx][1])
        l_idx += 1
        r_idx -= 1

if S == 0:
    print(ans - 1)
else:
    print(ans)

