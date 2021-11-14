'''
Title   : 두 개의 배열
Level   : S3
Problem : 서로다른 양의 정수를 N개 포함한 A배열, M개 포함한 B 배열이 있다.
          A,B를 이용하여 길이가 n인 새로운 배열 C를 만든다.
          1. C[i] = B에 있는 값중 A[i]에 가장 가까운값
          2. 조건을 만족하는 값이 여럿 있을 경우, 가장 작은 값
          1 <= n,m <= 10^6
Type    : 이분탐색
Idea    : 1. B를 정렬한다.
          2. A[i]의 값을 B에서 이분탐색한다.
          3. 이분탐색의 결과로 같은 값이 안 나오더라도, target과 최대한 가까운 값이 찾아진다.
          4. 이분탐색의 결과의 양옆과 비교하여 조건을 만족하는 값을 찾는다.
'''
import math
def bin_search(b, target):
    left, right = 0, len(b)-1
    ret = b[left]
    while left < right:
        mid = (left+right)//2
        if b[mid] < target:
            left = mid+1
        elif b[mid] > target:
            right = mid
        else:
            return mid
    return left
T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B.sort()
    answer = 0
    for a in A:
        idx = bin_search(B, a)
        diff = math.inf
        small_diff = 0
        for i in range(1, -2,-1):
            if abs(B[(idx-i)%m] - a) < diff :
                diff = abs(B[(idx-i) % m] - a)
                small_diff = B[(idx-i) % m]
        answer += small_diff
    print(answer)