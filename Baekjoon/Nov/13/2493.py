'''
Title   : 탑
Level   : G5
Problem : 높이가 다른 탑이 일렬로 배치되어 있다.
          탑의 왼쪽으로 신호를 보내며, 가장 먼저 만나는 본인보다 높은 탑이 신호를 수신한다.
          각 탑에서 발사한 신호를 어느 탑에서 수신하는지를 알아낸다.
Type    : 구현, 스택
Idea    : 1. 뒤에서부터 시작한다.
          2. 스택의 top과 현재 방문한 타워의 크기를 비교한다.
          3. 방문한 타워의 크기 < top 일 경우, 스택에 추가한다.
          4. 방문한 타워의 크기 >= top 일 경우, 스택에서 빼고 답에 추가한다.
          방문한 타워의 크기가 스택의 top보다 작을 경우, top에 넣어 먼저 레이저 신호를 수신하는 탑을 찾는다.

'''

N = int(input())
tower = list(map(int, input().split()))
length = len(tower)
answer = [0 for _ in range(length)]
stack = []
idx = length-1
while True:
    if idx < 0:
        break
    if len(stack) == 0:
        stack.append((tower[idx], idx))
        idx -= 1
        continue
    if tower[idx] < stack[-1][0]:
        stack.append((tower[idx], idx))
        idx -= 1
    else :
        t, i = stack.pop()
        answer[i] = idx+1
for a in answer:
    print(a, end=' ')