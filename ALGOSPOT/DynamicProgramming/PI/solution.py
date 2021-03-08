T = int(input())
N,M,X,Y = 0,0,0,0
#K = 2 4 1
#몇칸 움직일까?
def movecnt(rot, cnt) :
    global cur
    for i in range(cnt) :
        if rot == 1:
            cur = (cur-1)%klen
        else :
            cur = (cur+1)%klen
    return K[cur]
def isWall(x,y) :
    if y < 0 or x < 0 or y >= M or x >= N :
        return False
    if MAP[y][x] == -1 :
        return False

    return True
#S 1 2
#N 2 1
#E 2 5
def move(dir, rot, cnt) :
    global Y,X
    rot = int(rot)
    cnt = int(cnt)
    score = MAP[Y][X]
    MAP[Y][X] = 0
    num = movecnt(rot,cnt)
    for i in range(num) :
        if dir == 'N' :
            if isWall(X,Y-1) :
                Y=Y-1
                score += MAP[Y][X]
            else :
                break
        elif dir == 'S':
            if isWall(X,Y+1) :
                Y=Y+1
                score += MAP[Y][X]
            else :
                break
        elif dir == 'W':
            if isWall(X-1,Y) :
                X=X-1
                score += MAP[Y][X]
            else :
                break
        else :
            if isWall(X+1,Y) :
                X=X+1
                score += MAP[Y][X]
            else :
                break
        MAP[Y][X] = 0
    return score

for i in range(T) :
    answer = 0
    N, M, X, Y = map(int, input().split())
    X-=1
    Y-=1
    MAP = []
    for _ in range(M):
        MAP.append(list(map(int, input().split())))
    #안써도됨
    klen = int(input())
    #돌림판
    K = list(map(int, input().split()))
    cur = 0
    L = int(input())
    #명령어
    command = []
    for _ in range(L) :
        command.append(input().split())

    for c in command :
        answer += move(c[0],c[1],c[2])
    print('#{} {} {} {}'.format(i+1,answer,X+1,Y+1))