'''
Title   : 스도쿠
Level   : G4
Problem : 9x9 크기의 보드가 있을 때, 각 행과 각 열, 그리고 9개의 3x3 크기의 보드에 1~ 9까지의 숫자가 중복없이 나타나도록 보드를 채운다.
          하다 만 스도쿠 퍼즐이 주어졌을 떄, 마저 끝내는 프로그램을 작성한다.
Type    : 백트래킹, dfs
Idea    : 1. 9x9크기의 모든 칸을 확인한다.
          2. row,col위치의 값이 0이면 사용하지 않은 숫자중 하나를 적고 다음칸으로 이동한다
          3. 사용하지 않은 숫자 체크
          3-1. 가로/세로 : row 혹은 col을 고정후, 반복문을 이용하여 9칸을 확인한다
          3-2. 3x3 보드 : (row,col)//3 * 3에서 시작하여 2중반복문을 이용하여 9칸을 확인한다.
'''

board = []
for _ in range(9):
    tmp = input()
    lst = [0]*9
    for i, t in enumerate(tmp):
        lst[i] = int(t)
    board.append(lst)

def check(num, row, col):
    # 가로/ 세로 체크
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    r, c = row//3 * 3, col//3 * 3
    for i in range(3):
        for j in range(3):
            if board[r+i][c+j] == num:
                return False
    return True


def dfs(row, col):
    if row == 9: # 종료조건,
        for i in range(9):
            for j in range(9):
                print(board[i][j],end ='')
            print()

        return True
    ret = False
    if board[row][col] != 0: # 이미 채워져 있다면 다음칸 채우기
        if col != 8:
            ret = dfs(row, col+1)
        else:
            ret = dfs(row+1, 0)
    else:
        for i in range(1,10):
            if ret is True:
                return ret
            if check(i, row, col) is True: #숫자 i가 입력 가능한 위치라면
                if col != 8:
                    board[row][col] = i
                    ret = dfs(row, col+1)
                    board[row][col] = 0
                else:
                    board[row][col] = i
                    ret = dfs(row+1, 0)
                    board[row][col] = 0
    return ret


dfs(0,0)
