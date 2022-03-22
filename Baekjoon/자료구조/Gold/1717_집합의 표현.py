import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]

def union(p: int, c: int):
    parent[find(c)] = find(p)

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

for m in range(M):
    q, a, b = map(int, input().split())
    if q == 0:
        union(a, b)
    else:
        print("YES" if find(a) == find(b) else "NO")

# Time out
# def BFS(start, end):
#     visit = [False for _ in range(N + 1)]
#     visit[start] = True
#     bfs = deque()
#     bfs.append(start)
#     while bfs:
#         node = bfs.popleft()
#         if node == end:
#             return True
#         for n in graph[node]:
#             if visit[n]: continue
#             bfs.append(n)
#             visit[n] = True
#     return False

# for m in range(M):
#     q, a, b = map(int, input().split())
#     if q == 0:
#         graph[a].append(b)
#         graph[b].append(a)
#     else:
#         flag = BFS(a, b)
#         print("YES" if flag else "NO")

# Memory Out
# import sys
# from collections import deque
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# graph = [set([i]) for i in range(N + 1)]
#
# def BFS(start, end):
#     visit = [False for _ in range(N + 1)]
#     visit[start] = True
#     bfs = deque()
#     bfs.append(start)
#     while bfs:
#         node = bfs.popleft()
#         if node == end:
#             return True
#         for n in graph[node]:
#             if visit[n]: continue
#             bfs.append(n)
#             visit[n] = True
#     return False
#
# for m in range(M):
#     q, a, b = map(int, input().split())
#     if q == 0:
#         for n in graph[a]:
#             graph[b].add(n)
#         for n in graph[b]:
#             graph[a].add(n)
#         # graph[a].add(list(graph[b]))
#         # graph[b].add(list(graph[a]))
#     else:
#         print("YES" if b in graph[a] else "NO")
