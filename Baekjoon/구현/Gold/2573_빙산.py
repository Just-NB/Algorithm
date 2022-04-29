from collections import deque
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

def melt(board: list) -> list:
    new_board = [[0 for _ in range(M)] for _ in range(N)]

    for r in range(N):
        for c in range(M):
            if board[r][c] == 0: continue
            sea = 0
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < N and 0 <= nc < M:
                    if board[nr][nc] == 0:
                        sea += 1
            new_board[r][c] = max(0, board[r][c] - sea)
    return new_board

def is_divide() -> int:
    visit = [[False for _ in range(M)] for _ in range(N)]
    ret = 0
    for r in range(N):
        for c in range(M):
            if board[r][c] == 0: continue
            if visit[r][c]: continue
            ret += 1
            if ret == 2: return ret # 2번이상 bfs시, 분리되어있다.

            bfs = deque()
            bfs.append([r, c])
            visit[r][c] = True
            while bfs:
                cr, cc = bfs.popleft()
                for i in range(4):
                    nr, nc = cr + dr[i], cc + dc[i]
                    if 0 <= nr < N and 0 <= nc < M:
                        if visit[nr][nc]: continue
                        if board[nr][nc] == 0: continue
                        visit[nr][nc] = True
                        bfs.append([nr, nc])
    # 0 : 빙산이 모두 녹은 상태
    # 1 : 빙산이 하나의 덩어리
    return ret

answer = 0
while 1:
    dividable = is_divide()
    if dividable == 0:
        print(0)
        break
    elif dividable == 2:
        print(answer)
        break

    board = melt(board)
    answer += 1