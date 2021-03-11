'''
4×4 크기의 격자판이 있다. 격자판의 각 격자칸에는 0부터 9 사이의 숫자가 적혀 있다.

격자판의 임의의 위치에서 시작해서, 동서남북 네 방향으로 인접한 격자로 총 여섯 번 이동하면서, 각 칸에 적혀있는 숫자를 차례대로 이어 붙이면 7자리의 수가 된다.

이동을 할 때에는 한 번 거쳤던 격자칸을 다시 거쳐도 되며, 0으로 시작하는 0102001과 같은 수를 만들 수도 있다.

단, 격자판을 벗어나는 이동은 가능하지 않다고 가정한다.

격자판이 주어졌을 때, 만들 수 있는 서로 다른 일곱 자리 수들의 개수를 구하는 프로그램을 작성하시오.


1
1 1 1 1
1 1 1 2
1 1 2 1
1 1 1 1

#1 23

'''
from queue import Queue
def bfs(r,c) :
    numQueue.put([board[r][c], [r,c], 1])

    while numQueue.qsize() :
        cur = numQueue.get()
        if cur[2] == 8 :
            numSet.add(cur[0])
               # print(numLst)
        else :
            numstr = cur[0]+board[cur[1][0]][cur[1][1]]
            for i in range(4) :
                nxtR = cur[1][0] + dirR[i]
                nxtC = cur[1][1] + dirC[i]
                if 0 <= nxtR < 4 and 0 <= nxtC < 4 :
                    numQueue.put([numstr  ,[nxtR,nxtC], cur[2]+1])


T = int(input())
#동 서 남 북
dirR = [-1,1,0,0]
dirC = [0,0,1,-1]
for tc in range(T) :
    numSet = set()
    numQueue = Queue()
    board = []
    result = 0
    for i in range(4) :
        board.append(input().split())
    for r in range(4) :
        for c in range(4) :
            bfs(r,c)
    result = len(numSet)
    print(f'#{tc+1} {result}')

'''
1 1 1 1
1 1 1 2
1 1 2 1
1 1 1 1
'''