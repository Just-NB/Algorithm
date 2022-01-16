'''
Title   : 선분교차 2
Level   : G2
Problem : L1, L2 선분이 주어졌을때, 교차하는지 아닌지 구해본다.
          한 선분의 끝 점이 다른 선분이나 끝 점 위에 있는 것도 교차하는 것이다.
Type    : 수학
Idea    : 1. CCW : 세 점의 위치관계를 나타내는 공식
          2. CCW < 0 : 시계방향/ CCW > 0 : 반시계 방향/ CCW = 0 : 직선
          3. L1와 L2각 점들의 CCW 2개를 곱하여 음수가 나온다면 교차한다.
          4. 둘 중 하나가 0이 나온다면 0이나온 점이 A,B 사이에 있다면 교차한다.
'''

def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])

def check_boundary(a, b, c):
    if min(a[0], b[0]) <= c[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= c[1] <= max(a[1], b[1]):
        return True
    else:
        return False


L1 = list(map(int, input().split()))
L2 = list(map(int, input().split()))

A, B = L1[:2], L1[2:]
C, D = L2[:2], L2[2:]

abc = ccw(A, B, C)
abd = ccw(A, B, D)
cda = ccw(C, D, A)
cdb = ccw(C, D, B)

if abc * abd < 0 and cdb * cda < 0:
    print(1)
elif abc == 0 and check_boundary(A, B, C):
    print(1)
elif abd == 0 and check_boundary(A, B, D):
    print(1)
elif cda == 0 and check_boundary(C, D, A):
    print(1)
elif cdb == 0 and check_boundary(C, D, B):
    print(1)
else:
    print(0)

