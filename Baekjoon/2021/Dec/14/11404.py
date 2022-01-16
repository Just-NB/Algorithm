'''
Title   : 플로이드
Level   : G4
Problem : N개의 도시가 있다. 한 도시에서 출발하여 다른 도시에 도착하는 m개의 버스가 있다.
          버스는 한 번 사용할 떄 필요한 비용이 있다.
          모든 쌍 (A,B)에 대해 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성한다.
Type    : 플로이드 와샬, 다이나믹 프로그래밍
Idea    : 1. A -> B로 이동할 떄, Cost가 가장 적은 것만 board에 저장한다.
          2. A -> B로 이동할 떄, K도시를 거쳐서 가는 경우가 더 저렴할 때, 값을 갱신한다.
          3. dp[A][B] > dp[A][K] + dp[K][B] 일 경우 값 갱신
'''
import math

N = int(input())
M = int(input())
board = [[math.inf for _ in range(N+1)] for __ in range(N+1)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    if board[a][b] > cost:
        board[a][b] = cost
floyd = [[0 for _ in range(N+1)] for __ in range(N+1)]


for temp in range(1, N+1): # temp : 거쳐가는 도시
    board[temp][temp] = 0
    for start in range(1, N+1): # start : 출발지
        for dest in range(1, N+1): # dest : 목적지
            trans = board[start][temp] + board[temp][dest]
            if board[start][dest] > trans :
                board[start][dest] = trans

for b in board[1:]:
    for answer in b[1:]:
        if answer == math.inf:
            answer = 0
        print(answer, end=' ')
    print()
