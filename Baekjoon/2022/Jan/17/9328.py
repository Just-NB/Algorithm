'''
Title   : 열쇠
Level   : G1
Problem : 평면도에 문서의 위치가 나타나있다. 문은 모두 잠겨있기 때문에, 열쇠가 필요하다.
          열쇠를 일부 가지고 있고, 일부는 빌딩의 바닥에 놓여져 있다. 상하좌우로만 이동가능하다
          몇 개 훔칠 수 있는지 작성한다.
          '.' : 빈공간, '*' : 벽, '$' : 문서, 대문자 : 문, 소문자 : 열쇠
          처음에는 빌딩의 밖에 있다, 빌딩 가장자리 벽이 아닌 곳을 통해 안팎을 드나들 수 있다.
          열쇠는 여러 번 사용할 수 있다.
Type    : BFS
'''
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
dr = [(-1, 0), (1, 0), (0, -1), (0, 1)]
keys = 0
def open(door):
    if keys & (1 << ord(door) - 65):
        return True
    else:
        return False


def move(start):
    global keys
    ret = 0
    if board[start[0]][start[1]] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and open(board[start[0]][start[1]]) is False:
        return 0
    if board[start[0]][start[1]] in 'abcdefghijklmnopqrstuvwxyz':
        keys = keys | (1 << ord(board[start[0]][start[1]]) - 97)
    if board[start[0]][start[1]] == '$' and visit[start[0]][start[1]] == -1:
        visit[start[0]][start[1]] = keys
        ret += 1
    q = deque()
    q.append([start[0], start[1]]) # 시작위치.
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i][0], c + dr[i][1]
            if 0 <= nr < R and 0 <= nc < C:
                if visit[nr][nc] >= keys:
                    continue
                if board[nr][nc] == '.':
                    q.append([nr, nc])
                elif board[nr][nc] in 'abcdefghijklmnopqrstuvwxyz':
                    keys = keys | (1 << (ord(board[nr][nc]) - 97))
                    q.append([nr, nc])
                elif board[nr][nc] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    if open(board[nr][nc]):  # 열쇠가 있으면
                        q.append([nr, nc])
                elif board[nr][nc] == '$':
                    if visit[nr][nc] == -1:
                        ret += 1
                    q.append([nr, nc])
                visit[nr][nc] = keys

    return ret


for tc in range(T):
    R, C = map(int, input().split())
    board = [['' for _ in range(C)] for _ in range(R)]
    keys = 0
    ENTER = []  # 입구 후보군
    for r in range(R):
        tmp = input().strip()
        for c, t in enumerate(tmp):
            if r == 0 or r == R - 1:
                if t != '*':
                    ENTER.append([r, c])
            else:
                if c == 0 or c == C - 1:
                    if t != '*':
                        ENTER.append([r, c])
            board[r][c] = t

    KEYS = input().strip()
    if KEYS != '0':
        for k in KEYS:
            # key로 a, b가 들어올 경우  0000 ~ 0011
            keys = keys | (1 << (ord(k) - 97)) # a = 97, 가지고 있는 열쇠.
    visit = [[-1 for _ in range(C)] for _ in range(R)]  # -1 : 초기상태, 0 : key없는 상태로 한번 이동, N : 비트 이용하여 가지고 있는 키의 종류마다 이동여부 확인.
    # 입구를 찾아 이동 시작.
    ans = 0
    e, e_len = 0, len(ENTER)
    cnt = 0
    while cnt < e_len*e_len:
        r, c = ENTER[e][0], ENTER[e][1]
        if visit[r][c] < keys:  # 다른 입구로 들어가서 새로운 키를 발견했다면 다시 들어가볼거임.
            ans += move([r, c])
        e = (e + 1) % e_len
        cnt += 1
    print(ans)



'''
1
5 17
*****************
.............**$*
*C*A*P*B**X*Y*.X.
*p*x*a*y**$*$**$*
*****************
cz

1
7 7
*ABCDE*
X.....F
W.$$$.G
V.$$$.H
U.$$$.J
T.....K
*SQPML*
irony

1
15 15
**$*.**********
****.*******$**
****B.$****b.**
$*****c*****.**
*C$.*****fD..**
*$*xd******.**$
$.C********A.**
**h********.AA.
***************
***.i**********
***.***.K$*****
*k.$$I.$*******
******.$..j***$
*******D*******
****$**F*******
za
a z b c h x d f j 
'''