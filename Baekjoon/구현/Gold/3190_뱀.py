import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
for k in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1


class SNAKE:
    def __init__(self):
        self.body = deque()
        self.dir = (0, 1)
        self.body.append([0, 0]) # head / tail
        board[0][0] = 2

    def move(self) -> bool:
        head, tail = self.body[0], self.body[-1]
        nr, nc = head[0] + self.dir[0], head[1] + self.dir[1]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            return False
        if board[nr][nc] == 2:
            return False
        if board[nr][nc] != 1:
            board[tail[0]][tail[1]] = 0
            self.body.pop()

        self.body.appendleft([nr, nc])  # new head
        board[nr][nc] = 2

        return True

    def change_dir(self, d):
        if d == 'D':  # 오른쪽
            self.dir = (self.dir[1] * 1, self.dir[0] * -1)
        elif d == 'L':
            self.dir = (self.dir[1] * -1, self.dir[0] * 1)


snake = SNAKE()
L = int(input())
end_flag = False
answer = 0
for _ in range(L):
    if end_flag:
        break
    x, d = input().split()
    time = int(x) - answer
    for __ in range(time):
        if not snake.move():
            end_flag = True
            break
        answer += 1
    snake.change_dir(d)

if not end_flag:
    while snake.move():
        answer += 1

print(answer + 1)  # 마지막 움직임으로 패배가 확정될 경우 프로그램은 종료된다. 하지만 정답은 마지막 움직임을 포함하므로 1을 더한다.