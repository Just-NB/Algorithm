H,W = 0,0
dx = [[1,0],[1,1],[-1,0],[0,1]]
dy = [[0,1],[0,1],[1,1],[1,1]]


def solution(board) :
    ret = 0
    isFinish = True
    x,y = 0,0
    for i,b in enumerate(board) :
        if isFinish == False : break
        for j,v in enumerate(b) : 
            if v == '.' :
                isFinish = False
                x,y = j,i
                break
    
    if isFinish : 
        return 1
    
    for d in range(4) :
        x0,y0 = dx[d][0],dy[d][0]
        x1,y1 = dx[d][1],dy[d][1]
        nxtX0,nxtY0 = x+x0,y+y0
        nxtX1,nxtY1 = x+x1,y+y1
        try :
            if nxtX0 < 0 : continue
            if board[nxtY0][nxtX0] == '.' and board[nxtY1][nxtX1] == '.' :
                board[y][x] = board[nxtY0][nxtX0] = board[nxtY1][nxtX1] = '@'
                ret += solution(board)
                board[y][x] = board[nxtY0][nxtX0] = board[nxtY1][nxtX1] = '.'
        except :
            continue

    return ret


if __name__ == '__main__' :
  C = int(input())
  for _ in range(C) :
        BOARD = list()
        H,W = list(map(int,input().split()))
        for __ in range(H) :
            BOARD.append(list(input()))
        print(solution(BOARD))