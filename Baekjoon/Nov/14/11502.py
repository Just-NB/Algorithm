'''
Title   : 세 개의 소수문제
Level   : S4
Problem : 5보다 큰 임의의 홀수는 정확히 세 개의 소수들의 합으로 나타낼 수 있다.
          가능한지 알아본다.
          7 <= 정수 < 1000
Type    : 소수판별, 완전 탐색
Idea    : 1. 에라토스테네스의 체를 통해 범위 내의 소수를 판별한다.
          2. 1000이하의 소수는 많지 않으므로 3중 반복문으로 문제를 해결한다.
'''

sieve = [True for _ in range(1001)] #  True : 소수
sieve[0], sieve[1] = False, False
prime = []
for i in range(2, 1000):
    if sieve[i] is True:
        prime.append(i)
        for j in range(i+i, 1000, i):
            sieve[j] = False

T = int(input())
for tc in range(T):
    k = int(input())
    flag = False #  만들지 못한다.
    for i in prime:
        if flag is True :
            break
        for j in prime:
            if flag is True:
                break
            for l in prime:
                if flag is True:
                    break
                if i+j+l == k:
                    flag = True
                    print(i, j, l)

    if flag is False:
        print(0)