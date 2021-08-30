import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
items = list(map(int, input().split()))
graph = [[99999 for _ in range(N)] for __ in range(N)]

for _ in range(R):
    a, b, l = map(int, input().split())
    graph[a-1][b-1] = l
    graph[b-1][a-1] = l

for i in range(N):
    graph[i][i] = 0

# Floyd-Warshall
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

answer= [0 for _ in range(N)]
# Find a zone to maximize items
for i in range(N):
    for j in range(N):
        if graph[i][j] <= M:
            answer[i] += items[j]
print(max(answer))
