import sys
input = sys.stdin.readline

M = int(input())
N = int(input())

prime_number = [True for _ in range(N+1)]
prime_number[0],prime_number[1] = False,False
for i in range(2, N//2+1):
    if prime_number[i] is True:
        idx,cnt = i,2
        while idx*cnt <= N:
            prime_number[idx*cnt] = False
            cnt += 1
prime_sum = 0
prime_min = 10001
for i in range(M, N+1):
    if prime_number[i] is True:
        prime_sum += i
        if prime_min == 10001:
            prime_min = i

if prime_sum == 0 :
    print(-1)
else:
    print(prime_sum)
    print(prime_min)