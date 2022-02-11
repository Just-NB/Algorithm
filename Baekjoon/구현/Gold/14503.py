N, M = map(int, input().split())

board = []
clean = [[False for _ in range(M)] for _ in range(N)]
r, c, d = map(int, input().split())
for n in range(N):
    board.append(list(map(int, input().split())))

dr = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 북 동 남 서
turn_cnt = 0
answer = 1
while True:
    # print(r, c, d, answer)
    left = (d - 1) % 4
    clean[r][c] = True
    nr, nc = r + dr[left][0], c + dr[left][1]
    # a : 왼쪽 방향에 아직 청소를 안했다면
    if board[nr][nc] == 0 and clean[nr][nc] is False:
        # print(nr, nc)
        r, c = nr, nc  # 전진 후
        turn_cnt = 0
        answer += 1
    else:  # b. 청소할 공간이 없다면 회전한다.
        turn_cnt += 1
    d = left

    if turn_cnt == 4:  # 방향 회전만 4번했다면, 4방향 모두 청소했다.
        # 바라보고 있는 방향에서 후진
        turn_cnt = 0
        nr, nc = r - dr[d][0], c - dr[d][1]
        if board[nr][nc] == 0:
            r, c = nr, nc
        elif board[nr][nc] == 1:
            break
print(answer)

