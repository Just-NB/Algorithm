'''
Level   : S3
Problem : 친구와 짝을 지어 춤을 추고 싶다.
          친구 관계도가 주어졌을때, 최대 몇명이 짝을 지을수 있는지 출력한다.
Idea    : 1. 친구 관계도를 통해 그래프를 그린다.
          2. 완전탐색을 통해, 친구들을 한 쌍씩 맺어준다.
'''

n, m = map(int, input().split())
graph = [[] for __ in range(n)]
visit = [False for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if u > v:
        u, v = v, u
    graph[u].append(v)


def dfs(idx, match):
    if idx == n:  # 한칸씩 진행하므로, idx가 n이면 종료.
        return match
    if visit[idx] is True: # 이미 매칭된 친구면 다음친구 확인.
        return dfs(idx+1, match)
    ret = 0
    for friend in graph[idx]:
        if visit[friend] is False:
            visit[friend] = True
            ret = max(ret, dfs(idx + 1, match + 1))
            visit[friend] = False
    return max(ret, dfs(idx+1, match))


answer = dfs(0, 0) * 2
print(answer+1 if n > answer else answer)
