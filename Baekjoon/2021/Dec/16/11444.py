# '''
# Title   : 피보나치 수 6
# Level   : G3
# Problem : N은 1,000,000,000,000,000,000보다 작거나 같은 자연수 일때 N번째 피보나치 수를 구하는 프로그램을 작성한다.
# Type    : 수학, 다이나믹 프로그래밍
# Idea    : 1. 도가뉴 항등식이 있다.
#           1-1. F_(m+n) = F_(m-1)*F_n + F_m*F_(n+1)
#           2. 도가뉴 항등식을 이용하여 짝수항/홀수항을 다음과 같이 정리할 수 있다.
#           2-1. 짝수항 F_2n = F_n(F_n + 2F_(n-1))
#           2-2. 홀수항 F_(2n-1) = F_n**2 + F_(n-1)**2
#           3. N이 큰 수 이므로, 배열에 값을 memo하지 못한다. dict자료형을 이용하여 값을 memo한다.
# '''
import sys
input = sys.stdin.readline
N = int(input())
memo = {0: 0, 1: 1, 2: 1}

cnt = 0
def fibo(n):
    if memo.get(n):
        return memo[n]

    global cnt
    cnt += 1
    nxt = n // 2
    if n % 2 != 0:
        nxt += 1

    a = fibo(nxt)
    b = fibo(nxt-1)

    if n % 2 == 0:
        ret = a*(a+2*b)
    else:
        ret = a**2+b**2

    memo[n] = ret % 1000000007

    return memo[n]
print(fibo(N))
