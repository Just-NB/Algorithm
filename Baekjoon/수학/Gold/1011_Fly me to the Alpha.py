'''
1  : 1                  - 1
2  : 1 1                - 2
3  : 1 1 1              - 3
4  : 1 2 1              - 3 : 2 * 2 - 1
5  : 1 2 1 1            - 4
6  : 1 2 2 1            - 4
7  : 1 2 2 1 1          - 5
8  : 1 2 2 2 1          - 5
9  : 1 2 3 2 1          - 5 : 3 * 2 - 1
10 : 1 2 3 2 1 1        - 6
11 : 1 2 3 2 2 1        - 6
12 : 1 2 3 3 2 1        - 6
13 : 1 2 3 3 2 1 1      - 7
14 : 1 2 3 3 2 2 1      - 7
15 : 1 2 3 3 3 2 1      - 7
16 : 1 2 3 4 3 2 1      - 7 : 4 * 2 - 1
17 : 1 2 3 4 3 2 1 1    - 8
18 : 1 2 3 4 3 2 2 1    - 8
19 : 1 2 3 4 3 3 2 1    - 8
20 : 1 2 3 4 4 3 2 1    - 8

- - - - -
'''
# import sys
# input = sys.stdin.readline
#
# T = int(input())
# for tc in range(T):
#     x, y = map(int, input().split())
#     length = y - x
#     sqrt = int(length ** 0.5)
#     if length == sqrt * sqrt:
#         print(sqrt * 2 - 1)
#     elif length <= ((sqrt + 1) * (sqrt + 1) + sqrt * sqrt ) // 2:
#         print(sqrt * 2)
#     else:
#         print(sqrt * 2 + 1)

T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    # 출발 및 도착 지점
    d = y - x #거리
    n = 0
    while True:
        if d <= n*(n+1): break
        n += 1 #총 이동 거리가 n의 제곱보다 작거나 같을 때

    if d <= n**2:
        print(n*2-1) #총 이동 거리가 n의 제곱보다 클 때
    else:
        print(n*2)

