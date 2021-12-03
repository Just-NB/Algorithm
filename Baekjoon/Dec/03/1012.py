'''
Title   : 유기농 배추
Level   : S2
Problem : 해충을 보호하기 위한 지렁이를 구입했다. 이 지렁이는 배추 근처에 서식하며 해충을 잡아먹는다.
          어떤 배추에 지렁이가 한 마리라도 살고 있으면 인접한 다른 배추로 이동할 수 있고, 보호받을 수 있따
          한 배추의 상하좌우 네 방향이 인접해 있는 것이다.
          배추들이 몇 군데에 퍼져있는지 조사하여 필요한 지렁이 양을 구한다.
Type    : bfs
Idea    : 1. 반복문을 통해 모든 배열을 순회한다.
          2. 현재 값이 1이고 방문한 적이 없다면, bfs를 통해 상하좌우를 순회하며 인접한 배추를 찾는다.
          3. visit배열을 통해 방문여부를 체크한다.
          4. 2~3을 반복한다.
'''
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

dr, dc = (-1,1,0,0), (0,0,-1,1)
for tc in range(T):
    C,R,K = map(int, input().split())
    board = [[0 for _ in range(C)] for __ in range(R)]
    visit = [[False for _ in range(C)] for __ in range(R)]
    answer = 0
    for k in range(K) :
        c, r = map(int, input().split())
        board[r][c] = 1

    bfs = deque()
    for r in range(R):
        for c in range(C):
            if board[r][c] == 1 and visit[r][c] is False:
                answer += 1
                bfs.append([r, c])
                visit[r][c] = True
                while len(bfs) != 0:
                    cur_r, cur_c = bfs.pop()
                    for i in range(4):
                        nr, nc = cur_r + dr[i], cur_c + dc[i]
                        if 0 <= nr < R and 0 <= nc < C:
                            if board[nr][nc] == 1 and visit[nr][nc] is False:
                                bfs.append([nr, nc])
                                visit[nr][nc] = True

    print(answer)