'''
Tree : 순환이 없는 그래프
따라서 하나의 간선을 지운다면 연결되어있던 두 노드를 루트로 한 두개의 Tree를 만들 수 있다.
'''
graph = []
visit = []
def dfs(node):
    ret = 1
    visit[node] = True
    for n in graph[node]:
        if visit[n] is False:
            ret += dfs(n)

    return ret

def solution(n, wires):
    global graph, visit
    answer = 9999999
    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for a, b in wires:
        visit = [False for _ in range(n + 1)]
        graph[a].remove(b)
        graph[b].remove(a)
        answer = min(abs(dfs(a) - dfs(b)), answer)
        graph[a].append(b)
        graph[b].append(a)
    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]), '3')
print(solution(4, [[1, 2], [2, 3], [3, 4]]), '0')
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]), '1')