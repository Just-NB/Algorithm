'''
input :
3
7 
7 1 5 9 6 7 3
7 
1 4 4 4 4 1 1
4 
1 8 2 2
output :
20
16
8
'''
def solution(fence,left,right) :
    # 1개일 경우
    if left == right :
        return fence[left]
    mid = (left+right)//2
    #left에서만 찾아보기
    le = solution(fence, left, mid)
    #right에서만 찾아보기
    ri = solution(fence, mid+1, right)
    #left와 right 비교
    ret = max(le,ri)
    
    #걸치는 값 비교
    l, r = (mid), (mid+1)
    #1. 걸치는거 양옆
    height = min(fence[r],fence[l])
    ret = max(ret, height*2)
    #2. 나머지
    while ((r < right) or (l > left)) :
        #오른쪽 펜스가 더 높을 때 or 왼쪽 펜스를 다 봤을 때,
        if (r < right) and ((fence[r+1] > fence[l-1]) or (l == left))  :
            r += 1
            height = min(height, fence[r])
        else :
            l -= 1
            height = min(height, fence[l])
        ret = max(ret, height* (r - l + 1))
    
    return ret

C = int(input())
for _ in range(C) :
    length = int(input())
    fence = list(map(int, input().split()))
    print(solution(fence, 0, length-1))
