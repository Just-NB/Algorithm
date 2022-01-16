'''
Title   : 보석도둑
Level   : G2
Problem : 보석이 N개 있고, 각 보석은 무게 M과 가치 V를 가지고 있다
          K개의 가방이 있고, 각 가방에 담을 수 있는 최대 무게는 C이다.
          가방에는 한개의 보석만 넣을 수 있다
          훔칠 수 있는 보석의 최대 가격을 작성한다.
Type    : 그리디 알고리즘,
Idea    : 1. 보석을 무게를 기준으로 오름차순 정렬한다.
          2. 가방을 무게를 기준으로 오름차순 정렬한다.
          3. 가방의 무게에 맞는 보석 중 가치가 가장 비싼것을 선택한다.
          3-1. 무게기준 오름차순 정렬 하였기 때문에 i번째 무게에 맞는 보석을 힙에 넣은 경우
          3-2. i+1번째 무게에 맞는 보석을 찾을때, i번째 무게에 사용한 힙을 그대로 사용할 수 있다.
'''
import heapq
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    answer = 0
    N, K = map(int, input().split())

    gems = [[0, 0] for _ in range(N)]
    for n in range(N):
        gems[n] = list(map(int, input().split()))
    bags = [0 for _ in range(K)]
    for k in range(K):
        bags[k] = int(input())

    gems.sort()
    bags.sort()
    used_gem = [False for _ in range(N)]

    gem_idx = 0
    heap = []
    for w in bags:
        while gem_idx < N:
            m, v = gems[gem_idx]
            if m <= w:
                heapq.heappush(heap, (-v, v))
                gem_idx += 1
            else:
                break

        if len(heap) > 0:
            answer += heapq.heappop(heap)[1]

    print(answer)
