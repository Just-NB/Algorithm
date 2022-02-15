import copy
import sys
from collections import deque
MAX = sys.maxsize
R, C = 0, 1

# 내가 해보고 싶던거.
# 1. rotate함수의 코드 중복을 줄여보고 싶었다.
# 1-1. 과연 좋아진걸까?
# 2. 같은 함수를 이용하여 dfs / bfs를 구현해보고 비교해보고 싶었다.


def make_string(a: list, b: list):
    return str(a[0]) + str(a[1]) + str(b[0]) + str(b[1])


def move(board, a, b, d):
    dr = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    '''
    :param board: 맵, 0 -이동가능, 1 -이동 불가능
    :param pos: 로봇 좌표, a 은 왼쪽/위 에 있음. b 은 오른쪽/아래에 있음
    :param d: 이동방향, 0,1,2,3 : 상,하,좌,우
    :return: 이동 후 좌표, a 은 왼쪽/위 에 있음. b 은 오른쪽/아래에 있음
    '''
    nxt_a, nxt_b = copy.deepcopy(a), copy.deepcopy(b)
    nxt_a[R] += dr[d][R]
    nxt_a[C] += dr[d][C]

    nxt_b[R] += dr[d][R]
    nxt_b[C] += dr[d][C]
    if board[nxt_a[R]][nxt_a[C]] == 1 or board[nxt_b[R]][nxt_b[C]] == 1:
        return [a, b]
    else:
        return [nxt_a, nxt_b]


def rotate(board, a, b, i):
    dr = [-1, 1, -1, 1]
    nxt_a, nxt_b = a, b
    # i : 0/1일때 A가 움직인다.
    # i : 2/3일때 B가 움직인다.

    if a[0] == b[0]:  # 가로일때, row만 변한다.

        if i < 2 and board[b[R] + dr[i]][a[C]] == 0:  # 왼쪽이 움직일 때
            nxt_a = [b[R] + dr[i], b[C]]
        elif i >= 2 and board[a[R] + dr[i]][b[C]] == 0:  # 오른쪽이 움직일 때
            nxt_b = [a[R] + dr[i], a[C]]

    else:  # 세로일때, col만 변한다.
        if i < 2 and board[a[R]][b[C] + dr[i]] == 0:  # 위쪽이 움직일 때
            nxt_a = [b[R], b[C] + dr[i]]
        elif i >= 2 and board[b[R]][a[C] + dr[i]] == 0:  # 아래쪽이 움직일 때
            nxt_b = [a[R], a[C] + dr[i]]

    if board[nxt_a[R]][nxt_a[C]] == 0 and board[nxt_b[R]][nxt_b[C]] == 0:
        if nxt_a[0] < nxt_b[0] or nxt_a[1] < nxt_b[1]:
            return [nxt_a, nxt_b]
        else:
            return [nxt_b, nxt_a]

    return [a, b]


def dfs(board, a, b, depth, visit):
    ret = MAX
    N = len(board) - 2
    if a == [N, N] or b == [N, N]:
        return depth

    # move
    for i in range(4):
        nxt_a, nxt_b = move(board, a, b, i)
        v = make_string(nxt_a, nxt_b)
        if v not in visit:
            visit.add(v)
            ret = min(dfs(board, nxt_a, nxt_b, depth + 1, visit), ret)
            visit.remove(v)

    # rotate
    for i in range(4):
        nxt_a, nxt_b = rotate(board, a, b, i)
        v = make_string(nxt_a, nxt_b)
        if v not in visit:
            visit.add(v)
            ret = min(dfs(board, nxt_a, nxt_b, depth + 1, visit), ret)
            visit.remove(v)

    return ret


def bfs(board, N, visit):
    q = deque()
    q.append([[1, 1], [1, 2], 0])

    while len(q) != 0:
        a, b, d = q.popleft()
        if a == [N, N] or b == [N, N]:
            return d
        # move
        for i in range(4):
            nxt_a, nxt_b = move(board, a, b, i)
            v = make_string(nxt_a, nxt_b)
            if v not in visit:
                visit.add(v)
                q.append([nxt_a, nxt_b, d + 1])

        # rotate
        for i in range(4):
            nxt_a, nxt_b = rotate(board, a, b, i)
            v = make_string(nxt_a, nxt_b)
            if v not in visit:
                visit.add(v)
                q.append([nxt_a, nxt_b, d + 1])


def solution(board):
    answer = 0
    size = len(board)
    new_board = [[1 for _ in range(size + 2)] for _ in range(size + 2)]
    for i in range(size):
        for j in range(size):
            new_board[i + 1][j + 1] = board[i][j]
    visit = set()
    visit.add("1112")
    # answer = dfs(new_board, [1, 1], [1, 2], 0, visit)
    answer = bfs(new_board, size, visit)
    return answer



# print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
# print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]]))
print(solution([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))





from queue import Queue


def solution(board):
    answer = 0
    size = len(board)
    p1, p2 = (0, 0), (0, 1)

    def isValid(p1, p2):
        Y, X = 0, 1
        if 0 <= p1[Y] < size and 0 <= p1[X] < size and 0 <= p2[Y] < size and 0 <= p2[X] < size:
            if board[p1[Y]][p1[X]] == 0 and board[p2[Y]][p2[X]] == 0:
                return True
        return False

    def move(p1, p2):
        Y, X = 0, 1
        DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        cand = []
        for dy, dx in DELTAS:
            try:
                nxt1 = (p1[Y] + dy, p1[X] + dx)
                nxt2 = (p2[Y] + dy, p2[X] + dx)
                if isValid(nxt1, nxt2):
                    cand.append((nxt1, nxt2))
            except:
                print(p1, dy, dx, p2)
        return cand

    def rotate(p1, p2):
        cand = []
        for d in [-1, 1]:
            Y, X = 0, 1
            if p1[Y] == p2[Y]:
                nxt1 = (p1[Y] + d, p1[X]) # p1고정, p2움직임.
                nxt2 = (p2[Y] + d, p2[X])
            else:
                nxt1 = (p1[Y], p1[X] + d)
                nxt2 = (p2[Y], p2[X] + d)

            if isValid(nxt1, nxt2):
                cand.append((p1, nxt1))
                cand.append((p2, nxt2))
        return cand

    def rotate(p1, p2):
        # 가로로 있을때
        Y, X = 0, 1
        cand = []
        if p1[Y] == p2[Y]:
            UP, DOWN = -1, 1
            for d in [UP, DOWN]:
                nxt1 = (p1[Y] + d, p1[X])
                nxt2 = (p2[Y] + d, p2[X])
                if isValid(nxt1, nxt2):
                    cand.append((p1, nxt1))
                    cand.append((p2, nxt2))
        else:
            # 세로로 있을 때
            LEFT, RIGHT = -1, 1
            for d in [LEFT, RIGHT]:
                nxt1 = (p1[Y], p1[X] + d)
                nxt2 = (p2[Y], p2[X] + d)
                if isValid(nxt1, nxt2):
                    cand.append((p1, nxt1))
                    cand.append((p2, nxt2))
        return cand

    queue = Queue()
    queue.put((p1, p2, 0))
    done = set([(p1, p2)])
    # BFS
    while queue.empty() == False:
        q = queue.get()
        if q[0] == (size - 1, size - 1) or q[1] == (size - 1, size - 1):
            return q[2]
        # 움직이고 넣는다.
        for cand in move(q[0], q[1]):
            if cand not in done:
                done.add(cand)
                queue.put((cand[0], cand[1], q[2] + 1))

        # 회전하고 넣는다.
        for cand in rotate(q[0], q[1]):
            if cand not in done:
                done.add(cand)
                queue.put((*cand, q[2] + 1))

    return answer
