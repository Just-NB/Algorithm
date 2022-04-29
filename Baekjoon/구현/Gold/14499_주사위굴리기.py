class Dice:
    def __init__(self):
        self.t = 0
        self.b = 5
        self.w = 3
        self.e = 2
        self.f = 4
        self.r = 1
        self.val = [0, 0, 0, 0, 0, 0]

    def move(self, d: int) -> int:
        tmp = self.t
        if d == 1:      # 동
            self.t = self.w  # w에 있던 값이 top이 된다.
            self.w = self.b
            self.b = self.e
            self.e = tmp
        elif d == 2:    # 서
            self.t = self.e
            self.e = self.b
            self.b = self.w
            self.w = tmp
        elif d == 3:    # 북
            self.t = self.f
            self.f = self.b
            self.b = self.r
            self.r = tmp
        else:           # 남
            self.t = self.r
            self.r = self.b
            self.b = self.f
            self.f = tmp

        return self.val[self.t]  # top에 적혀 있는 값 반환

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
query = list(map(int, input().split()))
dice = Dice()
dr = [[], [0, 1], [0, -1], [-1, 0], [1, 0]] # 동 서 북 남
dice.val[dice.b] = board[x][y]
for i, q in enumerate(query):
    nx, ny = x + dr[q][0], y + dr[q][1]
    if 0 <= nx < N and 0 <= ny < M:
        print(dice.move(q))
        if board[nx][ny] == 0:
            board[nx][ny] = dice.val[dice.b]
        else:
            dice.val[dice.b] = board[nx][ny]
            board[nx][ny] = 0
        x, y = nx, ny