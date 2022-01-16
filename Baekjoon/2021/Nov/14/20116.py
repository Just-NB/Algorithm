'''
Title   : 상자의 균형
Level   : S3
Problem : n개의 상자가 있다, 바닥부터 쌓아 올ㄹ린다.  상자의 크기는 2x2
          바닥에 가까이 있는 상자부터 1~n번 상자, i번 상자의 중심은 (xi, 2Lxi-L) == i번 상자 1개의 무게중심
          모든 상자에 대하여, 무게중심의 x좌표가 i번 상자의 구간안에 포함되면 전체가 균형을 이룬다.
Type    : 누적합, 구현
Idea    : 1. 위에서부터 아래로 내려가며 무게중심이 맞는지 확인한다.
          2. 무게중심의 합을 누적시켜나간다.
'''

n, size = map(int, input().split())
center = list(map(int, input().split()))
cnt = 1
acc_center = 0 # 누적 무게중심.
flag = True
for i in range(n-1, 0, -1):
    acc_center = (center[i]+acc_center)
    left, right = center[i-1] - size, center[i-1] + size
    if acc_center/cnt <= left or acc_center/cnt >= right:
        flag = False
        break
    cnt += 1
if flag is True:
    print('stable')
else:
    print('unstable')