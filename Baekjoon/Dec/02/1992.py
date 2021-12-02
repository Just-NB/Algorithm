'''
Title   : 쿼드트리
Level   : S1
Problem : 쿼드 트리는 0과 1로만 이루어진 2차원 배열의 영상에서 같은 숫자의 점들이 몰려있으면 압축하여 표현한다
          왼쪽 위/ 오른쪽 위/ 왼쪽 아래/ 오른쪽 아래 4개로 영상을 나누어 압축한다.
          압축한 결과를 차례대로 괄호 안에 묶어서 표현한다.

Type    : 재귀, 분할정복
Idea    : 1. 분할 필요 여부 구하기
          1-1. 범위 내 모든 숫자를 더한 후, 범위의 넓이과 더한 값이 같거나 0이면 분할 필요X, 그 이외는 분할 필요 O
          2. 쿼드 트리는 해당 범위가 분할이 필요할 경우, 범위를 4분할 하여 재귀탐색한다.
          3. 범위 분할 방법 : start = [sr, sc]/ end = [er, ec]
          3-1. 왼쪽 위     : start = [sr, sc]/ end = [(er+sr)//2, (ec+sc)//2]
          3-2. 오른쪽 위   : start = [sr, (ec+sc)//2+1]/ end = [(er+sr)//2, ec]
          3-3. 왼쪽 아래   : start = [(er+sr)//2+1, sc]/ end = [er, (ec+sc)//2]
          3-4. 오른쪽 아래 : start = [(er+sr)//2+1, (ec+sc)//2+1]/ end = [er, ec]
'''

def d_flag(start, end):
    """
    쪼개야 하는지 확인하는 함수
    :param start: [row, col] 시작 위치
    :param end: [row, col] 종료 위치
    :return: True(쪼개야 한다)/ Fasle(쪼개지 않아도 된다)
    """
    sum = 0
    size = (end[0] - start[0] + 1) * (end[1] - start[1] + 1)
    for r in range(start[0], end[0]+1):
        for c in range(start[1], end[1]+1):
            sum += int(board[r][c])
    if sum == 0:
        return False
    if sum == size:
        return False
    else:
        return True


N = int(input())
board = []
for n in range(N):
    board.append(input())

def quadtree(start, end, d):
    """
    :param start: [row, col] 시작 위치
    :param end: [row, col] 종료 위치
    :param d: 깊이, 이 값을 기준으로 분할 크기를 결정한다.
    :return: 없음
    """
    if start == end: # 종료조건, 탐색 범위가 1칸일 경우 본인 값 출력
        print(board[start[0]][start[1]], end ='')
        return

    if d_flag(start, end) is True: # 쪼개야 한다면
        sr, sc = start
        er, ec = end
        print('(', end='')
        quadtree([sr, sc], [(er + sr) // 2, (ec + sc) // 2], 1) # 왼쪽 위
        quadtree([sr, (ec + sc) // 2 + 1], [(er + sr) // 2, ec], 2) # 오른쪽 위
        quadtree([(er + sr) // 2 + 1, sc], [er, (ec + sc) // 2], 3) # 왼쪽 아래
        quadtree([(er + sr) // 2 + 1, (ec + sc) // 2 + 1], [er, ec], 4) # 오른쪽 아래
        print(')', end='')
    else:
        print(board[start[0]][start[1]], end='')
        return

quadtree([0, 0], [N-1, N-1], 2)
