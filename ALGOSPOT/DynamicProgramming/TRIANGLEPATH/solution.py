cache = []
def solution_brute(path,r,c) :
    try :
        cur = path[c][r]          
    except :
        return 0

    ret = 0
    #down
    down = solution_brute(path, r, c+1)
    #right
    right = solution_brute(path, r+1, c+1)

    ret = max(cur+down, cur+right)
    return ret

#Iterate
def solution(path,length) :
    cache[-1] = path[-1]
    for c in range(length-2, -1, -1) : #0,1,2,3,4
        for r in range(c, -1, -1) : #0,1,2,3,4
            cache[c][r] = path[c][r] + max(cache[c+1][r],cache[c+1][r+1])
#Recursive
def solution2(path, length, y,x) :
    if y == length-1 :
        return path[y][x]
    if cache[y][x] != -1 :
        return cache[y][x]
    cache[y][x] = max(solution2(path,length, y+1, x) , solution2(path,length, y+1, x+1)) + path[y][x]
    return cache[y][x]
C = int(input())

for _ in range(C) :
    N = int(input())
    path = []
    cache = []
    for i in range(N):
        path.append(list(map(int, input().split())))
        cache.append([-1 for i in range(N)])
    #solution(path,N)
    #print(cache[0][0])
    print(solution2(path,N,0,0))