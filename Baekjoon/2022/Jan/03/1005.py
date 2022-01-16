'''
Title   : ACM Craft
Level   : G3
Problem : 건물 짓는 순서가 정해져 있지 않다. 매 게임시작 시 건물을 짓는 순서가 주어진다.
          모든 건물은 각각 건설을 시작하여 완서이 될 때까지 Delay가 존재한다.
          특정건물을 가장 빨리 지을 때까지 걸리는 최소시간을 알아내는 프로그램을 작성한다.
Type    : 위상정렬, DP
Idea    : 1. 각 노드에 연결되어있는 부모의 갯수를 저장하는 list를 만든다.
          2. 노드에 연결되어 있는 부모가 0인 노드부터 순회를 시작한다.
          3. 현재 노드와 연결되어 있는 자식노드들을 우선순위 Queue에 넣는다.
          4. 우선순위 큐의 값은 (누적 시간, 자식 노드 번호)로 최소 힙을 만든다.
          5. 각 노드에 방문했을 때마다 1에서 만든 list의 값을 1씩 제거 하여 0이 된다면 누적 시간을 DP에 저장한다.
'''

#topological sorting
import heapq

def top_sorting(N, D, graph, parent):
    ret = [0] * (N + 1)
    start = []
    for i, p in enumerate(parent):
        if p == 0:
            start.append(i)

    heap = []
    for s in start:
        heapq.heappush(heap, (D[s-1], s)) # 누적 값, 노드 번호

    while len(heap) != 0:
        time, node = heapq.heappop(heap)
        parent[node] -= 1

        if parent[node] <= 0: # 순서가 됬다면.
            ret[node] = time
            for child in graph[node]:
                heapq.heappush(heap, (time+D[child-1], child))
    return ret

if __name__=="__main__":
    T = int(input())
    for tc in range(T):
        N, K = map(int, input().split()) # N 건물의 갯수, K 규칙의 갯수
        D = list(map(int, input().split())) # 각 건물당 걸리는 시간
        graph = [[] for _ in range(N+1)] # 인접리스트를 이용한 그래프
        parent = [0 for _ in range(N+1)] # 부모의 갯수
        parent[0] = 9999 # 0번은 없는 번호.
        for k in range(K):
            x, y = map(int, input().split())
            graph[x].append(y)
            parent[y] += 1
        W = int(input())

        dp = top_sorting(N, D, graph, parent)
        print(dp[W])