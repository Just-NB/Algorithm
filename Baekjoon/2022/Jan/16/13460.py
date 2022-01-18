'''
Title   : 구슬 탈출 2
Level   : G1
Problem : 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임이다.
          세로 x 가로 = N x M, 바깥 행과 열을 막혀있고, 구멍은 하나 있다.
          파란구슬이 구멍에 빠지면 안된다.
          왼쪽/오른쪽/아래/위로 기울일 수 있다.
Type    : bfs, 구현
Idea    : 1. 기울이기 : 한개의 구슬을 한칸씩 이동시킨다. 이동시킬 위치에 따라 행동을 결정한다.
          2. 움직일 순서 : LEFT로 움직일때는 col이 더 작은 값인 구슬, RIGHT로 움직일 떄는 col이 더 큰값인 구슬, UP으로 움직일 때는 row가 작은 구슬, DOWN으로 움직일 때는 row가 더 큰 구슬을 먼저 움직인다.
'''

from collections import deque
ROW, COL = map(int, input().split())
board = [['' for _ in range(COL)] for _ in range(ROW)]
visit = [[[[False for _ in range(COL)] for _ in range(ROW)] for _ in range(COL)] for _ in range(ROW)]

B, R, E = [0, 0], [0, 0], [0, 0]
dr = [(0, -1), (0, 1), (-1, 0), (1, 0)]
for r in range(ROW):
    tmp = input()
    for c, t in enumerate(tmp):
        board[r][c] = t
        if t == 'O' :
            E = [r, c]
        if t == 'B':
            B = [r, c]
            board[r][c] = '.'
        if t == 'R':
            R = [r, c]
            board[r][c] = '.'

def pprint():
    for b in board:
        print(b)

def beads_move(first, second, d):
    f = move(first, second, d)
    s = move(second, f, d)
    return f, s


def move(mb, fb, d):
    r, c = mb[0], mb[1]
    #print(mb, fb)
    while True:
        nr, nc = r + dr[d][0], c + dr[d][1]

        if board[nr][nc] == 'O':  # 골인이면 종료
            return [nr, nc]
        elif [nr, nc] == fb:
            return [r, c]
        elif board[nr][nc] == '.':  # 다음칸은 길이 있다.
            r, c = nr, nc
        elif board[nr][nc] == '#':  # 벽이면 이동을 멈춘다.
            return [r, c]


def bfs():
    q = deque()
    q.append([R, B, 0])

    while len(q) != 0:
        r, b, c = q.popleft()
        #print(r, b, c)
        br, bc = b
        rr, rc = r
        if visit[rr][rc][br][bc] is True:
            continue
        visit[rr][rc][br][bc] = True
        if r == E and b != E:
            return c
        if b == E or (r == E and b == E) or c == 10:
            continue

        # LEFT/RIGHT
        if rc < bc: # red가 blue의 왼쪽에 있다면
            # 1. LEFT : RED가 먼저 움직인다.
            left_red, left_blue = beads_move(r, b, 0)
            # 2. RIGHT : BLUE가 먼저 움직인다.
            right_blue, right_red = beads_move(b, r, 1)
        else:
            # 1. LEFT
            left_blue, left_red = beads_move(b, r, 0)
            # 2. RIGHT
            right_red, right_blue = beads_move(r, b, 1)
        # UP/DOWN
        if rr < br: # red가 blue의 위쪽에 있다면
            # 3. UP
            up_red, up_blue = beads_move(r, b, 2)
            # 4. DOWN
            down_blue, down_red = beads_move(b, r, 3)
        else:
            # 3. UP
            up_blue, up_red = beads_move(b, r, 2)
            # 4. DOWN
            down_red, down_blue = beads_move(r, b, 3)

        q.append([left_red, left_blue, c + 1])
        q.append([right_red, right_blue, c + 1])
        q.append([up_red, up_blue, c + 1])
        q.append([down_red, down_blue, c + 1])

    return -1

print(bfs())