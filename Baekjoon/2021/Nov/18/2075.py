'''
Title   : N번째 큰 수
Level   : G5
Problem : NxN 크기의 표에 수가 채워져 있다.
          모든 수는 자신의 한 칸 위에 있는 수보다 크다.
          N번째 큰 수를 찾는다.
Type    : 구현
Idea    : 1. 표의 바닥에서 시작하는 N개의 포인터를 사용하여 값의 크기를 비교한다.
          2. N개중 가장 큰 값을 가리키는 포인터를 한칸 위로 올린다.
          3. 2를 N번 반복한다.
'''

N = int(input())
board = []
for _ in range(N) :
    board.append(list(map(int, input().split())))
pointer = [N-1 for _ in range(N)]
for _ in range(N): # N번 반복으로 N번째 큰 수를 찾는다.
    answer, answer_idx = -1000000001, 0
    for i in range(N): # pointer가 가리키는 N개의 수를 비교한다.
        idx = pointer[i]
        if board[idx][i] > answer:
            answer = board[idx][i]
            answer_idx = i

    pointer[answer_idx] -= 1

print(answer)
