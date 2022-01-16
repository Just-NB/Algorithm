'''
Title   : 트리의 부모 찾기
Level   : S2
Problem : 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라 정했을때, 각 노드의 부모를 구하는 프로그램을 작성한다.
Type    : 트리, bfs
Idea    : 1. 노드의 갯수를 길이로 하는 리스트를 만든다.
          2. 각 idx를 노드의 번호로 하고, 값을 연결된 노드들로 한다.
          3. bfs를 통해 연결된 노드들을 순회하며, 부모의 정보를 함께 넘긴다.
'''
from collections import deque
N = int(input())
nodes = [[] for _ in range(N+1)]
answer = [1 for _ in range(N+1)]
visit = [False for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

bfs = deque()
bfs.append([1,1]) # 자식 idx, 부모 idx
visit[1] = True
while len(bfs) != 0:
    child, par = bfs.popleft()
    answer[child] = par
    for node in nodes[child]:
        if visit[node] is False:
            bfs.append([node, child])
            visit[node] = True

for a in answer[2:]:
    print(a)
