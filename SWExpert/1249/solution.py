from queue import Queue

T = int(input())

for tc in range(1,T+1) :
    result = 0
    mapSize = int(input())
    startPos = [0, 0]
    goalPos = [mapSize-1, mapSize-1]
    MAP = [[0 for _ in range(mapSize)] for __ in range(mapSize)]
    DP = [[90000 for _ in range(mapSize)] for __ in range(mapSize)]
    for i in range(mapSize) :
        tmp = input()
        for j in range(mapSize) :
            MAP[i][j] = int(tmp[j])
    #bfs
    dr = [-1,1,0,0] #상하 좌우
    dc = [0,0,-1,1]
    pos = Queue()
    DP[0][0] = 0
    pos.put(startPos)
    while not pos.empty() :
        cur = pos.get()
        for i in range(4) :
            nxtR = cur[0] + dr[i]
            nxtC = cur[1] + dc[i]
            if 0 <= nxtR < mapSize and 0 <= nxtC < mapSize :
                if DP[nxtR][nxtC] > DP[cur[0]][cur[1]] + MAP[nxtR][nxtC] :
                    DP[nxtR][nxtC] = DP[cur[0]][cur[1]] + MAP[nxtR][nxtC]
                    pos.put([nxtR, nxtC])
    print(f'#{tc} {DP[mapSize-1][mapSize-1]}')