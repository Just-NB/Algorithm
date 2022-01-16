'''
Title   : 바이러스
Level   : S3
Problem : 한 컴퓨터가 바이러스에 걸리면 네트워크 상에 연결되어있는 바이러스에 모두 감염된다.
          컴퓨터 수와 네트워크 상에서 연결된 정보가 주어질 때, 1번 컴퓨터를 통해 바이러스에 감염되는 컴퓨터의 수를 출력
Type    : 그래프, bfs
Idea    : 1. 주어진 정보를 그래프로 만든다.
          2. 그래프를 bfs탐색한다.
'''
from collections import deque
N = int(input()) # 컴퓨터 수
M = int(input()) # 네트워크 연결 수

graph = [[] for _ in range(N+1)] # 각 배열안의 값은 연결되어있는 컴퓨터 번호
for m in range(M):
    s, d = map(int, input().split())
    graph[s].append(d)
    graph[d].append(s)

#print(graph)
visit = [False for _ in range(N+1)] # 각 컴퓨터에 방문했는지 여부.
visit[0] = True
visit[1] = True
bfs = deque()
bfs.append(1)

answer = 0
while len(bfs) != 0:
    num = bfs.popleft()
    for n in graph[num]:
        if visit[n] is False:
            visit[n] = True
            bfs.append(n)
            answer += 1

print(answer)

