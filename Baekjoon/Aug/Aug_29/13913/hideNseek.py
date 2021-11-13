from collections import deque
N,K = map(int, input().split())

bfs = deque() # [Num, depth]
bfs.append([N,0])
check = [-1 for _ in range(100001)] # 해당 숫자에 방문 했는지 확인. 중복체크 안하기 위함.
answer = []
while bfs:
    cur,depth = bfs.popleft()
    if cur == K:
        print(depth)
        idx = cur
        while idx != N:
            answer.append(idx)
            idx = check[idx]
        answer.append(N)
        for a in answer[::-1]:
            print(a, end=' ')
        break
    if cur-1 >= 0 and check[cur-1] == -1:
        check[cur-1] = cur
        bfs.append([cur-1, depth+1])

    if cur+1 <= 100000 and check[cur+1] == -1:
        check[cur+1] = cur
        bfs.append([cur+1, depth+1])

    if cur*2 <= 100000 and check[cur*2] == -1:
        check[2*cur] = cur
        bfs.append([cur*2, depth+1])
