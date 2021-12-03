'''
Title   : 색종이 만들기
Level   : S3
Problem : 여러개의 정사각형칸들로 이루어진 정사각형 모양의 종이가 있다.
          정사각형은 하얀색/파란색으로 칠해져있다.
          규칙에 따라 잘라서 다양한 크기를 가진 정사각형 모양의 하얀색/파란색 종이를 만들려한다.
          전체종이가 같은색이 아닐경우 4등분한다.
          4등분한 종이들도 마찬가지로 진행하여, 더이상 자를 수 없을 때까지 반복한다.
          모든 작업이 끝나고, 파란색/하얀색 종이의 갯수를 구하는 프로그램을 작성한다.
Type    : 재귀, 분할정복
Idea    : 1. 분할 필요 여부는 시작지점/종료지점까지의 숫자를 모두 더한 값이 0이거나, 해당 영역의 크기가 같으면 필요가 없다.
          2. 분할이 필요한 구역일 경우, 왼쪽/오른쪽 위/아래 크기를 4등분하여 재귀적인 방법으로 분할한다.
'''

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

def flag(start, end):
    """
    종이를 잘라야 하는지 구분한다.
    :param start: [row, col]
    :param end: [row, col]
    :return: True(잘라야 한다)/False(자르지 않는다)
    """
    cnt = 0
    size = (end[0] - start[0]+1) * (end[1] - start[1]+1)
    for i in range(start[0], end[0]+1):
        for j in range(start[1], end[1]+1):
            cnt += board[i][j]
    if cnt == 0:
        return False
    if cnt == size:
        return False
    else:
        return True

white, blue = 0, 0
def cut_paper(start, end):
    """
    종이를 자른다. 종료조건시  global변수 white, blue의 값을 조절한다.
    :param start: [row, col] 시작 좌표
    :param end: [row, col] 종료 좌표
    :return: None(없음)
    """
    global blue, white
    sr, sc = start
    er, ec = end
    if start == end: # 종료조건
        if board[start[0]][start[1]] == 1:
            blue += 1
        else:
            white += 1
        return

    if flag(start, end) is True: # 분리해야 된다면 4등분 한다.
        cut_paper([sr, sc], [(er + sr) // 2, (ec + sc) // 2])  # 왼쪽 위
        cut_paper([sr, (sc + ec)//2+1], [(er + sr) // 2, ec])  # 오른쪽 위
        cut_paper([(sr + er) // 2+1, sc], [er, (ec + sc) // 2])  # 왼쪽 아래
        cut_paper([(sr + er) // 2+1, (sc + ec)//2+1], [er, ec])  # 오른쪽 아래
    else:
        if board[sr][sc] == 1:
            blue += 1
        else:
            white += 1

cut_paper([0,0], [N-1, N-1])
print(white)
print(blue)