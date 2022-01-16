'''
Title   : 트리의 지름
Level   : G4
Problem : 트리는 사이클이 없는 무방향 그래프이다.
          어떤 두 노드를 선택해서 양쪽으로 짝 당길 때, 가장 길게 늘어나는 경우, 그 경로의 길이를 트리의 지름이라고 한다
          트리의 지름을 구해서 출력하는 프로그램을 작성한다.
Type    : dfs
Idea    : 1. 1번의 dfs를 통해 루트에서 가장 경로가 긴 노드를 찾는다.
          2. 가장 경로가 긴 노드를 루트로 하여 dfs를 통해 가장 경로가 긴 노드를 찾는다.
          3. 트리는 인접리스트 그래프로 표현한다.
'''
import sys
sys.setrecursionlimit(100000)
N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N):
    info = list(map(int, input().split()))
    node = info[0]
    idx = 1
    while idx < len(info)-2:
        tree[node].append([info[idx], info[idx+1]])
        idx += 2


def dfs(idx, dist):
    '''
    최대 깊이와 그 노드 번호를 구한다.
    :param idx: 현재 방문하고 있는 노드의 번호
    :param dist: 시작노드 ~ 현재 방문하고 있는 노드까지의 거리
    :return: [dist, idx], dist가 최대인 것을 반환.
    '''
    ret = [dist, idx] #Distance, Node
    for node, d in tree[idx] :
        if visit[node] is False:
            visit[node] = True
            tmp = dfs(node, dist+d)
            if ret[0] < tmp[0]:
                ret = tmp
    return ret

visit = [False for _ in range(N+1)]
visit[1] = True
start = 1
dist, start = dfs(1, 0)

visit = [False for _ in range(N+1)]
visit[start] = True
dist, start = dfs(start, 0)
print(dist)
