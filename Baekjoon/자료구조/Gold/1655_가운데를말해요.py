import heapq
import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    min_heap = []
    max_heap = []
    for n in range(N):
        num = int(input())
        if len(max_heap) == len(min_heap):
            heapq.heappush(max_heap, (-num, num))
        else:
            heapq.heappush(min_heap, (num, num))

        if min_heap and max_heap[0][1] > min_heap[0][1]:
            maxh, minh = heapq.heappop(max_heap), heapq.heappop(min_heap)
            heapq.heappush(max_heap, (-minh[1], minh[1]))
            heapq.heappush(min_heap, (maxh[1], maxh[1]))
        print(-max_heap[0][1])

solve()
