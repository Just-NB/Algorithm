'''
Title   : 최소 스패닝 트리
Level   : G4
Problem : 그래프가 주어졌을 때, 최소 스패닝 트리를 구하는 프로그램을 작성한다.
Type    : 탐욕적 방법, PRIM MST
Idea    : 1. 정점과 간선의 갯수가 많으므로 인접리스트를 이용하여 그래프를 구현한다.
          2. PRIM MST를 구현한다.
          2-1. 1번 노드를 시작으로 인접한 노드들을 cost기준 최소힙으로 저장한다.
          2-2. 최소힙의 값을 꺼내면서, 만약 꺼내진 노드가 이전에 방문했다면 다음 값을 꺼낸다.
          2-3. 최초로 꺼내진 노드일 경우, 해당 노드를 시작으로 2-1 ~ 2-2 과정을 반복한다.
'''
import heapq


def solution(V, E, graph):
    ret = 0
    visited = [False for _ in range(V+1)]
    visited[0], visited[1] = True, True
    heap = []
    #1번 노드와 인접된 노드를 최소 힙으로 저장
    for node, cost in graph[1]:
        heapq.heappush(heap, (cost, node))
    while len(heap) != 0:
        cost, node = heapq.heappop(heap)
        # 현재 노드가 방문한 적이 있으면, 다음 노드 확인
        if visited[node] is True:
            continue
        ret += cost
        visited[node] = True
        # 현재 노드와 인접한 노드를 모두 힙에 넣는다.
        for n, c in graph[node]:
            heapq.heappush(heap, (c, n))

    return ret


if __name__ == "__main__":
    V, E = list(map(int, input().split()))
    graph = [[] for _ in range(V+1)]
    for e in range(E):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])
        #graph[a][b] = min(c, graph[a][b])
        #graph[b][a] = min(c, graph[b][a])


    print(solution(V, E, graph))