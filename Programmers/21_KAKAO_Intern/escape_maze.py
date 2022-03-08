import copy
import heapq
import math

TRAP_LEN = 1025
N = 1001
FWD, RVS = 0, 1 # 정방향, 역방향
graph = []
trap_info = []

def dijkstra(start, end):
    dist = [[math.inf for _ in range(N)] for _ in range(TRAP_LEN)]
    pq = []
    dist[0][start] = 0
    heapq.heappush(pq, [0, start, 0])  # cost, node, state
    while pq:
        cost, cur, state = heapq.heappop(pq)
        if cur == end:
            return cost
        # 현재 내 위치가 트랩이라면 해당 비트를 키거나 끈다.
        if trap_info[cur] != -1:
            state ^= (1 << trap_info[cur])

        for nxt, c in graph[state][cur]:
            nxt_cost = cost + c
            if dist[state][nxt] <= nxt_cost:
                continue
            dist[state][nxt] = nxt_cost
            heapq.heappush(pq, [nxt_cost, nxt, state])


def solution(n, start, end, roads, traps):
    global graph, trap_info
    graph = [[[] for _ in range(N)] for _ in range(TRAP_LEN)]

    trap_info = [-1 for _ in range(N)]

    for i, t in enumerate(traps):
        trap_info[t] = i

    for state in range(1 << len(traps)):  # 모든 상태에 대해서.
        for u, v, w in roads:
            left, right = 0, 0
            # 두 노드 중 하나라도 트랩인 경우
            if trap_info[u] != -1:
                left = 1 if (state & (1 << trap_info[u])) else 0  # 현재 상태는 u트랩을 밟은 상태이다.
            if trap_info[v] != -1:
                right = 1 if (state & (1 << trap_info[v])) else 0
            if left ^ right:  # 둘 중 하나의 트랩만 밟은 경우, 간선의 방향이 바뀐다.
                u, v = v, u
            graph[state][u].append([v, w])
    answer = dijkstra(start, end)
    return answer
print(f'{solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2])} :5')
print(f'{solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])} : 4')