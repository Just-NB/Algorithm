'''
Title   : 스위치와 램프
Level   : S4
Problem : N개의 스위치, M개의 램프가 있다.
          스위치로 연결된 0개 이상의 램프의 전원을 켤 수 있다.
          한 번 켜진 전원은 꺼지지 않는다.
          N-1개의 스위치를 눌러도 모든 램프가 켜지는지 확인한다.
Idea    : 1. 램프의 번호가 idx인 배열을 만든다.
          2. 스위치를 눌렀을때 켜지는 램프의 값을 1씩 추가한다.
          3. 임의의 스위치만 안 눌렀을때도 모든 램프의 값이 1이상이면 N-1개로 모든 램프를 켤 수 있다.
'''
N, M = map(int, input().split())
lamp = [0 for _ in range(M+1)]
turn_on = []
for _ in range(N):
    turn_on.append(list(map(int, input().split()))[1:])
    for t in turn_on[-1]:
        lamp[t] += 1
answer = 1
for to in turn_on:
    answer = 1
    for t in to:
        lamp[t] -= 1
    for l in lamp[1:]:
        if l == 0:
            answer = 0
    for t in to:
        lamp[t] += 1
    if answer == 1:
        break
print(answer)
