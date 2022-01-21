'''
Title   : 사회망 서비스(SNS)
Level   : G3
Problem : 사회망에서 사람들의 친구 관계는 그래프로 표현된다. 두 정점을 잇는 엣지는 친구 관계임을 표현한다.
          사회망 서비스에 속한 사람들은 얼리 어답터이거나 얼리어답터가 아니다.
          얼리어답터가 아닌 사람은 모든 친구가 얼리어답터일때 아이디어를 수용한다.
          가능한 최소의 수의 얼리 어답터를 확보하여 모든 사람이 아이디어를 받아들이게 할때, 최소 얼리어답터의 수를 구한다.
Type    : 다이나믹 프로그래밍, dfs
Idea    : 1. DP[node][0/1] 2차원 배열로 다이나믹 프로그래밍을 계획한다. node번째 사람이 얼리어답터 이거나 아닐때, 다른 사람들이 얼리어답터가 될 최소수
          2. DP[node][0]  : node사람이 얼리어답터 일때, DP[node][1] : node사람이 얼리어답터가 아닐때.
          3. node번 사람이 얼리어답터 일때, node번 사람과 연결된 다른 사람들은 얼리어답터이거나, 아니어도 된다
          4. node번 사람이 얼리어답터가 아닐때, node번 사람과 연결된 다른사람들은 얼리어답터여야 한다.
'''

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N + 1)]
visit = [False for _ in range(N + 1)]
dp = [[0, 0] for _ in range(N + 1)]

for n in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)  # root 가 어딘지 모르므로 걍 다 연결한다.
    graph[v].append(u)

def dfs(node):
    visit[node] = True
    dp[node][0] = 1  # node가 얼리어답터일 경우
    for n in graph[node]:
        if visit[n] is False:
            dfs(n)
            dp[node][0] += min(dp[n][0], dp[n][1])
            dp[node][1] += dp[n][0]

dfs(1)
print(min(dp[1][0], dp[1][1]))


# def dfs(root, node, check):
#     if graph[node] == [root] and visit[root] is True:  # 단말노드일 경우
#         #print(root, node, check, "leaf")
#         # 종료할것입니다.
#         if check is False:  # 부모가 얼리어답터가 아니면 반드시 본인은 얼리어답터여야 한다.
#             return 1
#         else:  # 부모가 얼리어답터가 이면 본인은 얼리어답ㅇ터일 필요가 없다.
#             return 0
#
#     if visit[node] is True:  # 이미 방문한 노드는 확인할 필요가 없다.
#         return 0
#
#     visit[node] = True  # 현재 노드 확인 완료.
#     ret = 0
#     # 부모가 얼리어답터이면 본인은 얼리어답터 이거나/아니거나
#     if check is True:
#         on, off = 1, 0
#         for n in graph[node]:
#             on += dfs(node, n, True)
#             off += dfs(node, n, False)
#         ret = min(on, off)
#     # 부모가 얼리어답터가 아니면 본인은 반드시 얼리어답터여야 한다.
#     if check is False:
#         ret = 1
#         for n in graph[node]:
#             ret += dfs(node, n, True)
#
#     visit[node] = False
#     return ret
#
#
# print(dfs(0, 1, True))
