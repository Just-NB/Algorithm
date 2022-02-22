import heapq
def solution(food_times, k):
    answer = -1
    leftover = len(food_times)  # 남은 음식의 갯수.
    food_heap = [[time, idx + 1] for idx, time in enumerate(food_times)]
    heapq.heapify(food_heap)
    prev_time = 0
    while food_heap:
        food_time, food = food_heap[0]  # 전부 먹는 시간, 먹을 음식
        eat_time = (food_time - prev_time) * leftover  # 현재 음식의 남은 갯수만큼 모든 음식을 먹을때 걸리는 시간.
        if k >= eat_time:
            k -= eat_time
            prev_time = heapq.heappop(food_heap)[0]
            leftover -= 1
        else:
            food_heap.sort(key=lambda x: x[1])  # 인덱스 순으로 다시 정렬
            return food_heap[k % leftover][1]
    return answer

print(f'{solution([3, 1, 2], 5)} : 1')
print(f'{solution([3, 5, 1, 6, 5, 3], 20)} : 4')
print(f'{solution([3, 2, 3, 4, 7, 7], 19)} : 4')

'''
def next_idx(food_times, k):
    while True:
        k = (k + 1) % len(food_times)
        if food_times[k] != 0:
            return k


def simple_solution(food_times, k):
    idx, cnt = 0, 0
    MAX = sum(food_times)
    while True:
        # print(idx, cnt)
        if cnt == MAX - 1:
            return -1
        if cnt == k - 1:
            return next_idx(food_times, idx) + 1
        if food_times[idx] != 0:
            food_times[idx] -= 1
            cnt += 1
        idx = next_idx(food_times, idx)
    return answer
'''