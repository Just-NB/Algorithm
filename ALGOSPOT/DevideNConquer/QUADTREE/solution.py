'''
input
4
w
xbwwb
xbwxwbbwb
xxwwwbxwxwbbbwwxxxwwbbbwwwwbb

output
w
xwbbw
xxbwwbbbw
xxwbxwwxbbwwbwbxwbwwxwwwxbbwb

'''

'''
    QuadTree : xbwwb 
    1) xAB 로 축약
    2) xBA 로 변환
    3) A,B 내부에서 x를 만나면 1~2과정 반복
'''

def solution(quadtree,idx) :
    if quadtree[idx] in 'wb' : 
        return quadtree[idx]

    idx += 1
    A = solution(quadtree,idx)
    idx += len(A)
    B = solution(quadtree,idx)
    idx += len(B)
    C = solution(quadtree,idx)
    idx += len(C)
    D = solution(quadtree,idx)
    
    return 'x' + C + D + A + B


C = int(input())
for _ in range(C) :
    print(solution(input(), 0))

# assert solution('xbwwb',0) == 'xwbbw'
# assert solution('xbwxwbbwb',0) == 'xxbwwbbbw'
# assert solution('xxwwwbxwxwbbbwwxxxwwbbbwwwwbb',0) == 'xxwbxwwxbbwwbwbxwbwwxwwwxbbwb'