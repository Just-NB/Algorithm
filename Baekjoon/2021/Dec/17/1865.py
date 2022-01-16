'''
Title   : 웜홀
Level   : G3
Problem : N개의 지점이 있고, M개의 도로, W개의 우머홀이 있다.(웜홀은 방향이 있다.)
          웜홀은 시작 위치에서 도착위치로 가는 하나의 경로이다.
          웜홀을 통과하면 시간이 뒤로가게 된다.
          한 지점에서 출발하여 시간여행을 시작하여, 다시 출발지점으로 돌아왔을때
          시간이 되돌아가 있는 경우가 있는지 구하는 프로그램을 작성한다.
Type    : 벨만-포드 알고리즘
Idea    : 1. 가장 짧은 cost를 갖는 도로와 웜홀들로만 도시를 연결한다.
          2. 벨만-포드 알고리즘을 통해 음수 사이클이 있는지 확인한다.
          3. 모든 도로에 대해, 출발지 -> 해당 도로를 거쳐 목적지로 갈때 cost가 작으면 table을 수정한다.
          4. 3번을 V-1번 반복한다.
          5. 3번 과정을 한번 더 반복했을 때, table이 수정된다면 음수 사이클이 존재한다.
          6. 음수 사이클이 하나라도 존재한다면 시간이 되돌아가는 경우가 있다.
'''
import math

T = int(input())
for tc in range(T):
    N, M, W = map(int, input().split())
    edge = []
    for m in range(M):
        s, e, t = map(int, input().split())
        edge.append([s, e, t])
        edge.append([e, s, t])
    for w in range(W):
        s, e, t = map(int, input().split())
        edge.append([s, e, -t])

    cost = [10000*200+1 for _ in range(N+1)]
    flag = False
    for v in range(N-1): # V번 반복
        for j in range(len(edge)): # 모든 도로에 대해
            s, e, t = edge[j]
            if cost[s] + t < cost[e] :
                cost[e] = cost[s]+t
    for j in range(len(edge)): # 모든 도로에 대해
        s, e, t = edge[j]
        if cost[s] + t < cost[e] :
            flag = True

    if flag is True:
        print("YES")
    else:
        print("NO")