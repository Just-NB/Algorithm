'''
Title   : 최단경로
Level   : G5
Problem : 방향그래프가 주어지면, 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성한다.
Type    : 다익스트라 알고리즘
Idea    : 1. 그래프를 인접리스트로 표현한다
          1-1. 해당 노드에 연결되어있는 노드와 cost를 리스트로 저장한다.
          2. 다익스트라 알고리즘을 구현한다.
          2-1. 최소 힙을 이용하여 다음 탐색할 노드를 찾는다.
          2-2. dp를 이용하여 최소 비용을 저장한다.
          2-3. K 노드와 연결되어있는 가장 싼 cost의 노드를 다음 탐색으로 한다
          2-4. dp[nxt] > dp[cur] + graph[nxt] 일경우 값을 dp[cur] + graph[nxt]로 변경한다.
'''

import heapq
import sys
import math
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [list() for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u-1].append([w, v-1]) # 가중치, 노드

dijkstra = [math.inf] * V

dijkstra[K-1] = 0
heap = [[0, K-1]] # cost, Start
while len(heap) != 0:
    cost, node = heapq.heappop(heap)
    if dijkstra[node] < cost:
        continue
    for c, n in graph[node]:
        if dijkstra[n] > dijkstra[node] + c:
            dijkstra[n] = dijkstra[node] + c
            heapq.heappush(heap, [dijkstra[node] + c, n])
for d in dijkstra:
    if d == math.inf:
        print("INF")
    else:
        print(d)



# graph = [[0 for _ in range(V)] for __ in range(V)]
#
# dijk = [math.inf for _ in range(V)]
# visit = [False for _ in range(V)]
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     graph[u-1][v-1] = w
#
# dijk[K-1] = 0
# node = K - 1
# for _ in range(5):
#     visit[node] = True
#     for i, n in enumerate(graph[node]):
#         if dijk[i] > dijk[node] + n and n != 0:
#             dijk[i] = dijk[node] + n
#
#     cost = math.inf
#     for i, d in enumerate(dijk):
#         if d < cost and visit[i] is False:
#             node = i
#             cost = d
#
# for d in dijk:
#     print(d)
#
# import sys
# import heapq
# input = sys.stdin.readline
# INF = sys.maxsize
# V, E = map(int, input().split())
# #시작점 K
# K = int(input())
# #가중치 테이블 dp
# dp = [INF]*(V+1)
# heap = []
# graph = [[] for _ in range(V + 1)]
# def Dijkstra(start):
# #가중치 테이블에서 시작 정점에 해당하는 가중치는 0으로 초기화
#     dp[start] = 0
#     heapq.heappush(heap,(0, start))
#     #힙에 원소가 없을 때 까지 반복.
#     while heap:
#         wei, now = heapq.heappop(heap)
#         #현재 테이블과 비교하여 불필요한(더 가중치가 큰) 튜플이면 무시.
#         if dp[now] < wei:
#             continue
#         for w, next_node in graph[now]:
#             #현재 정점 까지의 가중치 wei + 현재 정점에서 다음 정점(next_node)까지의 가중치 W
#             # = 다음 노드까지의 가중치(next_wei)
#             next_wei = w + wei
#             #다음 노드까지의 가중치(next_wei)가 현재 기록된 값 보다 작으면 조건 성립.
#             if next_wei < dp[next_node]: #계산했던 next_wei를 가중치 테이블에 업데이트.
#                 dp[next_node] = next_wei #다음 점 까지의 가증치와 다음 점에 대한 정보를 튜플로 묶어 최소 힙에 삽입.
#                 heapq.heappush(heap,(next_wei,next_node))
#                 #초기화
#
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     #(가중치, 목적지 노드) 형태로 저장
#     graph[u].append((w, v))
#
# Dijkstra(K)
# for i in range(1,V+1):
#     print("INF" if dp[i] == INF else dp[i])
#
