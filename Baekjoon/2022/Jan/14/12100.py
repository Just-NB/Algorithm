'''
Title   : 2048 (EASY)
Level   : G2
Problem : N x N 보드에서 즐기는 2048게임이 있다.
          한 번의 이동은 보드 위의 전체 블록을 이동시킨다, 같은 값을 갖는 두 블록이 충돌하면 하나로 합쳐진다.
          보드의 크기와 보드판의 블록 상ㄴ태가 주어졌을 때, 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 프로그램을 작성한다
Type    : 단순 구현
Idea    : 1. 움직임은 보드를 90도 회전한 후, 모두 왼쪽으로 움직인다고 생각하고 풀이한다.
          2. 하나의 row를 이동하고 결과에 합친다.
          3. 하나의 row의 값들을 왼쪽으로 합치기 위해 Queue를 사용한다.
          4. col 크기의 0으로 초기화된 TMP배열을 사용하여 값을 왼쪽으로 모은다.
          5. tmp_idx를 0으로 시작하여 Queue.popleft()와 값을 비교한다.
          6. TMP[tmp_idx]의 값이 합쳐졌거나, v와 다를 경우 idx가 증가한다.
'''
import copy
from collections import deque
LEFT, RIGHT, UP, DOWN = 0, 1, 2, 3

N = int(input())
BOARD = [[[] for _ in range(N)] for _ in range(N)]
for n in range(N):
    BOARD[n] = list(map(int, input().split()))

dr = [(0, -1), (0, 1), (-1, 0), (1, 0)]


# 각 깊이별 이동 방향을 정한다.
def find_max_val(board, move_cnt):
    max_val = 0
    if move_cnt == 5: # 5번 이동했으면 종료.
        for b in board:
            max_val = max(max_val, max(b))
        return max_val
    rotate_board = copy.deepcopy(board)
    for d in range(4):
        rotate_board = list(zip(*rotate_board[::-1]))
        new_board = move(rotate_board)
        max_val = max(find_max_val(new_board, move_cnt + 1), max_val)

    return max_val


def move(board):
    queue = deque()
    result = []
    for b in board:
        for v in b:
            if v != 0: # 0이 아닌 값들을 큐에 넣는다.
                queue.append(v)
        moved_board = [0] * N
        idx = 0
        while len(queue) != 0:
            v = queue.popleft()
            if moved_board[idx] != v and moved_board[idx] != 0:
                idx += 1
            moved_board[idx] += v
            if moved_board[idx] // 2 == v:
                idx += 1
        result.append(moved_board)
    return result

print(find_max_val(BOARD, 0))
# def move(board, d):
#     '''
#     :param board: 이동 시킬 보드의 원본
#     :param d: 이동 방향 :  0(L), 1(R), 2(U), 3(D)
#     :return: d 방향으로 이동 후 생긴 새로운 보드
#     '''
#     new_board = copy.deepcopy(board)
#     if d == LEFT:
#         for r in range(N):
#             pos = 0
#             for c in range(1, N):
#                 cur_val = new_board[r][c]
#                 new_board[r][c] = 0
#                 # board[r][pos]와 board[r][c]를 비교한다.
#                 if cur_val == 0:  # 현재 위치가 0 이면 넘어간다.
#                     continue
#                 if new_board[r][pos] == cur_val:  # 같으면 합친다.
#                     new_board[r][pos] *= 2
#                     pos += 1
#                 elif new_board[r][pos] != cur_val:  # 다르다면
#                     if new_board[r][pos] == 0:  # pos 위치가 0이면 이곳으로 옮긴다.
#                         new_board[r][pos] = cur_val
#                     else:  # 0이 아니라면 한칸 다음으로 옮긴다.
#                         pos += 1
#                         new_board[r][pos] = cur_val
#     elif d == RIGHT:
#         for r in range(N):
#             pos = N - 1
#             for c in range(N - 2, -1, -1):
#                 cur_val = new_board[r][c]
#                 new_board[r][c] = 0
#                 # board[r][pos]와 board[r][c]를 비교한다.
#                 if cur_val == 0:  # 현재 위치가 0 이면 넘어간다.
#                     continue
#                 if new_board[r][pos] == cur_val:  # 같으면 합친다.
#                     new_board[r][pos] *= 2
#                     pos -= 1
#                 elif new_board[r][pos] != cur_val:  # 다르다면
#                     if new_board[r][pos] == 0:  # pos 위치가 0이면 이곳으로 옮긴다.
#                         new_board[r][pos] = cur_val
#                     else:  # 0이 아니라면 한칸 다음으로 옮긴다.
#                         pos -= 1
#                         new_board[r][pos] = cur_val
#     elif d == UP:
#         for c in range(N):
#             pos = 0
#             for r in range(1, N):
#                 cur_val = new_board[r][c]
#                 new_board[r][c] = 0
#                 # board[r][pos]와 board[r][c]를 비교한다.
#                 if cur_val == 0:  # 현재 위치가 0 이면 넘어간다.
#                     continue
#                 if new_board[pos][c] == cur_val:  # 같으면 합친다.
#                     new_board[pos][c] *= 2
#                     pos += 1
#                 elif new_board[pos][c] != cur_val:  # 다르다면
#                     if new_board[pos][c] == 0:  # pos 위치가 0이면 이곳으로 옮긴다.
#                         new_board[pos][c] = cur_val
#                     else:  # 0이 아니라면 한칸 다음으로 옮긴다.
#                         pos += 1
#                         new_board[pos][c] = cur_val
#
#     elif d == DOWN:
#         for c in range(N):
#             pos = N - 1
#             for r in range(N - 2, -1, -1):
#                 cur_val = new_board[r][c]
#                 new_board[r][c] = 0
#                 # board[r][pos]와 board[r][c]를 비교한다.
#                 if cur_val == 0:  # 현재 위치가 0 이면 넘어간다.
#                     continue
#                 if new_board[pos][c] == cur_val:  # 같으면 합친다.
#                     new_board[pos][c] *= 2
#                     pos -= 1
#                 elif new_board[pos][c] != cur_val:  # 다르다면
#                     if new_board[pos][c] == 0:  # pos 위치가 0이면 이곳으로 옮긴다.
#                         new_board[pos][c] = cur_val
#                     else:  # 0이 아니라면 한칸 다음으로 옮긴다.
#                         pos -= 1
#                         new_board[pos][c] = cur_val
#
#     return new_board

