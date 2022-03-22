wheels = [input() for _ in range(4)]
K = int(input())


def rotate(wheel:int, cw: int, meet:list) -> None:
    global wheels, rotated
    if rotated[wheel]:
        return

    rotated[wheel] = True

    if meet[wheel][0]:
        rotate(wheel - 1, cw * -1, meet)
    if meet[wheel][1] :
        rotate(wheel + 1, cw * -1, meet)

    if cw == 1:
        wheels[wheel] = wheels[wheel][7] + wheels[wheel][:7]
    else:
        wheels[wheel] = wheels[wheel][1:] + wheels[wheel][0]


for k in range(K):
    wn, cw = map(int, input().split()) # wheel_num / clock_wise
    meet = [[False, False] for _ in range(4)]

    # 맞물려있는 톱니 확인.
    for i in range(4):
        if i != 3: # 오른쪽 비교
            meet[i][1] = not(wheels[i][2] == wheels[i + 1][6])
        if i != 0: # 왼쪽 비교
            meet[i][0] = not(wheels[i][6] == wheels[i - 1][2])
    rotated = [False for _ in range(4)]
    # 회전
    rotate(wn - 1, cw, meet)
answer = 0
for i, wheel in enumerate(wheels):
    if wheel[0] == '1':
        answer = answer + (2 ** i)
print(answer)