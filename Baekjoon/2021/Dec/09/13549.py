'''
Title   : 숨바꼭질 3
Level   : G5
Problem : 수빈이는 점 N, 동생은 점 K에 있다.
          수빈이는 걷거나 순간이동을 할 수 있다.
          1. 걷기 : 수빈이의 위치가 X일때 1초후 X-1 or X+1로 이동할 수 있다
          2. 순간이동 : 수빈이의 위치가 X일때 0초 후에 2*X로 이동할 수 있다
          수빈이와 동생의 위치가 주어졌을 떄, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지를 구하는 프로그램을 작성한다.
Type    : 완전탐색, bfs
Idea    : 1. 100,000크기의 리스트를 사용하여 해당 위치에 방문여부를 저장한다.
          2. bfs를 통해 먼저 방문했다면, 다른 지점을 방문해서 도착한것보다 빠른것을 보장할 수 있다.

'''
from collections import deque

N, K = map(int, input().split())
bfs = deque()
bfs.append([N, 0])
visit = [0] * 100001
while len(bfs) != 0:
    cur, time = bfs.popleft() # 현재 위치/ 시간
    if cur == K:
        print(time)
        break
    else:
        if cur * 2 <= 100000 and visit[cur*2] == 0:
            bfs.append([cur*2, time])
            visit[cur * 2] = 1
        if cur-1 >= 0 and visit[cur-1] == 0:
            bfs.append([cur-1, time+1])
            visit[cur - 1] = 1
        if cur+1 <= 100000 and visit[cur+1] == 0:
            bfs.append([cur+1, time+1])
            visit[cur + 1] = 1