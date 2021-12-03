'''
Title   : 2*N 타일링
Level   : S3
Problem : 2*N 크기의 직사각형을 1*2, 2*1 타일로 채우는 방법의 수를 구하는 프로그램을 작성한다.
Type    : 다이나믹 프로그래밍
Idea    : 1. 2*i 칸을 채우는 방법은 2가지를 경우를 생각한다.
          2. 2*(i-1)칸을 채운 방법의 수 + 1개(세로로 세운다)
          3. 2*(i-2)칸을 채운 방법의 수 + 1개(가로로 2칸을 채운다)
'''

N = int(input())
tile = [i for i in range(N+1)]
for i in range(3, N+1):
    tile[i] = tile[i-1] + tile[i-2]
print(tile[-1]%10007)