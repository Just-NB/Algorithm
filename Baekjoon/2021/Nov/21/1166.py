'''
Title   : 선물
Level   : S3
Problem : 선물할 같은 크기의 작은 박스 N개 있다. 크기는 AxAxA이다.
          LxWxH인 직육면체 박스에 모두 넣으려고 한다.
          N,L,W,H가 주어질 때, 가능한 A의 최댓값을 찾는다.
Type    : 수학 이분탐색
Idea    : 1. (AxAxA)*N <= LxWxH가 되는 최소지점을 찾는다.
          1-1. N만을 남기고 모두 우변으로 옮겨서 계산한다.
          2. left = 1, right = min(L,W,H)에서 시작한다.
          2-1. 상자 한 변의 크기는 L,W,H를 넘길 수 없기 때문이다.
          3. 탐색할때 left = mid, right = mid, 로 +1을 하지 않는다. 소수점 단위로 움직이기 때문
'''

n, l, w, h = map(int, input().split())
left, right = 0, min(l, w, h)
for _ in range(100000):
    mid = (left + right) / 2
    if n <= ((l//mid) * (w//mid) * (h//mid)):
        left = mid
    else:
        right = mid
print(left)