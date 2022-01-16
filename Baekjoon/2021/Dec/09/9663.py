'''
Title   : N-Qeen
Level   : G5
Problem : NxN 크기의 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
          N이 주어졌을 때, 퀸을 놓는 방법이 수를 구하는 프로그램을 작성한다.
          퀸은 가로/세로/대각선을 모두 이동한다.
Type    : 백트래킹, 완전탐색
Idea    : 1. dfs탐색으로 1row씩 퀸을 놓는다.
          2. [r,c] 좌표에 퀸을 놓을 때, 가로/세로/대각선에 다른 퀸이 있는지 확인한다.
          3. 위에서 아래로 퀸을 놓기 때문에 가로는 확인하지 않아도 된다.
          4. 위에서 아래로 퀸을 놓기 때문에 r열 이후는 확인하지 않아도 된다.
          4-1. idx가 col을 의미하는 리스트를 만들어, 윗행에 퀸이 있는지 여부를 체크한다.
          4-2. https://developnote.tistory.com/70 참고
          5. \ 대각선 : r,c <= 0 일 때까지 [r-1 , c-1]에 퀸이 있는지 확인
          6. / 대각선 : r,c >N 일 때까지 [r-1, c+1]에 퀸이 있는지 확인
'''

N = int(input())
board = [[False for _ in range(N)] for __ in range(N)]
visit_col = [False for _ in range(N)]
def is_valid(row, col):
    for r in range(row):
        if col + r - row >= 0 : #\ 대각선
            if board[r][col+r-row] is True:
                return False
        if col - r + row < N : # / 대각선
            if board[r][col-r+row] is True:
                return False
    return True
def dfs(row) :
    if row == N:
        return 1
    ans = 0
    for c in range(N): # 가로 확인
        if visit_col[c] is True:
            continue

        if is_valid(row, c):
            board[row][c] = True
            visit_col[c] = True
            ans += dfs(row+1)
            board[row][c] = False
            visit_col[c] = False
    return ans

print(dfs(0))
