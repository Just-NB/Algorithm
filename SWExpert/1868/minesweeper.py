'''
2
3
..*
..*
**.
5
..*..
..*..
.*..*
.*...
.*...

#1 2
#2 8
'''
'''
012
3x4
567
'''
dr = [-1,-1,-1,0,0,1,1,1]
dc = [-1,0,1,-1,1,-1,0,1]

T = int(input())

for tc in range(1,T+1):
    clickCnt = 1
    size = int(input())
    board = []

    for s in range(size) :
        board.append(input())

    #클릭했으면
    def click(r,c) :
        if isVisit[r][c] == True:
            return 0
        if board[r][c] == '*' :
            isVisit[r][c] = True
            return 0

        isVisit[r][c] = True
        mineCnt = 0

        #8방향 체크
        for i in range(8) :
            nr,nc = r+dr[i],c+dc[i]
            #범위 안에 있고
            if 0<=nr<size and 0<=nc<size :
                #지뢰면
                if board[nr][nc] == '*' :
                    isVisit[nr][nc] = True
                    mineCnt += 1
        # 8방향 지뢰 없으면
        if mineCnt == 0 :
            # 전부 순회
            nBoard[r][c] = 0
            for i in range(8) :
                nr, nc = r + dr[i], c + dc[i]
                # 범위 안에 있고
                if 0 <= nr < size and 0 <= nc < size:
                    click(nr,nc)

        # 지뢰 있으면
        else :
            nBoard[r][c] = mineCnt
        return 1

    ans = 0
    isVisit = [[False for _ in range(size)] for __ in range(size)]
    nBoard = [[0 for _ in range(size)] for __ in range(size)]
    for i in range(size) :
        for j in range(size) :
            ans += click(i,j)
    print(f'#{tc} {ans}')

    for b in nBoard:
        print(b)