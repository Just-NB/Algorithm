'''
Title   : 숨바꼭질
Level   : S1
Problem : 수빈이는 N위치에 있고, 동생은 K에 있다. 수빈이는 걷거나 순간이동을 할 수있다.
          걸을땐 1초 후 X+1/X-1 로 이동하고, 순간이동할 경우 1초 후 2*X로 이동한다.
          수빈이와 동생의 위치를 알 때, 가장 빨리 찾는 시간을 구한다.
Type    : BFS
Idea    : 1. 이동을 통해 가장 멀리 갈 수 있는 곳은 20만으로 한정한다.(동생의 위치가 최대 10만까지)
          2. visit 배열을 이용하여 재방문을 막는다.
          3. X-1,X+1,X*2가 범위내에 있다면 BFS탐색한다.
'''
import math
from collections import deque
N, M = map(int, input().split())
visit = [False for _ in range(200000)]
bfs = deque()
bfs.append([N, 0])
while len(bfs) != 0:
    cur, step = bfs.popleft()
    if cur == M:
        print(step)
        break

    if cur - 1 >= 0 and visit[cur-1] is False:
        bfs.append([cur-1, step+1])
        visit[cur-1] = True
    if cur + 1 < 200000 and visit[cur+1] is False:
        bfs.append([cur+1, step+1])
        visit[cur+1] = True
    if cur*2 < 200000 and visit[cur*2] is False:
        bfs.append([cur*2, step+1])
        visit[cur*2] = True