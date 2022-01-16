'''
Title   : 가장 긴 증가하는 부분 수열 2
Level   : G2
Problem : 수열 A가 주어졌을 떄, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성한다.
          ex) A = {10, 20, 10, 30, 20, 50}의 경우 {10, 20, 30, 50}이고, 길이는 4 이다.
Type    : 다이나믹 프로그래밍, 이분 탐색
Idea    : 1. DP[l] : 길이 l인 증가 부분 수열 중, 마지막이 최소인 값
          2. 모든 수열을 순서대로 탐색한다.
          3. DP[l] > nums[i] : DP의 마지막에 nums[i]를 추가한다.
          4. DP[l] <= nums[i] : DP안에서 nums[i]의 lower_bound를 찾고 nums[i]로 값을 바꾼다.
          5. 최종적으로 DP[l]의 길이가 LIS의 길이.
'''


# 세그먼트 트리 풀이
tree = []

def find_max_val(node_id, start, end, left, right):
    '''
    :param node_id: 트리의 노드 id 
    :param start: 트리 탐색 시작 지점
    :param end: 트리 탐색 종료 지점
    :param left: 찾고자 하는 구간 시작 지점
    :param right: 찾고자 하는 구간 종료 지점
    :return: 찾고자 하는 구간의 최댓값
    '''
    # 범위 밖이면 0을 반환, 재귀가 반복될 수록 end 는 줄어들고 start는 커지므로 범위체크를 한다.
    if left > end or right < start:
        return 0
    # 범위 안이면 현재 값 반환
    if left <= start and end <= right:
        return tree[node_id]
    mid = (start + end) // 2
    ret = max(find_max_val(node_id * 2 + 1, start, mid, left, right),
              find_max_val(node_id * 2 + 2, mid + 1, end, left, right))
    return ret


def update(node_id, start, end, idx, val):
    '''
    :param node_id: 트리의 노드 id
    :param start: 트리 탐색 시작 지점
    :param end: 트리 탐색 종료 지점
    :param idx: 변경할 인덱스
    :param val: 변경할 값
    '''
    if idx > end or idx < start:
        return
    if start == end:
        tree[node_id] = val
        return

    mid = (start + end) // 2
    update(node_id * 2 + 1, start, mid, idx, val)
    update(node_id * 2 + 2, mid + 1, end, idx, val)

    tree[node_id] = max(tree[node_id * 2 + 1], tree[node_id * 2 + 2])


N = int(input())
nums = list(map(int, input().split()))

tree = [0] * 4000000 # 4를 곱하면 모든 범위를 커버할 수 있다. 트리는 2의 제곱형태의 길이를 갖는다.

s_nums = [(v, i) for i, v in enumerate(nums)]
s_nums.sort(key = lambda x: (x[0], -x[1])) # val기준으로 정렬, val이 같을 경우 idx 기준으로 정렬한다.

for val, idx in s_nums:
    max_val = find_max_val(0, 0, N - 1, 0, max(idx - 1, 0))
    update(0, 0, N - 1, idx, max_val + 1)

print(tree[0])






# 이분탐색 풀이
# # lower bound는 데이터내 특정 K값보다 같거나 큰값이 처음 나오는 위치를 리턴
# def lower_bound(left, right, val):
#     while (left < right):
#         mid = (left + right) // 2
#         if val <= DP[mid]:
#             # {1, 2, 2, 3, 3} 의 수열에서 3의 lower_bound는 idx = 3이다.
#             # 따라서 같은 경우도 범위를 좁혀나간다.
#             right = mid
#         else:
#             left = mid + 1
#
#     return left
#
# N = int(input())
# nums = list(map(int, input().split()))
# DP = [-1]
# length = 0
# for n in nums:
#     if n > DP[length]:
#         DP.append(n)
#         length += 1
#     elif n < DP[length]:
#         lb = lower_bound(0, length, n)
#         DP[lb] = n
#
# print(len(DP)-1)
