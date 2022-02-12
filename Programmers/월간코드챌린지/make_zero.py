import sys
sys.setrecursionlimit(10**6)

tree = []
answer = 0


def dfs(a, node, parent):
    global answer
    val, child = a[node], tree[node]
    for c in child:
        if c == parent: continue
        val += dfs(a, c, node)
    answer += abs(val)
    return val


def solution(a, edges):
    global tree
    if sum(a) != 0: return -1
    tree = [[] for val in a]  # node : val(int), child(list)
    for u, v in edges:
        tree[u].append(v)  # 양 방향 연결
        tree[v].append(u)

    dfs(a, 0, 0)
    return answer


print(solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]), ' : 9')


'''
첫번째 버전.
def dfs(node):
    global answer
    val, child = tree[node]
    if len(child) == 1 and visit[child[0]] is True:
        answer += abs(val)
        return val

    visit[node] = True
    for c in child:
        if visit[c] is True:
            continue
        val += dfs(c)
    answer += abs(val)
    return val


def solution(a, edges):
    global tree, visit
    if sum(a) != 0: return -1
    tree = [[val, []] for val in a]  # node : val(int), child(list)
    for u, v in edges:
        tree[u][1].append(v)  # 양 방향 연결
        tree[v][1].append(u)

    visit = [False for _ in range(len(a))]  # 방문 여부 확인, 중복방문 방지.
    dfs(0)
    return answer
'''