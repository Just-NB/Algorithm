## template
N = int(input())
x, y, r = map(int, input().split())
MAT = [[0 for _ in range(N)] for _ in range(N)]
x -= 1
y -= 1
MAT[x][y] = 'x'
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for i in range(N) :
    for j in range(N) :
        dist = abs(i-x) + abs(j-y)
        if dist <= r :
            MAT[i][j] = dist
        if dist == 0 :
            MAT[i][j] = 'x'
for ma in MAT:
    for m in ma:
        print(m,end = ' ')
    print()