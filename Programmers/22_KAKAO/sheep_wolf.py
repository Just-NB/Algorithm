from collections import deque
import copy
tree = []
answer = 0
def make_tree(length:int, edges: list)-> list:
    tree = [[] for _ in range(length)]
    for p, c in edges:
        tree[p].append(c)
    return tree


def dfs(node, sheep, wolf, info, nxt_nodes: list):
    global answer

    sheep += info[node] ^ 1
    wolf += info[node]
    answer = max(answer, sheep)
    if sheep == wolf:
        return
    nxt = copy.deepcopy(nxt_nodes)
    nxt.remove(node)
    nxt.extend(tree[node])
    for n in nxt:
        dfs(n, sheep, wolf, info, nxt)


def solution(info, edges):
    global tree
    # 1. 트리 만들기.
    tree = make_tree(len(info), edges)
    dfs(0, 0, 0, info, [0])
    return answer

print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))