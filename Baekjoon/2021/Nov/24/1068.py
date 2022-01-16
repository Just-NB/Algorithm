'''
Title   : 트리
Level   : G5
Problem : 트리의 노드 개수 N과 노드들의 부모 정보, 지울 노드의 번호가 주어진다.
          주어진 노드를 지웠을 때, 단말 노드의 개수를 출력한다.
Type    : 트리, 구현
Idea    : 1. 지워질 노드는 부모를 -2를 가리키게 한다.
          2. 부모노드 정보를 통해 자식노드 정보를 갖는 리스트를 만든다.
          3. 루트노드에서 시작하여 dfs탐색후, 더이상 자식노드가 없으면 리프 노드 개수에 +1한다.
'''
N = int(input())
parents = list(map(int, input().split()))
del_node = int(input())
parents[del_node] = -2
root = -1
child = [[] for _ in range(N)]
for i, p in enumerate(parents):
    if p == -1:
        root = i
    if p != -1 and p != -2:
        child[p].append(i)


def dfs(idx):
    if idx == -1: # 루트를 지웠을 때,
        return 0
    if len(child[idx]) == 0:
        return 1
    ret = 0
    for c in child[idx]:
        ret += dfs(c)
    return ret

print(dfs(root))