'''
6
6
10
13
9
8
1
'''
import sys
input = sys.stdin.readline

length = int(input())
N = [0] + [int(input()) for _ in range(length)]
DP = [N[_] for _ in range(length + 1)]
if length == 1:
    print(N[1])
elif length == 2:
    print(N[1] + N[2])
else:
    DP[1], DP[2] = N[1], N[1] + N[2]

    for i in range(3, length + 1):
        # a = DP[i - 3] + N[i - 2] + N[i - 1]
        a = DP[i - 1]
        b = DP[i - 2] + N[i]
        c = DP[i - 3] + N[i - 1] + N[i]
        DP[i] = max(a, b, c)
    print(DP[-1])