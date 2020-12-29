'''
input
3
3 3
1 2 4
3 4 7
3 3
1 2 3
4 5 6
5 3
10 20 30 1 2
10 20 30
output
5
6
5
'''

C = int(input())
N,M = 0,0
A,B = [],[]
cache = []
NEGINF = -9999999999999
def solution(idxA, idxB) :
    if cache[idxA+1][idxB+1] != -1 :
        return cache[idxA+1][idxB+1]
    cache[idxA+1][idxB+1] = 2

    a = A[idxA] if idxA != -1 else NEGINF
    b = B[idxB] if idxB != -1 else NEGINF
    maxElement = max(a,b)
    for nxt in range(idxA+1,N) :
        if maxElement < A[nxt] :
            cache[idxA+1][idxB+1] = max(cache[idxA+1][idxB+1], solution(nxt, idxB) + 1)
    for nxt in range(idxB+1,M) :
        if maxElement < B[nxt] :
            cache[idxA+1][idxB+1] = max(cache[idxA+1][idxB+1], solution(idxA, nxt) + 1)

    return cache[idxA+1][idxB+1]


for _ in range(C) :
    cache = [ [-1 for i in range(101)] for j in range(101)]
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(solution(-1, -1)-2)
