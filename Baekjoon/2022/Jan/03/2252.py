'''
Title   : 줄 세우기
Level   : G3
Problem : N명의 학생들을 키 순서대로 줄을 세운다.
          두 학생의 키를 비교하며, 모든 학생을 다 비교하지 않는다
          일부 학생들의 키를 비교한 결과가 주어졌을 때, 주을 세우는 프로그램을 작성한다.
Type    : 위상정렬
Idea    : 1. 각 노드에 연결되어있는 부모의 갯수를 저장하는 list를 만든다.
          2. 노드에 연결되어 있는 부모가 0인 노드부터 순회를 시작한다.
          3. 현재 노드와 연결되어 있는 자식노드들을 Queue에 넣는다.
          4. 각 노드에 방문했을 때마다 1에서 만든 list의 값을 1씩 제거 하여 0이 된다면 누적 시간을 DP에 저장한다.
'''
import heapq

def topol_sort(graph, parent):
    heap = []
    ret = []
    for i, p in enumerate(parent):
        if p == 0 :
            heapq.heappush(heap, i)
    while heap:
        node = heapq.heappop(heap)
        parent[node] -= 1
        if parent[node] <= 0:
            ret.append(str(node))
            for n in graph[node]:
                heapq.heappush(heap, n)

    return ' '.join(ret)



if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    parent = [0 for _ in range(N+1)]
    parent[0] = 9999
    for m in range(M):
        a, b = map(int, input().split())
        graph[a].append(b) # a > b
        parent[b] += 1
    print(topol_sort(graph, parent))