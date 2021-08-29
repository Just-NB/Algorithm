import math
T = int(input())
for tc in range(T):
    N = int(input())
    students = []
    isFinish = [False for _ in range(N)]

    for n in range(N):
        students.append(list(map(int, input().split())))

    cnt = 0
    while False in isFinish:
        cnt += 1
        corridor = []

        for n in range(N):
            curS = students[n]

            if not isFinish[n]:
                #큰걸 뒤로 옮기기
                if curS[0] > curS[1]:
                    curS[0], curS[1] = curS[1], curS[0]
                if len(corridor) == 0:
                    corridor.append(curS)
                    isFinish[n] = True

                else:
                    length = len(corridor)
                    overlap = False
                    for i in range(length):
                        c = corridor[i]
                        #큰걸 뒤에 옮기기.
                        if c[0] > c[1]:
                            c[0], c[1] = c[1], c[0]

                        # 3,4 는 겹친다.
                        # 반례 100 50 / 48 2 가 걸렸다.
                        if c[0] < curS[1] and math.ceil(c[0]/2) == math.ceil(curS[1]/2):
                            overlap = True
                            break
                        elif curS[1] < c[0] and math.ceil(c[0]/2) == math.ceil(curS[1]/2):
                            overlap = True
                            break
                        elif c[1] < curS[0] and math.ceil(c[1]/2) == math.ceil(curS[0]/2):
                            overlap = True
                            break
                        elif curS[0] < c[1] and math.ceil(c[1]/2) == math.ceil(curS[0]/2):
                            overlap = True
                            break

                        if c[0] <= curS[0] <= c[1] or c[0] <= curS[1] <= c[1]:
                            overlap = True
                            break
                        elif curS[0] <= c[0] <= curS[1] or curS[0] <= c[1] <= curS[1] :
                            overlap = True
                            break

                    if not overlap:
                        corridor.append(curS)
                        isFinish[n] = True

    print(f'#{tc+1} {cnt}')
