dr = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
MAX = 9999
def is_valid(r, c, board):
    if 0 <= r < len(board) and 0 <= c < len(board[0]):
        if board[r][c] == 1:
            return True
        return False
    return False



def play_game(board, loc, turn):
    '''
    A가 무조건 이기거나 무조건 질 때 turn의 최소횟수를 찾는다.
    :param board: 게임 보드
    :param loc: [aloc, bloc] -> [a의 row,col, b의 row, col]
    :param turn: 짝수 - a의 턴 , 홀수 - b의 턴
    :returns : [ winner, turn ] -> 승자/ 이기기 까지의 턴
    '''
    move_cnt = 0
    nxt_loc = [[], []]
    min_turn, max_turn = MAX, 0

    # 움직일 수 없으면 게임이 끝난다.
    movable = False
    for i in range(4):
        nxt_r = loc[turn % 2][0] + dr[i][0]  # turn % 2 == 0 이면 A
        nxt_c = loc[turn % 2][1] + dr[i][1]  # turn % 2 == 1 이면 B
        nxt_loc[turn % 2] = [nxt_r, nxt_c]
        nxt_loc[(turn + 1) % 2] = loc[(turn + 1) % 2]
        if is_valid(nxt_r, nxt_c, board):
            movable = True
            break
    if movable is False:  # 못움직이면 나는 진다.
        return [(turn + 1) % 2, turn]
    # 현재 내 발판이 없을때 게임이 끝난다.
    if loc[0] == loc[1]:
        # print(turn, min_turn, max_turn, loc)
        # turn % 2 == 0, 현재 A턴, A가 이동하면 A는 승리한다.
        # turn % 2 == 1, 현재 B턴, B가 이동하면 B는 승리한다.
        # [ 승자 , 턴 ]
        return [turn % 2, turn + 1]  # 현재 턴인 사람이 승리.

    for i in range(4):
        nxt_r = loc[turn % 2][0] + dr[i][0]  # turn % 2 == 0 이면 A
        nxt_c = loc[turn % 2][1] + dr[i][1]  # turn % 2 == 1 이면 B
        nxt_loc[turn % 2] = [nxt_r, nxt_c]
        nxt_loc[(turn + 1) % 2] = loc[(turn + 1) % 2]

        if is_valid(nxt_r, nxt_c, board):
            move_cnt += 1
            board[loc[turn % 2][0]][loc[turn % 2][1]] = 0
            ret = play_game(board, nxt_loc, turn + 1)
            board[loc[turn % 2][0]][loc[turn % 2][1]] = 1

            if ret[0] != (turn % 2): # 내가 패배하는게 확정 됬다면 턴을 최대한 끌고간다.
                max_turn = max(max_turn, ret[1])
            else: # 내가 승리하는게 확정 됬다면 턴을 최소로 끌고간다.
                min_turn = min(min_turn, ret[1])
    # print(turn, min_turn, max_turn, loc)
    if max_turn == 0 and min_turn == MAX:  # 움직이지 않았다.
        # turn % 2 == 0, 현재 A턴, A는 이동하지 못했다. B의 승리
        # turn % 2 == 1, 현재 B턴, B는 이동하지 못했다. A의 승리
        # [ 승자, 턴 ]
        return [(turn + 1) % 2, turn]
    elif min_turn != MAX:  # 무조건 이긴다.
        return [turn % 2, min_turn]
    else:  # 무조건 진다.
        return [(turn + 1) % 2, max_turn]

def solution(board, aloc, bloc):
    answer = play_game(board, [aloc, bloc], 0)
    return answer[1]


print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))
print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]))